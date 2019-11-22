
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

class FoodShopScene(Scene):
    def __init__(self):       
        super(FoodShopScene,self).__init__();
        from FoodShopBG import FoodShopBG as bg;
        self.bg = (bg(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True));
        #self.bg = (GameBG(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True));
        
        self.AddTerrainObject(self.bg);
        self.AddAllyObject(Player.MyPlayer);          

        self.AddObstacleObject(portal(START_X + 2100, START_Y + 90, 0,1,1,True, 3));
        
        #NPC
        self.AddMonsterObject(Horerica(START_X + 1100, 180 + 35 ,0,1,1,True));          
        from Pannel import FoodShop;
        self.AddTerrainObject(FoodShop(START_X + 800, 200 + 256 ,0,1,1,True));

        #UI
        self.AddUi(HPBar.get_instance());
        self.AddUi(Wallet.get_instance());
        self.AddUi(DashBar.get_instance());

        self.AddTerrainObject(terrain(self.bg.map.width //2, 90, self.bg.map.width //2, 90 ));
        self.AddTerrainObject(terrain(0, 100 + self.bg.map.height // 4, 180,  self.bg.map.height // 4));
        #print("height =", self.bg.map.height)

        mouse:Mouse = Mouse();
        mouse.set_cursor(Const.CURSOR_TARGET);

        self.AddUi(mouse);
        self.AddAllyObject(mouse);          
        return;

    def on_change_scene(self):
        pass;