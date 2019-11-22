from Scene import Scene;
from GameBG import GameBG;
from Const import Const as const;
from Mouse import Mouse;
from Player import Player;

from Belial import *;
from Banshee import *;
from SkeletonArcher import *;

from Terrain import Terrain as terrain;
from Portal import Portal as portal;
from SmallHeal import SmallHeal as small_heal;
from BigHeal import BigHeal as big_heal;
from coin import Coin as coin;

#UI
from HPBar import *;
from Wallet import *;
from DashBar import *;

#NPC
from Horerica import *;

START_X,START_Y = 300, 120;

class GameScene(Scene):
    def __init__(self):       
        super(GameScene,self).__init__();
        self.bg = (GameBG(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True));
        
        self.AddTerrainObject(self.bg);
        self.AddAllyObject(Player(START_X,  START_Y + 90,0,1,1,True));          

        self.AddMonsterObject(Banshee(START_X + 300, START_Y + 400 ,0,1,1,True));          
        self.AddMonsterObject(small_heal(self, START_X + 500, START_Y + 400 ,0,1,1,True));          
        self.AddMonsterObject(big_heal(self, START_X + 7, START_Y + 200 ,0,1,1,True));          
        self.AddMonsterObject(coin(self, START_X + 100, START_Y + 200 ,0,1,1,True));          
        self.AddMonsterObject(coin(self, START_X + 200, START_Y + 240 ,0,1,1,True));          

        self.AddObstacleObject(portal(START_X + 2100, START_Y + 90,0,1,1,True, 2));
        

        #UI
        self.AddUi(HPBar.get_instance());
        self.AddUi(Wallet.get_instance());
        self.AddUi(DashBar.get_instance());

        self.AddMonsterObject(SkeletonArcher(START_X + 100, START_Y + 100 ,0,1,1, True));     
        
        from BelialLaser import BelialLaser as bl;
        self.AddMonsterObject(bl(self, START_X + 1000, START_Y + 600 ,0,1,1, True));        
        
        self.AddTerrainObject(terrain(self.bg.map.width //2, 90, self.bg.map.width //2, 90 ));
        self.AddTerrainObject(terrain(0, 100 + self.bg.map.height // 4, 180,  self.bg.map.height // 4));
        self.AddTerrainObject(terrain(800, self.bg.map.height // 4, 100,  1));
        self.AddTerrainObject(terrain(1200, self.bg.map.height // 4, 100,  1));
        #print("height =", self.bg.map.height)

        mouse:Mouse = Mouse();
        mouse.set_cursor(Const.CURSOR_TARGET);

        self.AddUi(mouse);
        self.AddAllyObject(mouse);          
        return;

    def on_change_scene(self):
        pass;