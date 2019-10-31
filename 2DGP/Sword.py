from Const import *;
from GameObject import *;
from Player import *;


class Sword(GameObject):
    LOAD:bool = False;
    Imgs:list = [];

    def __init__(self, x, y, angle, sx, sy, state, owner):
        import pico2d;
        super(Sword, self).__init__(x, y, angle, sx, sy, state);
        self.owner = owner;
        print(owner.tag);
        img = pico2d.load_image("assets/Weapon/Katana.png") ;
        Sword.Imgs.append( pico2d.load_image("assets/Weapon/Katana.png") );

        LOAD = True;

    def set_onwer(self):
        pass;

    def render(self):
        if self.owner.m_dir == Const.direction_R:
            Sword.Imgs[0].rotate_draw(2, self.owner.transform.tx -10, self.owner.transform.ty - 20, 15, 80);
        if self.owner.m_dir == Const.direction_L:
            Sword.Imgs[0].rotate_draw(-2, self.owner.transform.tx +10, self.owner.transform.ty - 20, 15, 80);
        pass;

    def update(self, time):
        pass;


