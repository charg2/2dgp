from GameObject import *;
from Graphic import *;
from math import*;
from FrameWork import *;
from KeyIO import *;
from Const import *;
from CollisionRect import*;

from Gun import *;
from Player import *;

from typing import List;

frame_time = 0.2;
frame = 6;
damage = 5;
animation_timer = 0.25;
class PlayerBullet(GameObject):
    LOAD:bool = False;
    UNIQUE_ID:int = 0;
    IMGS:List[Image] = [];

    def __init__(self, owner, x, y, angle, sx, sy, state):
        super(PlayerBullet, self).__init__(x, y, angle, sx, sy, state);
        if PlayerBullet.LOAD == False:
            #PlayerBullet.IMGS.append(pico2d.load_image('assets/Monster/Banshee/Bullet/banshee_bullet (1).png'));
            #PlayerBullet.IMGS.append(pico2d.load_image('assets/Monster/Banshee/Bullet/banshee_bullet (2).png'));
            #PlayerBullet.IMGS.append(pico2d.load_image('assets/Monster/Banshee/Bullet/banshee_bullet (3).png'));
            #PlayerBullet.IMGS.append(pico2d.load_image('assets/Monster/Banshee/Bullet/banshee_bullet (4).png'));
            
            PlayerBullet.IMGS.append(pico2d.load_image('assets/Weapon/Bullet/Bullet02.png'));
            PlayerBullet.IMGS.append(pico2d.load_image('assets/Weapon/Bullet/Bullet03.png'));
            PlayerBullet.IMGS.append(pico2d.load_image('assets/Weapon/Bullet/Bullet07.png'));
            PlayerBullet.IMGS.append(pico2d.load_image('assets/Weapon/Bullet/Bullet08.png'));
            PlayerBullet.IMGS.append(pico2d.load_image('assets/Weapon/Bullet/Bullet09.png'));
            PlayerBullet.IMGS.append(pico2d.load_image('assets/Weapon/Bullet/Bullet10.png'));

            PlayerBullet.LOAD = True;

        self.name = "PlayerBullet_" + str(PlayerBullet.UNIQUE_ID);

        self.has_image = True;
        self.owner = None;
        self.img = PlayerBullet.IMGS[0];
        PlayerBullet.UNIQUE_ID += 1;
        
        self.velocity = 850; 
        self.owner = owner;
        self.animation_time = 0.0;
        self.animation_status = 0;
        
        self.collider:Collision = CollisionRect(x,y, self.IMGS[0].w // 2, self.IMGS[0].h // 3);

        pass;

    def update(self, time):
        self.update_component();
        self.update_timer(time);
        self.clampingInWindow();
        self.Physx_bullet(time);
        pass;

    def update_component(self):
        self.previous_transform = self.transform;
        self.collider.cx, self.collider.cy = self.transform.tx, self.transform.ty;

    def Physx_bullet(self, time):
        radian = self.transform.angle; # * math.pi;
        
        self.physx.velocity_x = self.velocity * math.sin(radian) * time;
        self.physx.velocity_y = self.velocity * math.cos(radian) * time;
        
        self.transform.angle += self.physx.angle_rate;
        
        self.transform.set_position(self.physx.velocity_x, self.physx.velocity_y);

    def render(self):
        #PlayerBullet.IMGS[self.animation_status].draw(self.transform.tx - GameObject.Cam.camera_offset_x, self.transform.ty - GameObject.Cam.camera_offset_y);    
        PlayerBullet.IMGS[self.animation_status].rotate_draw(-self.transform.angle,self.transform.tx - GameObject.Cam.camera_offset_x, self.transform.ty - GameObject.Cam.camera_offset_y, self.img.w * 1.5, self.img.h * 1.5);    
        pass;

    def render_debug(self): 
        if self.collider :
            draw_rectangle(*self.collider.get_area_offset(GameObject.Cam.camera_offset_x, GameObject.Cam.camera_offset_y));
        return;



    def on_collision(self, obj):
        if Const.TAG_MONSTER == obj.tag:
            obj.calc_hp(damage);
            self.state = False;
        if Const.TAG_TERRAIN == obj.tag:
            self.state = False;

        #    self.owner.remove_projectile(self);
        #맵에서 나가도 ㅇㅇ;
        # 벽이면 사라짐.
        #print("{0} - 충돌함 ({1},{2})".format(self.name,self.transform.tx, self.transform.ty));
        # 플레이어면 체력을 깍아 버림.


    

    def update_timer(self,time):
        if frame-1 != self.animation_status:
            self.animation_time += time;

            if animation_timer < self.animation_time:
                self.animation_status = ( self.animation_status + 1 ) % frame;
                self.img = PlayerBullet.IMGS[self.animation_status];
                self.animation_time = 0.0; 

    def clampingInWindow(self):
        self.transform.tx = Const.clamp(0, self.transform.tx, GameObject.Cam.map_width-self.IMGS[0].w//16)  
        self.transform.ty = Const.clamp(0, self.transform.ty, GameObject.Cam.map_height-self.IMGS[0].h//8)
        return;