
from GameObject import *;
from Const import *;
from Player import *;


offset_x, offset_y = 20, 20;
class DashBar(GameObject):
    LOAD = False;

    Template:Image;
    BG      :Image;
    Dash      :Image;

    Instance:GameObject = None;

    MyPlayer:GameObject = None;

    Font:Font = None;
    def __init__(self, owner, x, y, angle, sx, sy, state):
        super(DashBar, self).__init__(x, y, angle, sx, sy, state);
        
        if False == DashBar.LOAD :
            DashBar.Template  = pico2d.load_image("assets/UI/Template.png");
            DashBar.BG        = pico2d.load_image("assets/UI/BG.png");
            DashBar.Dash        = pico2d.load_image("assets/UI/Dash.png");

            DashBar.Instance = self;
            
            DashBar.Font = pico2d.load_font("assets/Font/font.ttf", 30);


            DashBar.LOAD =True;

            
        self.name = "DashBar";
        self.state = True;
        self.has_image = True;
        self.hp_of_one_percent_length:float = DashBar.Dash.w / 100.0;


        pass;

    def update(self, time):
        pass;

    def render(self):
        #clipdraw로 바꿔줘야함.
        
        #플레이어 체력 얻어서 
        current_hp = Player.MyPlayer.current_hp;
        max_hp = Player.MyPlayer.max_hp;

        hp_percent = (current_hp / max_hp) * 100;

        hp_width:int = int(hp_percent * self.hp_of_one_percent_length);

        hp_str = str(current_hp) + " / " + str(max_hp);
        #hp_str.format(current_hp, max_hp);

        DashBar.BG.draw_to_origin( offset_x , Const.WIN_HEIGHT - DashBar.BG.h - offset_y );
        DashBar.Dash.draw_to_origin( offset_x + 90, Const.WIN_HEIGHT - DashBar.BG.h - 10, hp_width, DashBar.Dash.h, );
        DashBar.Template.draw_to_origin( offset_x , Const.WIN_HEIGHT - DashBar.BG.h - offset_y );

        DashBar.Font.draw( 135, Const.WIN_HEIGHT - DashBar.BG.h + 8, hp_str,(255,255,255));
        pass;
        
    def get_instance():
        if None == DashBar.Instance:
            from Player import Player;
            DashBar.Instance = DashBar(Player.MyPlayer, 0,0,0,1,1,True);

        return DashBar.Instance;
