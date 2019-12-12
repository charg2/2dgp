from Scene import Scene;
from RoomBG import RoomBG;
from Const import Const as const;
from Mouse import Mouse;
from Player import Player;

from Belial import *;

from Terrain import Terrain as terrain;
from Portal import Portal as portal;

#UI
from HPBar import *;
from Wallet import *;
from DashBar import *;

START_X,START_Y = 300, 120;

class BossRoomScene(Scene):
    BGM = None;
    CLEAR_IMG = None;
    def __init__(self):       
        super(BossRoomScene,self).__init__();
        self.bg = (RoomBG(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True, "room_boss.map"));
        if None == BossRoomScene.BGM :
            #BossRoomScene.CLEAR_IMG = pico2d.load_image('assets/UI/end2.png');
            BossRoomScene.CLEAR_IMG     = pico2d.load_image('assets/UI/complete2.png');
            BossRoomScene.BGM           = load_wav('assets/Sound/boss.wav');
            BossRoomScene.Font          = pico2d.load_font('assets/Font/font.TTF', 50);

            BossRoomScene.BGM.set_volume(50);

        self.add_terrain(self.bg);
        self.add_ally_object(Player.MyPlayer);          

        self.add_monster(Belial(START_X + 800, START_Y + 690 ,0,1,1,True));          
        #self.AddObstacleObject(portal(START_X + 800, START_Y,0,1,1,True,0));
        # 바닥
        self.add_terrain(terrain(self.bg.map.width //2, 90, self.bg.map.width //2, 90 ));
        #TOP
        self.add_terrain(terrain(self.bg.map.width //2, 1980, self.bg.map.width //2, 90, Const.TOP ));
        # LEFT 벽
        self.add_terrain(terrain(90, self.bg.map.height // 2, 90,  self.bg.map.height // 2, Const.LEFT));
        #RIGHT
        self.add_terrain(terrain(self.bg.map.width - 90, self.bg.map.height // 2, 90,  self.bg.map.height // 2, Const.RIGHT));



        
        self.add_terrain(terrain(90 * 3, 90*9, 90 ,  0));
        self.add_terrain(terrain(90 * 24, 90*9, 90 ,  0));



        from BelialLaser import BelialLaser as bl;
        self.add_monster(bl(self, START_X + 1000, START_Y + 400 ,0,1,1, True));        

        from Event import ConditionEvent;
        self.add_ally_object(ConditionEvent( monster_empty, run_game_clear_event, self, self, 1));        

        mouse:Mouse = Mouse();
        mouse.set_cursor(Const.CURSOR_TARGET);

        self.add_ui(HPBarForPlayer.get_instance());
        self.add_ui(Wallet.get_instance());
        self.add_ui(DashBar.get_instance());
        
        self.add_ui(mouse);
        self.add_ally_object(mouse);          
        return;

    def on_change_scene(self):
        Player.MyPlayer.transform.tx, Player.MyPlayer.transform.ty = 400, 220; 
        Scene.BACK_GROUND_MUSIC.__del__();
        BossRoomScene.BGM.repeat_play();
        pass;

def monster_empty(scene):
    for obj in scene.game_object_list_monster:
        if obj.name == "Belial":
            return False;

    return True;

def run_game_clear_event(scene):
    print("Game Clear!!");
    from Effect import EffectStaticFont;
    from Effect import EffectStaticSprite2;
    #scene.AddObstacleObject(EffectStaticSprite(scene, 200, 200, BossRoomScene.CLEAR_IMG, 10, lambda : print("real clear"))); # 일단 포털을 넣어놨지만 
    scene.add_obstacle(EffectStaticSprite2(scene, 0, Const.WIN_HEIGHT // 2, BossRoomScene.CLEAR_IMG, 1000 )); # 일단 포털을 넣어놨지만 
    scene.add_obstacle(EffectStaticFont(scene, Const.WIN_HEIGHT // 2, Const.WIN_HEIGHT // 4, BossRoomScene.Font, 1000, "종료는 ESC", (255, 0, 0) )); # 일단 포털을 넣어놨지만 



    # 문구 Effect Static Animation 등.. 사용하고
    # 사운드 바꿔주고
    # 게임을 종료시킴 or end Scene 만들자.
