from Const import *;
from GameObject import *;
from Player import *;


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

        LOAD = True;

    def set_onwer(self):
        pass;

    def render(self):
        if self.owner.m_dir == Const.direction_R:
            Katana.Imgs[0].composite_draw( 2, "",self.owner.transform.tx -10 - GameObject.Cam.camera_offset_x, self.owner.transform.ty - 20 - GameObject.Cam.camera_offset_y, 15, 80);
        if self.owner.m_dir == Const.direction_L:
            Katana.Imgs[0].composite_draw( -2, "", self.owner.transform.tx +10 - GameObject.Cam.camera_offset_x, self.owner.transform.ty - 20 - GameObject.Cam.camera_offset_y, 15, 80);
        pass;

    def update(self, time):
        #self.transform.angle;
        pass;


