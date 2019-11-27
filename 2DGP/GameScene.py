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
        
        self.AddTerrainObject(self.bg);
        self.AddAllyObject(Player(START_X,  START_Y + 90,0,1,1,True));          
        
        self.AddAllyObject(ConditionEvent( monster_empty, create_portal, self, self, 1));          

        self.AddMonsterObject(Banshee(START_X + 300, START_Y + 400 ,0,1,1,True));          
        self.AddMonsterObject(SkeletonDog(START_X + 700, START_Y + 90 ,0,1,1,True));          
        
        self.AddObstacleObject(small_heal(self, START_X + 500, START_Y + 400 ,0,1,1,True));          
        self.AddObstacleObject(big_heal(self, START_X + 7, START_Y + 200 ,0,1,1,True));          
        #self.AddObstacleObject(coin(self, START_X + 100, START_Y + 200 ,0,1,1,True));          
        #self.AddObstacleObject(coin(self, START_X + 200, START_Y + 240 ,0,1,1,True));          
        #self.AddObstacleObject(portal(90 * 25 - 45, START_Y + 90,0,1,1,True, 2));
        
        #UI
        self.add_ui(HPBarForPlayer.get_instance());

        self.add_ui(Wallet.get_instance());
        self.add_ui(DashBar.get_instance());

        self.AddMonsterObject(SkeletonArcher(START_X + 100, START_Y + 100 ,0,1,1, True));     
        

        self.AddTerrainObject(terrain(self.bg.map.width //2, 90, self.bg.map.width //2, 90 ));
        self.AddTerrainObject(terrain(0, 100 + self.bg.map.height // 4, 180,  self.bg.map.height // 4));
        self.AddTerrainObject(terrain(90 * 8 - 45, 90*5, 135,  0));
        self.AddTerrainObject(terrain(90 * 11 - 45, 90*7, 135,  0));
        self.AddTerrainObject(terrain(90 * 18 - 45, 90*9, 90 * 4 - 45,  0));
        self.AddTerrainObject(terrain(90 * 25 - 45, 90*9, 90 * 1 - 45,  0));
        self.AddTerrainObject(terrain(90 * 30 - 45, 90*9, 90 * 2 - 45,  0));

        mouse:Mouse = Mouse();
        mouse.set_cursor(Const.CURSOR_TARGET);

        self.add_ui(mouse);
        self.AddAllyObject(mouse);          
        return;

    def on_change_scene(self):
        #Scene.BGM = GameScene.BGM;
        GameScene.BGM.repeat_play();
        Scene.BACK_GROUND_MUSIC = GameScene.BGM;



def monster_empty(scene):
    if len(scene.game_object_list_monster) == 0 :
        return True;
    else :
        return False;
        

def create_portal(scene):
    print("portal on");
    scene.AddObstacleObject(portal(90 * 31 - 45, START_Y + 760,0,1,1,True, 2));
