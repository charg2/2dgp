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
    def __init__(self):       
        super(BossRoomScene,self).__init__();
        self.bg = (RoomBG(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True, "room_boss.map"));
        
        self.AddTerrainObject(self.bg);
        self.AddAllyObject(Player.MyPlayer);          

        self.AddMonsterObject(Belial(START_X + 800, START_Y + 690 ,0,1,1,True));          
        #self.AddObstacleObject(portal(START_X + 800, START_Y,0,1,1,True,0));
        self.AddTerrainObject(terrain(self.bg.map.width //2, 90, self.bg.map.width //2, 90 ));
        self.AddTerrainObject(terrain(self.bg.map.width //2, 1800, self.bg.map.width //2, 0 ));
        self.AddTerrainObject(terrain(0, 450+ self.bg.map.height // 4, 180,  (self.bg.map.height // 4) ) );

        #self.AddTerrainObject(terrain(100, 100, 50, 45));

        mouse:Mouse = Mouse();
        mouse.set_cursor(Const.CURSOR_TARGET);

        self.add_ui(HPBarForPlayer.get_instance());
        self.add_ui(Wallet.get_instance());
        self.add_ui(DashBar.get_instance());
        
        self.add_ui(mouse);
        self.AddAllyObject(mouse);          
        return;

    def on_change_scene(self):
        Player.MyPlayer.transform.tx, Player.MyPlayer.transform.ty = 400, 220; 
        Scene.BACK_GROUND_MUSIC.__del__();
        GameScene.BGM.repeat_play();
        pass;
