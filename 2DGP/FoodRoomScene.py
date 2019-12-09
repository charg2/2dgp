
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

#UI
from HPBar import *;
from Wallet import *;
from DashBar import *;

#NPC
from Horerica import *;


START_X,START_Y = 300, 120;

# Scene을 하나 더 둠.
# 플레이어도 없고다 없는 깔끔한 곳으로 갓다가 나오면 다시 일로 이동 ㅇㅇ;
# 그래서 STAGE를 이동할때마다 음식 리스트를 갱신함.

class FoodRoomScene(Scene):
    def __init__(self):       
        FoodRoomScene.BGM = load_wav('assets/Sound/foodshop.wav');
        super(FoodRoomScene,self).__init__();
        from FoodRoomBG import FoodRoomBG as bg;
        self.bg = (bg(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True));
        #self.bg = (GameBG(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True));
        
        FoodRoomScene.FOOD_SHOP_BGM = load_wav('assets/Sound/foodshop.wav');
        self.AddTerrainObject(self.bg);
        self.AddAllyObject(Player.MyPlayer);          

        self.AddObstacleObject(portal(START_X + 2100, START_Y + 160, 0,1,1,True, 3));
        
        #NPC
        from FoodShop import FoodShop;
        FoodRoomScene.SHOP = FoodShop(START_X + 800, 200 + 256 ,0,1,1,True);
        self.AddTerrainObject(FoodRoomScene.SHOP);
        self.AddMonsterObject(Horerica(START_X + 1100, 180 + 35 ,0,1,1,True, FoodRoomScene.SHOP));          

        #UI
        self.add_ui(HPBarForPlayer.get_instance());
        self.add_ui(Wallet.get_instance());
        self.add_ui(DashBar.get_instance());

        self.AddTerrainObject(terrain(self.bg.map.width //2, 90, self.bg.map.width //2, 90 ));
        
        #LEFT
        self.AddTerrainObject(terrain(180, 100 + self.bg.map.height // 4, 0,  self.bg.map.height // 4, Const.LEFT));

        mouse:Mouse = Mouse();
        mouse.set_cursor(Const.CURSOR_TARGET);

        self.add_ui(mouse);
        self.AddAllyObject(mouse);          
        return;

    def on_change_scene(self):
        Player.MyPlayer.transform.tx, Player.MyPlayer.transform.ty = 400, 220; 
        Scene.BACK_GROUND_MUSIC.__del__();

        FoodRoomScene.BGM.repeat_play();
        Scene.BACK_GROUND_MUSIC = FoodRoomScene.BGM;
        pass;