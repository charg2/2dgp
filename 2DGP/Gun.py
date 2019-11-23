from Const import *;
from GameObject import *;
from Player import *;
from KeyIO import *;

from PlayerBullet import PlayerBullet as pbullet;

attack_timer = 0.4;

class Gun(GameObject):
    LOAD:bool = False;
    IMGS:list = [];

    def __init__(self, x, y, angle, sx, sy, state, owner):
        import pico2d;
        super(Gun, self).__init__(x, y, angle, sx, sy, state);
        self.owner = owner;
        print(owner.tag);
        Gun.IMGS.append( pico2d.load_image("assets/Weapon/UZI.png") );
        self.current_img = Gun.IMGS[0];
        Gun.SOUND = load_wav('assets/Weapon/gun.wav');
        Gun.SOUND.set_volume(50);

        LOAD = True;
        self.attack_trigger     :bool   = True;
        self.attack_time        :float  = 0.0;
        self.attack_key_timer   :float  = 0.3;

        self.radian = 0;

    def render(self):
        dir = '';
        if self.owner.m_dir == Const.direction_L:
            dir = "v";

        #self.current_img.composite_draw( 2, dir,self.owner.transform.tx -10 - GameObject.Cam.camera_offset_x, self.owner.transform.ty - 20 - GameObject.Cam.camera_offset_y, self.current_img.w, self.current_img.h);
        self.current_img.rotate_draw( -self.radian ,self.owner.transform.tx - GameObject.Cam.camera_offset_x, self.owner.transform.ty - 20 - GameObject.Cam.camera_offset_y, self.current_img.w, self.current_img.h);

    def update(self, time):
        #self.transform.angle;
        # mouse의 좌표를 얻어서 방향으로 angle을 갱신.
        
        self.update_time(time);
        self.handle_io();
        self.update_component();

    def handle_io(self):
        if self.attack_trigger:
            if KeyInput.g_mouse_ldown :
                self.shot();
        pass;

    def update_time(self, time):

        if False == self.attack_trigger :
            self.attack_time += time;

            if attack_timer <= self.attack_time:
                self.attack_trigger = True;
                self.attack_time = 0;

    def shot(self):
        #target_x = KeyInput.g_mouse_x;
        #target_y = Const.WIN_HEIGHT - KeyInput.g_mouse_y - 1;

        #radian = ( Const.calc_radian(self.owner.transform.tx - GameObject.Cam.camera_offset_x, self.owner.transform.ty - GameObject.Cam.camera_offset_y, target_x, target_y) );
        Gun.SOUND.play(1);

        tx = self.owner.transform.tx;
        ty = self.owner.transform.ty;

        from FrameWork import FrameWork;
        if Const.direction_L == self.owner.m_dir:
            FrameWork.CurScene.add_player_weapon(pbullet(FrameWork.CurScene, tx, ty, self.radian,1,1, True)); 
        else :
            FrameWork.CurScene.add_player_weapon(pbullet(FrameWork.CurScene, tx, ty, self.radian,1,1, True)); 
        
        self.attack_trigger = False;


    def update_component(self):
        #target_x = KeyInput.g_mouse_x;
        target_y = Const.WIN_HEIGHT - KeyInput.g_mouse_y - 1;
        self.radian = ( Const.calc_radian(self.owner.transform.tx - GameObject.Cam.camera_offset_x, self.owner.transform.ty - GameObject.Cam.camera_offset_y, KeyInput.g_mouse_x, target_y) );



