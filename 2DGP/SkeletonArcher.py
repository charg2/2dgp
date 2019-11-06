
from GameObject import *;
from Graphic import *;
from math import*;
from FrameWork import *;
from KeyIO import *;
from Const import *;
from CollisionRect import*;

from Player import Player;
#from IdleStateForSkeletonArcher import *; # 미 적용.

from typing import List;

attack_speed = 2;
IDLE_L, IDLE_R = range(2);
class SkeletonArcher(GameObject):
    LOAD:bool = False;
    UNIQUE_ID:int = 0;
    IMGForL:Image = None;
    IMGForR:Image = None;
    IMGSForBullet:List[Image] = [];
    FieldOfView:float = 0.0;

    def __init__(self, x, y, angle, sx, sy, state):
        super(SkeletonArcher, self).__init__(x, y, angle, sx, sy, state);
        self.has_image = True;
        if SkeletonArcher.LOAD == False:
            
            SkeletonArcher.IMGForL = pico2d.load_image('assets/Monster/SkeletonArcher/Idle/L.png');
            SkeletonArcher.IMGForR = pico2d.load_image('assets/Monster/SkeletonArcher/Idle/R.png');
        
            # bullet
            SkeletonArcher.IMGSForBullet.append(pico2d.load_image('assets/Monster/SkeletonArcher/Arrow/Arrow.png'));
            
            SkeletonArcher.FieldOfView = Const.BANSHEE_FIELD_OF_VIEW;

            SkeletonArcher.LOAD = True;
        
        self.name = "SkeletonArcher_" + str(SkeletonArcher.UNIQUE_ID); # For Debug
        SkeletonArcher.UNIQUE_ID += 1;

        self.IMG = SkeletonArcher.IMGForL;
        self.collider:Collision = CollisionRect(x,y, self.IMG.w // 2, self.IMG.h // 2);

        # attack
        self.attack_trigger:bool = False;
        self.attack_timer:float = 0;
        self.attack_key_timer:float = 0.5;

        # animation
        self.attack_speed:float = 10.0;
        self.dir:int = Const.direction_L; 
        self.tag:int = Const.TAG_MONSTER;

    def render(self): 
        self.IMG.clip_composite_draw(0,0,
                   self.IMG.w,
                   self.IMG.h,
                   0,'', 
                   self.transform.tx-GameObject.Cam.camera_offset_x,
                   self.transform.ty-GameObject.Cam.camera_offset_y,
                   );

        self.render_debug();
        return;

    def render_debug(self): 
        if self.collider :
            from Graphic import GraphicLib;
            GraphicLib.DebugImg1.draw(self.previous_transform.tx - GameObject.Cam.camera_offset_x, self.previous_transform.ty - GameObject.Cam.camera_offset_y);    
            #GraphicLib.DebugImg1.draw(self.transform.tx, self.transform.ty);    

        return;

    def update(self, time):
        # 플레이어와의 거리 체크 해서 어느 근처 거리면 다가가기 시작.
        #self.update_component();
        #self.forStateMachine();
        self.update_timer(time);
        self.update_dir();
        #self.clampingInWindow();
        pass;

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


        if True == self.attack_trigger :
            self.attack_timer += time;
            if(self.attack_timer > attack_speed):
                self.fire();
                self.attack_timer = 0;
        
    
        return;
    
    def update_dir(self):
        if ( self.transform.tx - Player.MyPlayer.transform.tx ) > 0 : # 내 오른쪽에 플레이어가;;
            self.IMG = SkeletonArcher.IMGForL;
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
        tx = self.transform.tx;
        ty = self.transform.ty;

        #self.bullets.append(BansheeBullet(self, tx, ty, 0,1,1, True)); 
        #self.bullets.append(BansheeBullet(self, tx, ty, 0.25,1,1, True)); 
        #self.bullets.append(BansheeBullet(self, tx, ty, 0.5,1,1, True)); 
        #self.bullets.append(BansheeBullet(self, tx, ty, 0.75,1,1, True)); 
        #self.bullets.append(BansheeBullet(self, tx, ty, 1,1,1, True)); 
        #self.bullets.append(BansheeBullet(self, tx, ty, -0.25,1,1, True)); 
        #self.bullets.append(BansheeBullet(self, tx, ty, -0.5,1,1, True)); 
        #self.bullets.append(BansheeBullet(self, tx, ty, -0.75,1,1, True)); 
        from FrameWork import FrameWork;
        from SkeletonArcherArrow import SkeletonArcherArrow as arrow;

        
        if Const.direction_L== self.dir:
            FrameWork.CurScene.add_projectile(arrow(FrameWork.CurScene, tx, ty, 1,1,1, True)); 
        else :
            FrameWork.CurScene.add_projectile(arrow(FrameWork.CurScene, tx, ty, 0,1,1, True)); 
            
        pass;

