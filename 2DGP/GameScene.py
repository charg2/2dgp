from Scene import Scene;
from GameBG import GameBG;
from Const import Const as const;
from Mouse import Mouse;
from Player import *;

from Banshee import *;

from Terrain import Terrain as terrain;

START_X,START_Y = 300, 120;

class GameScene(Scene):
    def __init__(self):       
        super(GameScene,self).__init__();
        self.bg = (GameBG(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True));
        
        self.AddTerrainObject(self.bg);
        self.AddAllyObject(Player(START_X, START_Y,0,1,1,True));          

        self.AddMonsterObject(Banshee(START_X + 300, START_Y + 400 ,0,1,1,True));          
        self.AddMonsterObject(Banshee(START_X + 300, START_Y ,0,1,1,True));          
        self.AddMonsterObject(Banshee(START_X + 500, START_Y + 100 ,0,1,1,True));          
        self.AddMonsterObject(Banshee(START_X + 1300, START_Y ,0,1,1,True));      
        self.AddMonsterObject(Banshee(START_X + 1500, START_Y ,0,1,1, True));          
        self.AddMonsterObject(Banshee(START_X + 1300, START_Y + 400 ,0,1,1,True));          
        self.AddMonsterObject(Banshee(START_X + 1300, START_Y ,0,1,1,True));          
        self.AddMonsterObject(Banshee(START_X + 1500, START_Y + 100 ,0,1,1,True));          
        self.AddMonsterObject(Banshee(START_X + 1300, START_Y + 100 ,0,1,1,True));      
        self.AddMonsterObject(Banshee(START_X + 1500, START_Y + 200 ,0,1,1, True));         
        self.AddTerrainObject(terrain(self.bg.map.width //2, 45, self.bg.map.width //2, 45 ));

        mouse:Mouse = Mouse();
        mouse.set_cursor(Const.CURSOR_TARGET);

        self.AddUi(mouse);
        self.AddAllyObject(mouse);          
        return;

    def Initialize(self): 
        player = Player(0,90,0,1,1,True);
        self.AddAllyObject(BG(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True));
        pass;
