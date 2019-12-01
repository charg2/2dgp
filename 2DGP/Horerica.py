

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
from MessageBox import *;

MENT = "오늘은 어떤 요리를 드시러 오셨나요? ";

class Horerica(GameObject):
    IMGS_L:Image        = [];
    IMGS_R:Image        = [];
    IMG:Image           = None;
    MESSAGE_BG:Image    = None;
    OPEN_KEY_F:Image    = None;

    def __init__(self, x, y, angle, sx, sy, state, shop):
        super(Horerica, self).__init__(x, y, angle, sx, sy, state);

        self.has_image = True;
        if Horerica.IMG == None:
            for idx in range(0, 5 + 1):
                Horerica.IMGS_R.append( pico2d.load_image('assets/NPC/Horerica/IMG-{0}.png'.format( str(idx) ) ) );
            for idx in range(6, 11 + 1):
                Horerica.IMGS_L.append( pico2d.load_image('assets/NPC/Horerica/IMG-{0}.png'.format( str(idx) ) ) );

            #Horerica.MESSAGE_BG = pico2d.load_image('assets/UI/MessageBox.png');
            Horerica.OPEN_KEY_F = pico2d.load_image('assets/NPC/F.png');

            Horerica.IMG = Horerica.IMGS_L[0];

        self.shop = shop;
        # animation
        self.dir:int = Const.direction_L; 
        self.tag:int = Const.TAG_NPC;
        self.imgs = Horerica.IMGS_L;

        self.animation_numb = 0;
        self.animation_timer = 0;

        self.name = "Horerica"; # For Debug
        self.collider:Collision = CollisionRect(x, y, Horerica.IMGS_L[0].w // 2, Horerica.IMGS_L[0].h // 2);

        # attack
        self.is_collided = False;
        self.f_key_down = False;
        self.message_box = None;
        self.shop_trigger:bool = False;
        self.is_collided:bool = False;


        # 접근시 F키를 보여줌.

        # f키가 눌렸으면 메시지 박스 
        # 아니면 걍지나감.

        # 메시지 박스 온일떄 멈춰야 함.
        # 메시지 박스가 끝나고 상점에 들갈지 아닐지 정할수 있음.

        

    def render(self): 
        self.imgs[self.animation_numb].clip_composite_draw(0,0,
                   Horerica.IMG.w,
                   Horerica.IMG.h,
                   0,'', 
                   self.transform.tx-GameObject.Cam.camera_offset_x,
                   self.transform.ty-GameObject.Cam.camera_offset_y,
                   );

        if self.message_box == None and self.is_collided :
            self.render_f_key();
        elif None != self.message_box and self.message_box.state == True : # 심층 조건이아니면 
            self.message_box.render();
            pass;
        else : #최후 상점.
            pass;
        return;

    # 신 ui에다가 집어넣고 출력 아니면 삭제.
    def render_f_key(self): 
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
        if self.is_collided == False and self.message_box != None :
            self.message_box.state = False;
            self.message_box = None;

        if False == self.is_collided :
            self.shop.close();
        if None != self.message_box and self.message_box.state == False : # 심층 조건이아니면 
            self.message_box.state = False;
            self.message_box = None;

        self.check_fkey();
        self.update_animation(time);
        self.update_dir();

        self.is_collided = False;
        if None != self.message_box : # 심층 조건이아니면 
            self.message_box.update(time);

    def update_pause(self):
        from FrameWork import FrameWork;
        if True == self.f_key_down: # pause
            FrameWork.CurScene.set_pause(True);
        else: 
            FrameWork.CurScene.set_pause(False);
        FrameWork.CurScene.game_control();


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

    def check_fkey(self):
        if None == self.message_box:
            if self.is_collided == True:
                if KeyInput.g_f:
                    self.f_key_down = True;
                    ment_list = [MENT];
                    #ment_list.append(MENT);
                    self.message_box = MessageBox(0, 0,  ment_list, lambda shop : shop.open(), self.shop);
                    #self.message_box = MessageBox(0, 0,  MENT, lambda shop : shop.open(), self.shop);
                    from FrameWork import FrameWork;
                    FrameWork.CurScene.add_ui(self.message_box);

def add_io_check_event():
    from FrameWork import FrameWork;
    FrameWork.CurScene.add_ui(self.message_box);



