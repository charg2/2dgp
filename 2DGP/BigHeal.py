


from GameObject import *;
from Graphic import *;
from math import*;
from FrameWork import *;
from Const import *;
from CollisionRect import*;

from Player import Player;

from typing import List;


heal = 25;
animation_frame = 16;
frame_time = 0.1;
class BigHeal(GameObject):
    LOAD:bool = False;
    UNIQUE_ID:int = 0;
    IMGS:List[Image] = [];
    def __init__(self, owner, x, y, angle, sx, sy, state):
        super(BigHeal, self).__init__(x, y, angle, sx, sy, state);
        self.has_image = True;
        if BigHeal.LOAD == False:
            BigHeal.IMGS.append(pico2d.load_image('assets/Monster/Heal/BigHeal/IMG-0.png'));
            BigHeal.IMGS.append(pico2d.load_image('assets/Monster/Heal/BigHeal/IMG-1.png'));
            BigHeal.IMGS.append(pico2d.load_image('assets/Monster/Heal/BigHeal/IMG-2.png'));
            BigHeal.IMGS.append(pico2d.load_image('assets/Monster/Heal/BigHeal/IMG-3.png'));
            BigHeal.IMGS.append(pico2d.load_image('assets/Monster/Heal/BigHeal/IMG-4.png'));
            BigHeal.IMGS.append(pico2d.load_image('assets/Monster/Heal/BigHeal/IMG-5.png'));
            BigHeal.IMGS.append(pico2d.load_image('assets/Monster/Heal/BigHeal/IMG-6.png'));
            BigHeal.IMGS.append(pico2d.load_image('assets/Monster/Heal/BigHeal/IMG-7.png'));
            BigHeal.IMGS.append(pico2d.load_image('assets/Monster/Heal/BigHeal/IMG-8.png'));
            BigHeal.IMGS.append(pico2d.load_image('assets/Monster/Heal/BigHeal/IMG-9.png'));
            BigHeal.IMGS.append(pico2d.load_image('assets/Monster/Heal/BigHeal/IMG-10.png'));
            BigHeal.IMGS.append(pico2d.load_image('assets/Monster/Heal/BigHeal/IMG-11.png'));
            BigHeal.IMGS.append(pico2d.load_image('assets/Monster/Heal/BigHeal/IMG-12.png'));
            BigHeal.IMGS.append(pico2d.load_image('assets/Monster/Heal/BigHeal/IMG-13.png'));
            BigHeal.IMGS.append(pico2d.load_image('assets/Monster/Heal/BigHeal/IMG-14.png'));
            BigHeal.IMGS.append(pico2d.load_image('assets/Monster/Heal/BigHeal/IMG-15.png'));
            BigHeal.LOAD = True;
        
        self.name = "BigHeal_" + str(BigHeal.UNIQUE_ID); # For Debug
        BigHeal.UNIQUE_ID += 1;

        self.IMG = BigHeal.IMGS[0];
        self.collider:Collision = CollisionRect(x,y, self.IMG.w // 1.5, self.IMG.h // 1.5);
        self.owner = owner;

        # animation
        self.animation_timer:float = 0;
        self.tag:int = Const.TAG_MONSTER;
        self.animation_status:int = 0;

    def render(self): 
        self.IMG.clip_composite_draw(0,0,
                   self.IMG.w,
                   self.IMG.h,
                   0,'', 
                   self.transform.tx-GameObject.Cam.camera_offset_x,
                   self.transform.ty-GameObject.Cam.camera_offset_y,
                   self.IMG.w * 3,
                   self.IMG.h * 3,
                   );

        self.render_debug();
        return;


    def render_debug(self): 
        if self.collider :
            draw_rectangle(*self.collider.get_area_offset(GameObject.Cam.camera_offset_x, GameObject.Cam.camera_offset_y));

        return;

    def update(self, time):
        self.update_animation(time);
        pass;

    def update_animation(self,time):
        self.animation_timer += time;
        if self.animation_timer > frame_time:
            self.animation_status = ( self.animation_status + 1 ) % animation_frame;
            self.IMG = BigHeal.IMGS[self.animation_status];
            self.animation_timer = 0.0; 
        return;

    def on_collision(self, obj):
        if Const.TAG_PLAYER == obj.tag:
            obj.current_hp += heal;
            if obj.max_hp < obj.current_hp :
                obj.current_hp = obj.max_hp;
            self.owner.remove_game_object(self);



