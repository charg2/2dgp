from GameObject import *;
from Graphic import *;
from math import*;
from FrameWork import *;
from KeyIO import *;
from Const import *;
from CollisionRect import*;

from Player import Player;
from typing import List;

frame_time = 0.2;
frame = 4;
extinction_time = 2;

class SkeletonArcherArrow(GameObject):
    LOAD:bool = False;
    UNIQUE_ID:int = 0;
    IMG:Image = None;


    def __init__(self, owner, x, y, angle, sx, sy, state):
        super(SkeletonArcherArrow, self).__init__(x, y, angle, sx, sy, state);
        if SkeletonArcherArrow.LOAD == False:
            SkeletonArcherArrow.IMG =pico2d.load_image('assets/Monster/SkeletonArcher/Arrow/Arrow.png');

            SkeletonArcherArrow.LOAD = True;

        self.name = "SkeletonArcherArrow_" + str(SkeletonArcherArrow.UNIQUE_ID);

        self.has_image = True;
        self.owner = None;

        SkeletonArcherArrow.UNIQUE_ID += 1;
        
        self.velocity = 7; 
        self.owner = owner;
        self.animation_timer = 0.0;
        self.animation_status = 0;
        self.extinction_timer = 0.0;
        
        self.collider:Collision = CollisionRect(x,y, self.IMG.w // 2, self.IMG.h // 2);

        pass;

    def update(self, time):
        self.update_component();
        self.clampingInWindow();
        self.Physx_bullet();
        pass;

    def update_component(self):
        self.previous_transform = self.transform;
        self.collider.cx, self.collider.cy = self.transform.tx, self.transform.ty;

    def Physx_bullet(self):
        radian = self.transform.angle * math.pi;
        
        self.physx.velocity_x = self.velocity * math.cos(radian);
        self.physx.velocity_y = self.velocity * math.sin(radian);
        
        self.transform.angle += self.physx.angle_rate;
        
        self.transform.set_position(self.physx.velocity_x, self.physx.velocity_y);


    def render(self):
        if self.transform.angle == 1:
            SkeletonArcherArrow.IMG.composite_draw(0, "h",self.transform.tx - GameObject.Cam.camera_offset_x, self.transform.ty - GameObject.Cam.camera_offset_y);    
        else :
            SkeletonArcherArrow.IMG.draw(self.transform.tx - GameObject.Cam.camera_offset_x, self.transform.ty - GameObject.Cam.camera_offset_y);    

    def render_debug(self):
        draw_rectangle(*self.collider.get_area_offset(GameObject.Cam.camera_offset_x, GameObject.Cam.camera_offset_y));
        #if self.collider :
            #from Graphic import GraphicLib;
            #GraphicLib.DebugImg1.draw(self.previous_transform.tx - GameObject.Cam.camera_offset_x, self.previous_transform.ty - GameObject.Cam.camera_offset_y, SkeletonArcherArrow.IMG.w, SkeletonArcherArrow.IMG.h );    
            #GraphicLib.DebugImg1.draw(self.transform.tx, self.transform.ty);    

        return;
    def on_collision(self, obj):
        if "Mouse" == obj.name:
            pass;
           
        elif "Hero" == obj.name:
            obj.current_hp -= 5;
            self.owner.remove_projectile(self);
            #맵에서 나가도 ㅇㅇ;
        # 벽이면 사라짐.
        #print("{0} - 충돌함 ({1},{2})".format(self.name,self.transform.tx, self.transform.ty));
        # 플레이어면 체력을 깍아 버림.

        #일단 충돌하면 없어지는건 뺴박 캔트.
        

        pass;
    

    #def update_timer(self,time):
    #    self.animation_timer += time;

    #    if self.animation_timer > frame_time:
    #        self.animation_status = ( self.animation_status + 1 ) % frame;
    #        self.animation_timer = 0.0; 


    def clampingInWindow(self):
        self.transform.tx = Const.clamp(0, self.transform.tx, GameObject.Cam.map_width-self.IMG.w//16)  
        self.transform.ty = Const.clamp(0, self.transform.ty, GameObject.Cam.map_height-self.IMG.h//8)
        return;

    def update_timer(self,time):
        self.extinction_timer += time;
        
        # 시간 지나면 사라짐.
        if self.extinction_timer > extinction_time:
            self.owner.remove_projectile(self);