
from GameObject import *;
from Graphic import *;
from math import*;
from FrameWork import *;
from KeyIO import *;
from Const import *;
from CollisionRect import*;

#component
from HitComponent import *;
#ui
from HPBarForMonster import *;

from Player import Player;
#from IdleStateForSkeletonArcher import *; # 미 적용.

from typing import List;

max_hp = 50;
attack_speed = 2;
hit_recovery_time = 0.2;
IDLE_L, IDLE_R = range(2);
class SkeletonArcher(GameObject):
    LOAD:bool = False;
    UNIQUE_ID:int = 0;
    IMGS:Image = None;
    IMGForR:Image = None;
    IMGSForBullet:List[Image] = [];
    FieldOfView:float = 0.0;

    def __init__(self, x, y, angle, sx, sy, state):
        super(SkeletonArcher, self).__init__(x, y, angle, sx, sy, state);
        self.has_image = True;
        if SkeletonArcher.LOAD == False:
            
            SkeletonArcher.IMGS = pico2d.load_image('assets/Monster/SkeletonArcher/Idle/L.png');
            SkeletonArcher.IMGForR = pico2d.load_image('assets/Monster/SkeletonArcher/Idle/R.png');
        
            # bullet
            SkeletonArcher.IMGSForBullet.append(pico2d.load_image('assets/Monster/SkeletonArcher/Arrow/Arrow.png'));
            
            SkeletonArcher.FieldOfView = Const.BANSHEE_FIELD_OF_VIEW;
            
            SkeletonArcher.DIE_SOUND = load_wav('assets/Monster/MonsterDie.wav');
            SkeletonArcher.DIE_SOUND.set_volume(50);
            SkeletonArcher.BEFORE_SHOT = load_wav('assets/Monster/SkeletonArcher/before_bow_shot.wav');
            SkeletonArcher.BEFORE_SHOT.set_volume(50);
            SkeletonArcher.AFTER_SHOT = load_wav('assets/Monster/SkeletonArcher/after_bow_shot.wav');
            SkeletonArcher.AFTER_SHOT.set_volume(50);
            SkeletonArcher.LOAD = True;
        
        self.name = "SkeletonArcher_" + str(SkeletonArcher.UNIQUE_ID); # For Debug
        SkeletonArcher.UNIQUE_ID += 1;

        self.IMG = SkeletonArcher.IMGS;
        self.collider:Collision = CollisionRect(x,y, self.IMG.w // 2, self.IMG.h // 2);

        # attack
        self.attack_trigger:bool = False;
        self.attack_timer:float = 0;
        self.attack_key_timer:float = 0.5;

        # animation
        self.attack_speed:float = 10.0;
        self.dir:int = Const.direction_L; 
        self.tag:int = Const.TAG_MONSTER;

        # status
        self.current_hp = 50;
        self.max_hp     = 50;

        # hit component
        self.hit_component = HitComponent(hit_recovery_time);
        self.hp_ui = HPBarForMonster(self, self.transform.tx, self.transform.ty, 1, 1, 1, True);

    def render(self): 
        self.IMG.clip_composite_draw(0,0,
                   self.IMG.w,
                   self.IMG.h,
                   0,'', 
                   self.transform.tx-GameObject.Cam.camera_offset_x,
                   self.transform.ty-GameObject.Cam.camera_offset_y,
                   );
        if False == self.hit_component.can_hitted():
            self.hp_ui.render();


    def render_debug(self): 
        if self.collider :
            draw_rectangle(*self.collider.get_area_offset(GameObject.Cam.camera_offset_x, GameObject.Cam.camera_offset_y));

        return;

    def update(self, time):
        # 플레이어와의 거리 체크 해서 어느 근처 거리면 다가가기 시작.
        self.update_component(time);
        #self.forStateMachine();
        self.update_timer(time);
        self.update_dir();
        pass;

    def update_component(self, time):
        self.hit_component.update(time);

    def update_timer(self,time):
        self.basictimer += time;
        self.attack_key_timer += time;

        # 방향 체크.
        # 무조건 플레이어를 바라 봄.

        # 시야 범위 안에 드는지 체크.
        if SkeletonArcher.FieldOfView >= Const.distance(  self.transform.tx
                                                        , self.transform.ty
                                                        , Player.MyPlayer.transform.tx
                                                        , Player.MyPlayer.transform.ty ) :
            self.attack_trigger = True;
            #SkeletonArcher.BEFORE_SHOT.play(1);


        if True == self.attack_trigger :
            self.attack_timer += time;
            if(self.attack_timer > attack_speed):
                #SkeletonArcher.AFTER_SHOT.play(1);
                self.fire();
                self.attack_timer = 0;
        
    
        return;
    
    def update_dir(self):
        if ( self.transform.tx - Player.MyPlayer.transform.tx ) > 0 : # 내 오른쪽에 플레이어가;;
            self.IMG = SkeletonArcher.IMGS;
            self.dir = Const.direction_L;
        else:
            self.IMG = SkeletonArcher.IMGForR;
            self.dir = Const.direction_R;


    #def forStateMachine(self):
    #    #self.current_state.update();

    #    if len(self.state_queue) > 0:
    #        temp = self.current_state;
    #        self.current_state.exit();
    #        self.current_state = self.state_queue.pop();
    #        del temp;


    #def update_component(self):
        #self.previous_transform = self.transform;
        #self.collider.cx, self.collider.cy = self.transform.tx, self.transform.ty;
        #return;

    #def clampingInWindow(self):
    #    self.transform.tx = Const.clamp(0, self.transform.tx, GameObject.Cam.map_width-self.IMG.w//16)  
    #    self.transform.ty = Const.clamp(0, self.transform.ty, GameObject.Cam.map_height-self.IMG.h//8)
    #    return;

    def on_collision(self, obj):
        #print("SkeletonArcher.py {0}-{1}".format(self.tag, obj.tag));
        pass;

    def fire(self):
        SkeletonArcher.AFTER_SHOT.play(1);
        tx = self.transform.tx;
        ty = self.transform.ty;

        from FrameWork import FrameWork;
        from SkeletonArcherArrow import SkeletonArcherArrow as arrow;
        from Player import Player as player;
        px, py = player.MyPlayer.transform.tx, player.MyPlayer.transform.ty;

        radian = Const.calc_radian( self.transform.tx  
                                     , self.transform.ty 
                                     , px 
                                     , py );
        if Const.direction_L== self.dir:
            FrameWork.CurScene.add_projectile(arrow(FrameWork.CurScene, tx, ty, radian,1,1, True, 1)); 
        else :                                                                                  
            FrameWork.CurScene.add_projectile(arrow(FrameWork.CurScene, tx, ty, radian,1,1, True, 0)); 
            
        pass;

    def calc_hp(self, damage):
        if self.hit_component.can_hitted() :
            self.hit_component.hit();
            self.current_hp -= damage;
            if self.current_hp <= 0:
                SkeletonArcher.DIE_SOUND.play(1);
                self.drop_coin();
                self.current_hp = 0;
                self.state = False;

    def drop_coin(self):
        from FrameWork import FrameWork;
        from coin import Coin as coin;
        FrameWork.CurScene.AddObstacleObject(coin(self, self.transform.tx, self.transform.ty, 0,1,1,True));          

