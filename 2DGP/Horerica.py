

from GameObject import *;
from Graphic import *;
from math import*;
from FrameWork import *;
from KeyIO import *;
from Const import *;
from CollisionRect import*;

from Player import Player;
#from IdleStateForHorerica import *; # 미 적용.

from typing import List;

class Horerica(GameObject):
    IMGS_L:Image = [];
    IMGS_R:Image = [];
    IMG:Image = None;
    MESSAGE_BG:Image = None;
    OPEN_KEY_F:Image = None;

    def __init__(self, x, y, angle, sx, sy, state):
        super(Horerica, self).__init__(x, y, angle, sx, sy, state);

        self.has_image = True;
        if Horerica.IMG == None:
            for idx in range(0, 5 + 1):
                Horerica.IMGS_R.append( pico2d.load_image('assets/NPC/Horerica/IMG-{0}.png'.format( str(idx) ) ) );
            for idx in range(6, 11 + 1):
                Horerica.IMGS_L.append( pico2d.load_image('assets/NPC/Horerica/IMG-{0}.png'.format( str(idx) ) ) );

            Horerica.MESSAGE_BG = pico2d.load_image('assets/UI/MessageBox.png');
            Horerica.OPEN_KEY_F = pico2d.load_image('assets/NPC/F.png');

            Horerica.IMG = Horerica.IMGS_L[0];

        self.animation_numb = 0;
        self.animation_timer = 0;
        self.is_collided = False;
        self.name = "Horerica"; # For Debug
        self.collider:Collision = CollisionRect(x, y, Horerica.IMGS_L[0].w // 2, Horerica.IMGS_L[0].h // 2);

        # attack
        self.shop_trigger:bool = False;
        self.is_collided:bool = False;

        # animation
        self.dir:int = Const.direction_L; 
        self.tag:int = Const.TAG_NPC;
        self.imgs = Horerica.IMGS_L;

    def render(self): 
        self.imgs[self.animation_numb].clip_composite_draw(0,0,
                   Horerica.IMG.w,
                   Horerica.IMG.h,
                   0,'', 
                   self.transform.tx-GameObject.Cam.camera_offset_x,
                   self.transform.ty-GameObject.Cam.camera_offset_y,
                   );

        self.render_debug();
        self.render_f_key();
        return;

    # 신 ui에다가 집어넣고 출력 아니면 삭제.
    def render_f_key(self): 
        if self.is_collided :
            Horerica.MESSAGE_BG.draw_to_origin(0,0,
                    #Horerica.MESSAGE_BG.w,
                    Const.WIN_WIDTH,
                    180,
                    #self.transform.tx-GameObject.Cam.camera_offset_x,
                    );

            Horerica.OPEN_KEY_F.clip_composite_draw(0,0,
                    Horerica.OPEN_KEY_F.w,
                    Horerica.OPEN_KEY_F.h,
                    0,'',
                    self.transform.tx-GameObject.Cam.camera_offset_x,
                    self.transform.ty-GameObject.Cam.camera_offset_y + 100 ,
                    );


    def render_debug(self): 
        if self.collider :
            draw_rectangle(*self.collider.get_area_offset(GameObject.Cam.camera_offset_x, GameObject.Cam.camera_offset_y));
        return;

    def update(self, time):
        self.update_animation(time);
        self.update_dir();
        self.is_collided = False;


    def update_dir(self):
        if ( self.transform.tx - Player.MyPlayer.transform.tx ) > 0 : # 내 오른쪽에 플레이어가;;
            self.imgs = Horerica.IMGS_L;
            self.dir = Const.direction_L;
        else:
            self.imgs = Horerica.IMGS_R;
            self.dir = Const.direction_R;


    def update_animation(self,time):
        self.animation_timer += time;

        if(self.animation_timer >0.1):
            self.animation_numb = ( self.animation_numb+1 ) % 6;
            self.animation_timer = 0;

        return;
    

    def on_collision(self, obj):
        if Const.TAG_PLAYER == obj.tag:
            self.is_collided = True;
            self.render_f_key();

            #from FrameWork import FrameWork;
            #FrameWork.CurScene.set_pause(True);
            #FrameWork.CurScene.game_control();
