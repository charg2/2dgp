
from GameObject import *;
from Graphic import *;
from math import*;
from FrameWork import *;
from KeyIO import *;
from Const import *;
from CollisionRect import*;

from Player import Player;
from IdleStateForBanshee import *;

from BansheeBullet import *;

#component
from HitComponent import *;
#ui
from HPBarForMonster import *;

from typing import List;

# 플레이어에게 접근 하는 패턴만 추가하면 완성.

max_hp = 100;
attack_speed = 3;
RUN_L, RUN_R, IDLE_R, IDLE_L = range(4);
hit_recovery_time = 0.2;
class Banshee(GameObject):
    LOAD:bool = False;
    UNIQUE_ID:int = 0;
    IMGSForIdleL:List[Image] = [];
    IMGSForIdleR:List[Image] = [];
    IMGSForBullet:List[Image] = [];
    FieldOfView:float = 0.0;
    
    def __init__(self, x, y, angle, sx, sy, state):
        super(Banshee, self).__init__(x, y, angle, sx, sy, state);
        self.has_image = True;
        if Banshee.LOAD == False:
            Banshee.IMGSForIdleR.append(pico2d.load_image('assets/Monster/Banshee/Idle/R (1).png'));
            Banshee.IMGSForIdleR.append(pico2d.load_image('assets/Monster/Banshee/Idle/R (2).png'));
            Banshee.IMGSForIdleL.append(pico2d.load_image('assets/Monster/Banshee/Idle/L (1).png'));
            Banshee.IMGSForIdleL.append(pico2d.load_image('assets/Monster/Banshee/Idle/L (2).png'));
    
            Banshee.FieldOfView = Const.BANSHEE_FIELD_OF_VIEW;

            Banshee.SOUND = load_wav('assets/Monster/Banshee/banshee.wav');
            Banshee.SOUND.set_volume(50);

            Banshee.LOAD = True;
        
        self.name = "Banshee_" + str(Banshee.UNIQUE_ID);
        Banshee.UNIQUE_ID += 1;

        self.m_dir = RUN_R;
        self.IMG = Banshee.IMGSForIdleR[0];
        self.force_x =6; 
        self.force_y =8;
        self.collider:Collision = CollisionRect(x,y, self.IMG.w // 2, self.IMG.h // 2);

        # status
        self.current_hp = 50;
        self.max_hp     = 50;

        # attack
        self.attack_trigger:bool = False;
        self.attack_timer:float = 0;
        self.attack_key_timer:float = 0.5;

        # animation
        self.animation_numb = 0;
        self.animation_timer = 0.0;
        self.animation_state = RUN_L;

        # hit component
        self.hit_component = HitComponent(hit_recovery_time);
        self.hp_ui = HPBarForMonster(self, self.transform.tx, self.transform.ty, 1, 1, 1, True);

        self.dir = Const.direction_L; 
        self.last_dir = RUN_L % 2;
        self.current_state = IdleStateForBanshee(self);
        self.tag = Const.TAG_MONSTER;


    def render(self): 
        self.current_state.render();
        if False == self.hit_component.can_hitted():
            self.hp_ui.render();
        #self.hp_ui.render();


    def render_debug(self): 
        if self.collider :
            draw_rectangle(*self.collider.get_area_offset(GameObject.Cam.camera_offset_x, GameObject.Cam.camera_offset_y));
        return;

    def update(self, time):
        self.update_component(time);
        self.forStateMachine();
        self.update_timer(time);
        self.clampingInWindow();
        pass;


    def update_timer(self,time):
        self.basictimer += time;
        self.animation_timer += time;
        self.attack_key_timer += time;
        self.last_dir = (self.dir%2);

        if(self.animation_timer >0.1):
            self.animation_numb = self.animation_numb+1;
            self.animation_timer = 0;

        # 시야 범위 안에 드는지 체크.
        if Banshee.FieldOfView >= Const.distance(  self.transform.tx
                                                 , self.transform.ty
                                                 , Player.MyPlayer.transform.tx
                                                 , Player.MyPlayer.transform.ty ) :
            self.attack_trigger = True;

        if True == self.attack_trigger :
            self.attack_timer += time;
            if(self.attack_timer > attack_speed):
                self.fire();
                self.attack_timer = 0;
        return;

    def forStateMachine(self):
        self.current_state.update();

        if len(self.state_queue) > 0:
            temp = self.current_state;
            self.current_state.exit();
            self.current_state = self.state_queue.pop();
            del temp;

    def update_component(self, time):
        self.previous_transform = self.transform;
        self.collider.cx, self.collider.cy = self.transform.tx, self.transform.ty;
        self.hit_component.update(time);
        #self.hp_ui.update(time);

        return;

    def clampingInWindow(self):
        self.transform.tx = Const.clamp(0, self.transform.tx, GameObject.Cam.map_width-self.IMG.w//16)  
        self.transform.ty = Const.clamp(0, self.transform.ty, GameObject.Cam.map_height-self.IMG.h//8)
        return;

    def on_collision(self, obj):
        #if Const.TAG_PLAYER_PROJECTILE == obj.tag :
        #    calc_hp(obj.damage);
        pass;


    def fire(self):
        Banshee.SOUND.play(1);

        tx = self.transform.tx;
        ty = self.transform.ty;

        from FrameWork import FrameWork;

        FrameWork.CurScene.add_projectile(BansheeBullet(FrameWork.CurScene, tx, ty, 0,1,1, True)); 
        FrameWork.CurScene.add_projectile(BansheeBullet(FrameWork.CurScene, tx, ty, 0.25,1,1, True)); 
        FrameWork.CurScene.add_projectile(BansheeBullet(FrameWork.CurScene, tx, ty, 0.5,1,1, True)); 
        FrameWork.CurScene.add_projectile(BansheeBullet(FrameWork.CurScene, tx, ty, 0.75,1,1, True)); 
        FrameWork.CurScene.add_projectile(BansheeBullet(FrameWork.CurScene, tx, ty, 1,1,1, True)); 
        FrameWork.CurScene.add_projectile(BansheeBullet(FrameWork.CurScene, tx, ty, -0.25,1,1, True)); 
        FrameWork.CurScene.add_projectile(BansheeBullet(FrameWork.CurScene, tx, ty, -0.5,1,1, True)); 
        FrameWork.CurScene.add_projectile(BansheeBullet(FrameWork.CurScene, tx, ty, -0.75,1,1, True)); 
        
    def calc_hp(self, damage):
        #if False == self.is_death :
            self.current_hp -= damage;
            if self.current_hp < 0:
                self.current_hp = 0;
                self.state = False;
