

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
            HPBarForBelial.BG        = pico2d.load_image("assets/Monster/Belial/UI/BG.png");
            HPBarForBelial.HP        = pico2d.load_image("assets/Monster/Belial/UI/HP.png");
        
        self.name     :str          = "HPBarForBelial";
        self.owner    :GameObject   = owner;
        self.state    :bool         = True;
        self.has_image:bool         = True;
        self.hp_of_one_percent_length:float = HPBarForBelial.HP.w / 100.0;

    def update(self, time):
        pass;

    def render(self):
        current_hp = self.owner.current_hp;
        max_hp = self.owner.max_hp;

        hp_percent  = (current_hp / max_hp) * 100;
        hp_width:int = int(hp_percent * self.hp_of_one_percent_length);

        tx = self.owner.transform.tx-GameObject.Cam.camera_offset_x;
        ty = self.owner.collider.bottom - GameObject.Cam.camera_offset_y;

        HPBarForBelial.BG.composite_draw( 0,'', tx, ty,
                                           HPBarForBelial.BG.w // 4,
                                           HPBarForBelial.BG.h // 4
                                          );

        HPBarForBelial.HP.composite_draw( 0,'', tx, ty,
                                          #HPBarForBelial.BG.w,
                                           hp_width // 4,
                                           HPBarForBelial.BG.h // 4
                                          );

