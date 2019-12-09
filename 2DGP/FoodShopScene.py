
from Scene import Scene;
from GameBG import GameBG;
from Const import Const as const;
from Mouse import Mouse;
from Player import Player;


from Terrain import Terrain as terrain;
from Portal import Portal as portal;

#UI
from HPBar import *;
from Wallet import *;
from DashBar import *;
from Menu import *;

#NPC
from Horerica import *;

from Event import *;
from Effect import *;


START_X,START_Y = 300, 120;

# Scene을 하나 더 둠.
# 플레이어도 없고다 없는 깔끔한 곳으로 갓다가 나오면 다시 일로 이동 ㅇㅇ;
# 그래서 STAGE를 이동할때마다 음식 리스트를 갱신함.


class FoodShopScene(Scene):
    TABLE_IMGS = [];
    def __init__(self):
        if 0 >= len(FoodShopScene.TABLE_IMGS):
            FoodShopScene.TABLE_IMGS.append(pico2d.load_image("assets/Food/Table (1)3.png"));
            FoodShopScene.TABLE_IMGS.append(pico2d.load_image("assets/Food/Table (2)3.png"));
            FoodShopScene.TABLE_IMGS.append(pico2d.load_image("assets/Food/Table (3)3.png"));
        

        FoodShopScene.BGM = load_wav('assets/Sound/foodshop.wav');
        super(FoodShopScene,self).__init__();
        from FoodShopBG import FoodShopBG as bg;
        #self.bg = (bg(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True));
        #self.bg = (GameBG(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True));
        
        FoodShopScene.FOOD_SHOP_BGM = load_wav('assets/Sound/foodshop.wav');
        #self.AddTerrainObject(self.bg);
    
        self.add_monster((bg(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True)));
        self.add_monster((EffectStaticAnimation(self, (const.WIN_WIDTH//2) + 240, (const.WIN_HEIGHT//2 ) - 30  ,FoodShopScene.TABLE_IMGS, len(FoodShopScene.TABLE_IMGS), 0.1, True )));
    
        #self.add_ui((bg(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True)));
        #self.add_ui((EffectStaticAnimation(self, (const.WIN_WIDTH//2) + 1000, (const.WIN_HEIGHT//2 ) - 30  ,FoodShopScene.TABLE_IMGS, 3, 0.2, True )));
 
 #selfAddMonsterObject.AddAllyObject(Player.MyPlayer);          

        self.AddObstacleObject(portal(START_X + 2100, START_Y + 160, 0,1,1,True, 4));
        
        #NPC
        #from FoodShop import FoodShop;
        #FoodShopScene.SHOP = FoodShop(START_X + 800, 200 + 256 ,0,1,1,True);
        #self.AddTerrainObject(FoodShopScene.SHOP);
        #self.AddMonsterObject(Horerica(START_X + 1100, 180 + 35 ,0,1,1,True, FoodShopScene.SHOP));          

        #UI
        self.add_ui(HPBarForPlayer.get_instance());
        self.add_ui(WalletR.get_instance());
        self.add_ui(DashBar.get_instance());


        #UI
        self.add_monster(Menu( 240, 600, 1, 1, 1, True));
        self.add_monster(Menu( 240, 400, 1, 1, 1, True));
        self.add_monster(Menu( 240, 200, 1, 1, 1, True));

        #EVENT
        # x를 누르면 전 신으로 돌아감.
        self.add_event(ConditionEvent(check_xkey_input, refill_food,None, self, 100));

        mouse:Mouse = Mouse();
        mouse.set_cursor(Const.CURSOR_TARGET);

        self.add_ui(mouse);
        self.AddAllyObject(mouse);          
        return;

    def on_change_scene(self):
        Player.MyPlayer.transform.tx, Player.MyPlayer.transform.ty = 400, 220; 
        Scene.BACK_GROUND_MUSIC.__del__();

        FoodShopScene.BGM.repeat_play();
        Scene.BACK_GROUND_MUSIC = FoodShopScene.BGM;
        pass;


def check_xkey_input() -> bool:
    if KeyInput.g_x:
        return True;
    else : 
        return False;

def refill_food(foodshop):
        foodshop.add_monster(Menu( 240, 600, 1, 1, 1, True));
        foodshop.add_monster(Menu( 240, 400, 1, 1, 1, True));
        foodshop.add_monster(Menu( 240, 200, 1, 1, 1, True));
        #foodshop.add_event(ConditionEvent(check_xkey_input, refill_food,None, foodshop, 100));

def go_to_foodroom_scene():
    from FrameWork import FrameWork;
    FrameWork.CurScene = FrameWork.SceneList[2];
