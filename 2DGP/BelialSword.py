
from GameObject import *;
from Graphic import *;
from math import*;
from FrameWork import *;
from KeyIO import *;
from Const import *;
from CollisionRect import*;

from Player import Player;
#from IdleStateForBelial import *;

from typing import List;

frame_time = 0.2;
frame = 10;
damage = 10;
count = 6;

class BelialSword(GameObject):
    LOAD:bool = False;
    UNIQUE_ID:int = 0;
    IMG:Image = None;

    def __init__(self, owner, x, y, angle, sx, sy, state):
        super(BelialSword, self).__init__(x, y, angle, sx, sy, state);
        if BelialSword.LOAD == False:
            BelialSword.IMG = pico2d.load_image('assets/Monster/Belial/Sword/IMG-0.png');
    
            BelialSword.LOAD = True;

        self.name = "BelialSword_" + str(BelialSword.UNIQUE_ID);

        self.has_image = True;
        self.owner = None;

        BelialSword.UNIQUE_ID += 1;
        
        self.velocity = 10; 
        self.owner = owner;
        self.animation_timer = 0.0;
        self.animation_status = 0;
        self.extinction_timer = 0.0;

        self.collider:Collision = CollisionRect(x,y, self.IMG.w // 2, self.IMG.h // 2);
        self.count = 0;
        self.offset_x = 0;
        pass;

    def update(self, time):
        self.update_component();
        self.clampingInWindow();
        self.Physx();
        pass;

    def update_component(self):
        self.previous_transform = self.transform;
        self.collider.cx, self.collider.cy = self.transform.tx, self.transform.ty;

    def Physx(self):
        radian = self.transform.angle * math.pi;
        
        self.physx.velocity_x = self.velocity * math.cos(radian);
        self.physx.velocity_y = self.velocity * math.sin(radian);
        
        self.transform.set_position(self.physx.velocity_x, self.physx.velocity_y);

    def render(self):
        BelialSword.IMG.draw(self.transform.tx - GameObject.Cam.camera_offset_x, self.transform.ty - GameObject.Cam.camera_offset_y);    
        pass;

    def render_debug(self): 
        if self.collider :
            from Graphic import GraphicLib;
            GraphicLib.DebugImg1.draw(self.previous_transform.tx - GameObject.Cam.camera_offset_x, self.previous_transform.ty - GameObject.Cam.camera_offset_y);    
            #GraphicLib.DebugImg1.draw(self.transform.tx, self.transform.ty);    

        return;
    def on_collision(self, obj):
        if "Mouse" == obj.name:
            pass;
           
        elif "Hero" == obj.name:
            obj.current_hp -= damage;
            self.owner.remove_projectile(self);
            #맵에서 나가도 ㅇㅇ;
        # 벽이면 사라짐.
        #print("{0} - 충돌함 ({1},{2})".format(self.name,self.transform.tx, self.transform.ty));
        # 플레이어면 체력을 깍아 버림.

        #일단 충돌하면 없어지는건 뺴박 캔트.
        

        pass;
    



    def clampingInWindow(self):
        self.transform.tx = Const.clamp(0, self.transform.tx, GameObject.Cam.map_width-self.IMG.w//16)  
        self.transform.ty = Const.clamp(0, self.transform.ty, GameObject.Cam.map_height-self.IMG.h//8)
        return;
