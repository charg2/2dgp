

from GameObject import *;
from Const import *;
from Belial import *;

offset_x, offset_y = 20, 20;
class HPBarForBelial(GameObject):
    BG:Image  = None;
    HP:Image  = None;

    def __init__(self, owner, x, y, angle, sx, sy, state):
        super(HPBarForBelial, self).__init__(x, y, angle, sx, sy, state);
        
        if None == HPBarForBelial.BG :
            HPBarForBelial.BG = pico2d.load_image("assets/Monster/Belial/UI/BG2.png");
            HPBarForBelial.HP = pico2d.load_image("assets/Monster/Belial/UI/HP3.png");
        
        self.name     :str         = "HPBarForBelial";
        self.owner    :GameObject  = owner;
        self.state    :bool        = True;
        self.has_image:bool        = True;
        self.hp_of_one_percent_length = HPBarForBelial.HP.w / 100.0;

    def update(self, time):
        pass;

    def render(self):
        current_hp  = self.owner.current_hp;
        max_hp      = self.owner.max_hp;

        hp_percent      = (current_hp / max_hp) * 100;
        hp_width:int    = int(hp_percent * self.hp_of_one_percent_length);

        HPBarForBelial.BG.draw_to_origin( 0, 0, HPBarForBelial.BG.w, HPBarForBelial.BG.h);
        HPBarForBelial.HP.draw_to_origin( 224, 0, hp_width, HPBarForBelial.HP.h );

