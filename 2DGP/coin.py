from GameObject import *;
from Graphic import *;
from math import*;
from FrameWork import *;
from Const import *;
from CollisionRect import*;

from Player import Player;

from typing import List;


price = 25;
animation_frame = 8;
frame_time = 0.1;

class Coin(GameObject):
    LOAD:bool = False;
    UNIQUE_ID:int = 0;
    IMGS:List[Image] = [];
    COIN_SOUND = None;
    def __init__(self, owner, x, y, angle, sx, sy, state):
        super(Coin, self).__init__(x, y, angle, sx, sy, state);
        self.has_image = True;
        if Coin.LOAD == False:
            Coin.IMGS.append(pico2d.load_image('assets/Monster/Coin/IMG-0.png'));
            Coin.IMGS.append(pico2d.load_image('assets/Monster/Coin/IMG-1.png'));
            Coin.IMGS.append(pico2d.load_image('assets/Monster/Coin/IMG-2.png'));
            Coin.IMGS.append(pico2d.load_image('assets/Monster/Coin/IMG-3.png'));
            Coin.IMGS.append(pico2d.load_image('assets/Monster/Coin/IMG-4.png'));
            Coin.IMGS.append(pico2d.load_image('assets/Monster/Coin/IMG-5.png'));
            Coin.IMGS.append(pico2d.load_image('assets/Monster/Coin/IMG-6.png'));
            Coin.IMGS.append(pico2d.load_image('assets/Monster/Coin/IMG-7.png'));

            Coin.COIN_SOUND = load_wav('assets/coin.wav');
            Coin.COIN_SOUND.set_volume(50);
            Coin.LOAD = True;
        
        self.name = "Coin_" + str(Coin.UNIQUE_ID); # For Debug
        Coin.UNIQUE_ID += 1;

        self.IMG = Coin.IMGS[0];
        self.collider:Collision = CollisionRect(x,y, self.IMG.w // 2, self.IMG.h // 2);
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
                   self.IMG.w,
                   self.IMG.h,
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

    def update_component(self):
        pass;

    def Physx(self, time):
        pass;

    def update_animation(self,time):
        self.animation_timer += time;
        if self.animation_timer > frame_time:
            self.animation_status = ( self.animation_status + 1 ) % animation_frame;
            self.IMG = Coin.IMGS[self.animation_status];
            self.animation_timer = 0.0; 
        return;

    def on_collision(self, obj):
        if Const.TAG_PLAYER == obj.tag:
            Coin.COIN_SOUND.play(1);

            obj.current_coin += price;
            self.state = False;
        return;