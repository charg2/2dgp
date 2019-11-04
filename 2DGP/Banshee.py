
from GameObject import *;
from Graphic import *;
from math import*;
from FrameWork import *;
from KeyIO import *;
from Const import *;
from CollisionRect import*;

from IdleStateForBanshee import *;

from typing import List;

RUN_L, RUN_R, IDLE_R, IDLE_L = range(4);
class Banshee(GameObject):
    LOAD:bool = False;
    UNIQUE_ID:int = 0;
    IMGSForIdleL:List[Image] = [];
    IMGSForIdleR:List[Image] = [];

    def __init__(self, x, y, angle, sx, sy, state):
        super(Banshee, self).__init__(x, y, angle, sx, sy, state);
        self.has_image = True;
        if Banshee.LOAD == False:
            
            Banshee.IMGSForIdleR.append(pico2d.load_image('assets/Monster/Banshee/Idle/R (1).png'));
            Banshee.IMGSForIdleR.append(pico2d.load_image('assets/Monster/Banshee/Idle/R (2).png'));

            Banshee.IMGSForIdleL.append(pico2d.load_image('assets/Monster/Banshee/Idle/L (1).png'));
            Banshee.IMGSForIdleL.append(pico2d.load_image('assets/Monster/Banshee/Idle/L (2).png'));
      
            Banshee.LOAD = True;
        
        self.name = "Banshee_" + str(Banshee.UNIQUE_ID);
        Banshee.UNIQUE_ID += 1;

        self.m_dir = RUN_R;
        self.IMG = Banshee.IMGSForIdleR[0];
        self.force_x =6; 
        self.force_y =8;
        self.collider:Collision = CollisionRect(x,y, self.IMG.w // 2, self.IMG.h // 2);


        self.attack_trigger = False;
        self.attack_timer = 0;
        self.attack_key_timer:float = 0.5;

        # animation
        self.animation_numb = 0;
        self.animation_timer = 0.0;
        self.animation_state = RUN_L;

        self.attack_speed = 0.0;
        self.dir = Const.direction_L; 
        self.last_dir = RUN_L % 2;
        self.current_state = IdleStateForBanshee(self);
        self.tag = Const.TAG_MONSTER;

    def render(self): 
        self.current_state.render();
        return;

    def render_debug(self): 
        if self.collider :
            from Graphic import GraphicLib;
            GraphicLib.DebugImg1.draw(self.previous_transform.tx - GameObject.Cam.camera_offset_x, self.previous_transform.ty - GameObject.Cam.camera_offset_y);    
            #GraphicLib.DebugImg1.draw(self.transform.tx, self.transform.ty);    

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

        if(True == self.attack_trigger):
            self.attack_timer += time;
            
        if(self.attack_timer > self.attack_speed):
            self.attack_trigger = False;
            self.attack_timer = 0;
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
        print("Banshee.py {0}-{1}".format(self.tag, obj.tag));

        pass;
