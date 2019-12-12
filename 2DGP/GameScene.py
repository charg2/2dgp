from Scene import Scene;
from GameBG import GameBG;
from Const import Const as const;
from Mouse import Mouse;
from Player import Player;

from Belial import *;
from Banshee import *;
from SkeletonArcher import *;
from SkeletonDog import *;

from Terrain import Terrain as terrain;
from Portal import Portal as portal;
from SmallHeal import SmallHeal as small_heal;
from BigHeal import BigHeal as big_heal;
from coin import Coin as coin;

#UI
from HPBar import *;
from Wallet import *;
from DashBar import *;
from MessageBox import *;

from Event import *;

START_X,START_Y = 300, 120;


class GameScene(Scene):
    BGM = None;
    def __init__(self):       
        super(GameScene,self).__init__();
        if None == GameScene.BGM :
            GameScene.BGM = load_wav('assets/Sound/jailfield.wav');
            GameScene.BGM.set_volume(50);

        
        self.bg = (GameBG(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True));
        
        self.add_terrain(self.bg);
        self.add_ally_object(Player(START_X,  START_Y + 90,0,1,1,True));          
        
        self.add_event(ConditionEvent( monster_empty, create_portal, self, self, 1));          

        self.add_monster(Banshee(START_X + 300, START_Y + 400 ,0,1,1,True));          
        self.add_monster(SkeletonDog(START_X + 700, START_Y + 90 ,0,1,1,True));          
        self.add_monster(SkeletonArcher(START_X + 100, START_Y + 100 ,0,1,1, True));     
        self.add_monster(SkeletonArcher(START_X + 290, 450 + 50 ,0,1,1, True));     
        self.add_monster(Banshee(START_X + 300, START_Y + 400 ,0,1,1,True));          
        self.add_monster(SkeletonDog(START_X + 700, START_Y + 90 ,0,1,1,True));          

        self.add_obstacle(small_heal(self, START_X + 500, START_Y + 400 ,0,1,1,True));          
        self.add_obstacle(big_heal(self, 90 * 15, START_Y + 200 ,0,1,1,True));          
        #self.AddObstacleObject(coin(self, START_X + 100, START_Y + 200 ,0,1,1,True));          
        #self.AddObstacleObject(coin(self, START_X + 200, START_Y + 240 ,0,1,1,True));          
        #self.AddObstacleObject(portal(90 * 25 - 45, START_Y + 90,0,1,1,True, 2));
        
        #UI
        self.add_ui(HPBarForPlayer.get_instance());

        self.add_ui(Wallet.get_instance());
        self.add_ui(DashBar.get_instance());

        

        ## BOTTOM 
        self.add_terrain(terrain(self.bg.map.width //2, 90, self.bg.map.width //2, 90, Const.BOTTOM ));
        # TOP
        self.add_terrain(terrain(self.bg.map.width //2, 1350, self.bg.map.width //2, 0, Const.TOP ));
        # LEFT 벽
        self.add_terrain(terrain(180, 450 + self.bg.map.height // 4, 0,  self.bg.map.height // 4, Const.LEFT));
        self.add_terrain(terrain(90, 90*5, 90,  0, Const.TOP));
        # RIGHT 벽
        self.add_terrain(terrain(3300, 100 + self.bg.map.height // 4, 0,  self.bg.map.height // 4, Const.RIGHT));
        

        self.add_terrain(terrain(90 * 8 - 45, 90*5, 135,  0));
        self.add_terrain(terrain(90 * 11 - 45, 90*7, 135,  0)); # 2번

        ##기둥
        #self.add_terrain(terrain(90 * 16 - 45, 90*6, 135,  0)); # 바닥 기둥 번
        #self.add_terrain(terrain(90 * 17, 90*3, 0,  90 * 2 + 45 , Const.LEFT)); # 바닥 기둥 번
        #self.add_terrain(terrain(90 * 14, 90*3, 0,  90 * 2 + 45 , Const.RIGHT)); # 바닥 기둥 번


        self.add_terrain(terrain(90 * 18 - 45, 90*9, 90 * 4 - 45,  0));
        self.add_terrain(terrain(90 * 25 - 45, 90*9, 90 * 1 - 45,  0));
        self.add_terrain(terrain(90 * 30, 90*9, 90 * 2,  0));

        mouse:Mouse = Mouse();
        mouse.set_cursor(Const.CURSOR_TARGET);

        self.add_ui(mouse);
        self.add_ally_object(mouse);          
        return;

    def on_change_scene(self):
        #Scene.BGM = GameScene.BGM;
        Scene.BACK_GROUND_MUSIC.__del__();
        GameScene.BGM.repeat_play();
        Scene.BACK_GROUND_MUSIC = GameScene.BGM;



def monster_empty(scene):
    if len(scene.game_object_list_monster) == 0 :
        return True;
    else :
        return False;
        

def create_portal(scene):
    print("portal on");
    scene.add_obstacle(portal(90 * 31 - 45, START_Y + 760,0,1,1,True, 2));
