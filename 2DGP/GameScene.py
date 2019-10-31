from Scene import Scene;
from GameBG import GameBG;
from Const import Const as const;
from Mouse import Mouse;
from Player import *;

from Banshee import *;

START_X,START_Y = 300, 120;

class GameScene(Scene):
    def __init__(self):       
        super(GameScene,self).__init__();
        self.bg = (GameBG(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True));
        
        self.AddAllyObject(self.bg);
        self.AddAllyObject(Player(START_X, START_Y ,0,1,1,True));          
        self.AddAllyObject(Banshee(START_X + 300, START_Y + 400 ,0,1,1,True));          

        mouse:Mouse = Mouse();
        mouse.set_cursor(1);
        self.AddUi(mouse);
        return;

    def Initialize(self): 
        player = Player(0,90,0,1,1,True);
        self.AddAllyObject(BG(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True));
        pass;
