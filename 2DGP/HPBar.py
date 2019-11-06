from GameObject import *;
from Const import *;
from Player import *;


offset_x, offset_y = 20, 20;
class HPBar(GameObject):
    LOAD = False;

    Template:Image;
    BG      :Image;
    HP      :Image;

    Instance:GameObject = None;

    MyPlayer:GameObject = None;

    Font:Font = None;
    def __init__(self, owner, x, y, angle, sx, sy, state):
        super(HPBar, self).__init__(x, y, angle, sx, sy, state);
        
        if False == HPBar.LOAD :
            HPBar.Template  = pico2d.load_image("assets/UI/Template.png");
            HPBar.BG        = pico2d.load_image("assets/UI/BG.png");
            HPBar.HP        = pico2d.load_image("assets/UI/HP.png");

            HPBar.Instance = self;
            
            HPBar.Font = pico2d.load_font("assets/Font/font.ttf", 30);


            HPBar.LOAD =True;

            
        self.name = "HPBar";
        self.state = True;
        self.has_image = True;
        self.hp_of_one_percent_length:float = HPBar.HP.w / 100.0;


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

        HPBar.BG.draw_to_origin( offset_x , Const.WIN_HEIGHT - HPBar.BG.h - offset_y );
        HPBar.HP.draw_to_origin( offset_x + 90, Const.WIN_HEIGHT - HPBar.BG.h - 10, hp_width, HPBar.HP.h, );
        HPBar.Template.draw_to_origin( offset_x , Const.WIN_HEIGHT - HPBar.BG.h - offset_y );

        HPBar.Font.draw( 135, Const.WIN_HEIGHT - HPBar.BG.h + 8, hp_str,(255,255,255));
        pass;
        
    def get_instance():
        if None == HPBar.Instance:
            from Player import Player;
            HPBar.Instance = HPBar(Player.MyPlayer, 0,0,0,1,1,True);

        return HPBar.Instance;
