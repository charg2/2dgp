
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

frame_time = 1;
frame = 7;
damage = 10;
extinction_time = 7;
class BelialLaser(GameObject):
    LOAD            :bool = False;
    UNIQUE_ID       :int         = 0;
    IMGSForLaserL   :List[Image] = [];
    IMGSForLaserR   :List[Image] = [];

    def __init__(self, owner, x, y, angle, sx, sy, state):
        super(BelialLaser, self).__init__(x, y, angle, sx, sy, state);
        if BelialLaser.LOAD == False:
            BelialLaser.IMGSForLaserL.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserL/IMG-6.png'));
            BelialLaser.IMGSForLaserL.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserL/IMG-5.png'));
            BelialLaser.IMGSForLaserL.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserL/IMG-4.png'));
            BelialLaser.IMGSForLaserL.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserL/IMG-3.png'));
            BelialLaser.IMGSForLaserL.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserL/IMG-2.png'));
            BelialLaser.IMGSForLaserL.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserL/IMG-1.png'));
            BelialLaser.IMGSForLaserL.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserL/IMG-0.png'));

            BelialLaser.IMGSForLaserR.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserR/IMG-6.png'));
            BelialLaser.IMGSForLaserR.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserR/IMG-5.png'));
            BelialLaser.IMGSForLaserR.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserR/IMG-4.png'));
            BelialLaser.IMGSForLaserR.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserR/IMG-3.png'));
            BelialLaser.IMGSForLaserR.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserR/IMG-2.png'));
            BelialLaser.IMGSForLaserR.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserR/IMG-1.png'));
            BelialLaser.IMGSForLaserR.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserR/IMG-0.png'));
            
            BelialLaser.LOAD = True;

        self.name = "BelialLaser_" + str(BelialLaser.UNIQUE_ID);
        self.img = BelialLaser.IMGSForLaserR[0];
        self.has_image = True;
        self.owner = None;
        self.dir = 1;# 램덤? 플레이어 방향으로 생가가소?

        BelialLaser.UNIQUE_ID += 1;
        
        self.owner = owner;
        self.animation_timer = 0.0;
        self.animation_status = 0;
        self.extinction_timer = 0.0;

        self.collider:Collision = CollisionRect(x,y, self.IMGSForLaserR[0].w//2, 5);

    def update(self, time):
        self.update_timer(time);
        self.clampingInWindow();

    def render(self):
        if 1 == self.dir:
            BelialLaser.IMGSForLaserR[self.animation_status].draw(self.transform.tx - GameObject.Cam.camera_offset_x, self.transform.ty - GameObject.Cam.camera_offset_y);    
        else :
            BelialLaser.IMGSForLaserL[self.animation_status].draw(self.transform.tx - GameObject.Cam.camera_offset_x, self.transform.ty - GameObject.Cam.camera_offset_y);    

    def render_debug(self): 
        if self.collider :
            draw_rectangle(*self.collider.get_area_offset(GameObject.Cam.camera_offset_x, GameObject.Cam.camera_offset_y));

    def on_collision(self, obj):
        if Const.TAG_PLAYER == obj.tag:
            obj.calc_hp(damage);
            self.owner.remove_projectile(self);
        # 플레이어면 체력을 깍아 버림.
    
    def update_timer(self,time):
        self.animation_timer += time;
        self.extinction_timer += time;

        if self.animation_timer > frame_time:
            self.animation_status = ( self.animation_status + 1 ) % frame;
            self.collider.multiply_area(1, 1.7);
            self.animation_timer = 0.0; 

        if self.extinction_timer > extinction_time:
            if (frame-1) == self.animation_status :
                self.owner.remove_projectile(self);

    def clampingInWindow(self):
        self.transform.tx = Const.clamp(0, self.transform.tx, GameObject.Cam.map_width-self.img.w//16)  
        self.transform.ty = Const.clamp(0, self.transform.ty, GameObject.Cam.map_height-self.img.h//8)
        return;
