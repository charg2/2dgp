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


        self.AddMonsterObject(Banshee(START_X + 300, START_Y + 400 ,0,1,1,True));          
        self.AddMonsterObject(SkeletonDog(START_X + 700, START_Y + 90 ,0,1,1,True));          
        
        self.AddObstacleObject(small_heal(self, START_X + 500, START_Y + 400 ,0,1,1,True));          
        self.AddObstacleObject(big_heal(self, START_X + 7, START_Y + 200 ,0,1,1,True));          
        self.AddObstacleObject(coin(self, START_X + 100, START_Y + 200 ,0,1,1,True));          
        self.AddObstacleObject(coin(self, START_X + 200, START_Y + 240 ,0,1,1,True));          

        self.AddObstacleObject(portal(START_X + 2100, START_Y + 90,0,1,1,True, 2));
        
        #UI
        self.add_ui(HPBarForPlayer.get_instance());
        self.add_ui(MessageBox(100, 100, 1,1,1,True, "TESET용 문서"));
        self.add_ui(Wallet.get_instance());
        self.add_ui(DashBar.get_instance());

        self.AddMonsterObject(SkeletonArcher(START_X + 100, START_Y + 100 ,0,1,1, True));     
        
        from BelialLaser import BelialLaser as bl;
        self.AddMonsterObject(bl(self, START_X + 1000, START_Y + 600 ,0,1,1, True));        
        
        self.AddTerrainObject(terrain(self.bg.map.width //2, 90, self.bg.map.width //2, 90 ));
        self.AddTerrainObject(terrain(0, 100 + self.bg.map.height // 4, 180,  self.bg.map.height // 4));
        self.AddTerrainObject(terrain(90 * 8 - 45, 90*5, 135,  0));
        self.AddTerrainObject(terrain(1170, self.bg.map.height // 4, 90,  0));

        mouse:Mouse = Mouse();
        mouse.set_cursor(Const.CURSOR_TARGET);

        self.add_ui(mouse);
        self.AddAllyObject(mouse);          
        return;

    def on_change_scene(self):
        #Scene.BGM = GameScene.BGM;
        GameScene.BGM.repeat_play();
        Scene.BACK_GROUND_MUSIC = GameScene.BGM;

