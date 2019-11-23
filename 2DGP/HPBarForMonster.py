
from GameObject import *;
from Const import *;

offset_x, offset_y = 20, 20;
class HPBarForMonster(GameObject):
    BG:Image  = None;
    HP:Image  = None;

    def __init__(self, owner, x, y, angle, sx, sy, state):
        super(HPBarForMonster, self).__init__(x, y, angle, sx, sy, state);
        
        if None == HPBarForMonster.BG :
            HPBarForMonster.BG        = pico2d.load_image("assets/UI/MonsterHPBar/BG.png");
            HPBarForMonster.HP        = pico2d.load_image("assets/UI/MonsterHPBar/HP.png");
        
        self.name     :str          = "HPBarForMonster";
        self.owner    :GameObject   = owner;
        self.state    :bool         = True;
        self.has_image:bool         = True;
        self.hp_of_one_percent_length:float = HPBarForMonster.HP.w / 100.0;

    def update(self, time):
        # 여기서 업데이트하는게 맞는데 굳이 매번 업뎃 할필요 있나;
        pass;

    def render(self):
        current_hp = self.owner.current_hp;
        max_hp = self.owner.max_hp;

        hp_percent  = (current_hp / max_hp) * 100;
        hp_width:int = int(hp_percent * self.hp_of_one_percent_length);

        tx = self.owner.transform.tx-GameObject.Cam.camera_offset_x;
        ty = self.owner.collider.bottom - GameObject.Cam.camera_offset_y;

        HPBarForMonster.BG.composite_draw( 0,'', tx, ty,
                                           HPBarForMonster.BG.w // 4,
                                           HPBarForMonster.BG.h // 4
                                          );

        HPBarForMonster.HP.composite_draw( 0,'', tx, ty,
                                          #HPBarForMonster.BG.w,
                                           hp_width // 4,
                                           HPBarForMonster.BG.h // 4
                                          );

