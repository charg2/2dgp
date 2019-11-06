
from GameObject import *;
from Graphic import *;
from math import*;
from FrameWork import *;
from KeyIO import *;
from Const import *;
from CollisionRect import*;

from Player import Player;

from BelialBullet import *;

from typing import List;


attack_speed = 3;
RUN_L, RUN_R, IDLE_R, IDLE_L = range(4);
class Belial(GameObject):
    LOAD:bool = False;
    IMGSForIdle:List[Image] = [];
    FieldOfView:float = 0.0;

    def __init__(self, x, y, angle, sx, sy, state):
        super(Belial, self).__init__(x, y, angle, sx, sy, state);
        self.has_image = True;
        if Belial.LOAD == False:
            
            Belial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (1).png'));
            Belial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (2).png'));
            Belial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (3).png'));
            Belial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (4).png'));
            Belial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (5).png'));
            Belial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (6).png'));
            Belial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (7).png'));
            Belial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (8).png'));
            Belial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (9).png'));
            Belial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (10).png'));
    
            Belial.FieldOfView = Const.BANSHEE_FIELD_OF_VIEW;

            Belial.LOAD = True;
        
        self.name = "Belial";

        self.m_dir = RUN_R;
        self.IMG = Belial.IMGSForIdleR[0];
        self.force_x =6; 
        self.force_y =8;
        self.collider:Collision = CollisionRect(x,y, self.IMG.w // 2, self.IMG.h // 2);

        # attack
        # bullet 공격의 경우 .1초 간격으로 4방향 30발 
        # laser 공격의 경우 3번 연속 레이저
        # 검 날리기 인데 이건 아직 고려 중.
        self.attack_trigger:bool = False;
        self.attack_timer:float = 0;
        self.attack_key_timer:float = 0.5;

        # animation
        self.animation_numb = 0;
        self.animation_timer = 0.0;
        self.animation_state = RUN_L;

        self.dir = Const.direction_L; 
        self.last_dir = RUN_L % 2;
        self.current_state = IdleStateForBelial(self);
        self.tag = Const.TAG_MONSTER;

        #self.bullets:List[BelialBullet] = [];

    def render(self): 
        self.current_state.render();
        #for bullet in self.bullets:
        #    bullet.render();
        #return;

    def render_debug(self): 
        if self.collider :
            from Graphic import GraphicLib;
            GraphicLib.DebugImg1.draw(self.previous_transform.tx - GameObject.Cam.camera_offset_x, self.previous_transform.ty - GameObject.Cam.camera_offset_y);    

        return;

    def update(self, time):
        # 플레이어와의 거리 체크 해서 어느 근처 거리면 다가가기 시작.
        self.update_component();
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
        if Belial.FieldOfView >= Const.distance(  self.transform.tx
                                                 , self.transform.ty
                                                 , Player.MyPlayer.transform.tx
                                                 , Player.MyPlayer.transform.ty ) :
            self.attack_trigger = True;


        if True == self.attack_trigger :
            self.attack_timer += time;

            if(self.attack_timer > attack_speed):
                self.fire();

                self.attack_timer = 0;
        
        #for bullet in self.bullets:
        #    bullet.update(time);

        return;
    

    def forStateMachine(self):
        self.current_state.update();

        if len(self.state_queue) > 0:
            temp = self.current_state;
            self.current_state.exit();
            self.current_state = self.state_queue.pop();
            del temp;

    def update_component(self):
        self.previous_transform = self.transform;
        self.collider.cx, self.collider.cy = self.transform.tx, self.transform.ty;

        
        return;

    def clampingInWindow(self):
        self.transform.tx = Const.clamp(0, self.transform.tx, GameObject.Cam.map_width-self.IMG.w//16)  
        self.transform.ty = Const.clamp(0, self.transform.ty, GameObject.Cam.map_height-self.IMG.h//8)
        return;

    def on_collision(self, obj):
        print("Belial.py {0}-{1}".format(self.tag, obj.tag));
        pass;

    def fire(self):
        tx = self.transform.tx;
        ty = self.transform.ty;

        from FrameWork import FrameWork;

        FrameWork.CurScene.add_projectile(BelialBullet(FrameWork.CurScene, tx, ty, 0.25,1,1, True)); 
        FrameWork.CurScene.add_projectile(BelialBullet(FrameWork.CurScene, tx, ty, 0.-25,1,1, True)); 
        FrameWork.CurScene.add_projectile(BelialBullet(FrameWork.CurScene, tx, ty, 0.75,1,1, True)); 
        FrameWork.CurScene.add_projectile(BelialBullet(FrameWork.CurScene, tx, ty, 0.-75,1,1, True)); 


        pass;


