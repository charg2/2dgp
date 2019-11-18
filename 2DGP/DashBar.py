
from GameObject import *;
from Const import *;
from Player import *;

from typing import List;

offset_x, offset_y = 20, 20;
class DashBar(GameObject):
    LOAD        :bool           = False;

    Bars        :List[Image]    = []; 
    BG          :Image          = None;
    DashGage    :Image          = None;

    Instance    :GameObject     = None;
    MyPlayer    :GameObject     = None;

    def __init__(self, owner, x, y, angle, sx, sy, state):
        super(DashBar, self).__init__(x, y, angle, sx, sy, state);
        
        if False == DashBar.LOAD :
            DashBar.Bars.append(pico2d.load_image("assets/UI/DashBar (1).png"));
            DashBar.Bars.append(pico2d.load_image("assets/UI/DashBar (2).png"));
            DashBar.Bars.append(pico2d.load_image("assets/UI/DashBar (3).png"));
            DashBar.Bars.append(pico2d.load_image("assets/UI/DashBar (4).png"));
            DashBar.Bars.append(pico2d.load_image("assets/UI/DashBar (5).png"));

            DashBar.DashGage      = pico2d.load_image("assets/UI/DashGage.png");

            DashBar.Instance = self;
            
            DashBar.LOAD =True;

        self.img = DashBar.Bars[0];    
        self.name = "DashBar";
        self.state = True;
        self.has_image = True;

    def update(self, time):
        pass;

    def render(self):
        current_dash_gage = Player.MyPlayer.dash_count;
        max_dash_gage = Player.MyPlayer.max_dash_count - 2;

        DashBar.Bars[max_dash_gage].draw_to_origin( 20 , Const.WIN_HEIGHT - 150);
        
        for i in range(current_dash_gage):
            DashBar.DashGage.draw_to_origin( 30 + 60 * i, Const.WIN_HEIGHT - 125, DashBar.DashGage.w, DashBar.DashGage.h);

    def get_instance():
        if None == DashBar.Instance:
            from Player import Player;
            DashBar.Instance = DashBar(Player.MyPlayer, 0,0,0,1,1,True);

        return DashBar.Instance;
