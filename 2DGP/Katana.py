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
        LOAD = True;
        self.hit_component = HitComponent(HIT_RECOVERY_TIME);

    def render(self):
        if self.owner.m_dir == Const.direction_R:
            Katana.Imgs[0].composite_draw( 2, "",self.owner.transform.tx -10 - GameObject.Cam.camera_offset_x, self.owner.transform.ty - 20 - GameObject.Cam.camera_offset_y, 15, 80);
        if self.owner.m_dir == Const.direction_L:
            Katana.Imgs[0].composite_draw( -2, "", self.owner.transform.tx +10 - GameObject.Cam.camera_offset_x, self.owner.transform.ty - 20 - GameObject.Cam.camera_offset_y, 15, 80);

    def update(self, time):
        update_component(time);

    def update_component(self, time):
        self.previous_transform = self.transform;
        self.collider.cx, self.collider.cy = self.transform.tx, self.transform.ty;
        self.hit_component.update(time);

    def handle_io(self):
        pass;

