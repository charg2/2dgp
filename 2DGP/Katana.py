from Const import *;
from GameObject import *;
from Player import *;

# component
from HitComponent import *;

HIT_RECOVERY_TIME = 0.3;
class Katana(GameObject):
    LOAD:bool = False;
    Imgs:list = [];

    def __init__(self, x, y, angle, sx, sy, state, owner):
        import pico2d;
        super(Katana, self).__init__(x, y, angle, sx, sy, state);
        self.owner = owner;
        print(owner.tag);
        Katana.Imgs.append( pico2d.load_image("assets/Weapon/Katana.png") );
        self.current_img = Katana.Imgs[0];
        Katana.SOUND = load_wav('assets/Weapon/katana2.wav');
        Katana.SOUND.set_volume(50);
        LOAD = True;
        
        self.attack_trigger     :bool   = True;
        self.attack_time        :float  = 0.0;
        self.attack_key_timer   :float  = 0.3;

        self.collider = None;

    def render(self):
        if self.owner.m_dir == Const.direction_R:
            Katana.Imgs[0].composite_draw( 2, "",self.owner.transform.tx -10 - GameObject.Cam.camera_offset_x, self.owner.transform.ty - 20 - GameObject.Cam.camera_offset_y, 15, 80);
        if self.owner.m_dir == Const.direction_L:
            Katana.Imgs[0].composite_draw( -2, "", self.owner.transform.tx +10 - GameObject.Cam.camera_offset_x, self.owner.transform.ty - 20 - GameObject.Cam.camera_offset_y, 15, 80);

    def update(self, time):
        self.update_time(time);
        self.handle_io();
        self.update_component();

    def update_time(self, time):
        if False == self.attack_trigger :
            self.attack_time += time;

            if attack_timer <= self.attack_time:
                self.attack_trigger = True;
                self.attack_time = 0;

    def update_component(self, time):
        self.previous_transform = self.transform;
        self.collider.cx, self.collider.cy = self.transform.tx, self.transform.ty;


    def handle_io(self):
        if self.attack_trigger:
            if KeyInput.g_mouse_ldown :
                self.shot();
    
    def shot(self):
        print("잘르기");
        Katana.SOUND.play(1);
        pass;