from Scene import Scene;
from GameBG import GameBG as BG;
from Const import Const as const;
from Mouse import *;
from Player import *;

#StartX,StartY = 110,160;

class GameScene(Scene):
    def __init__(self):       
        super(GameScene,self).__init__();
        self.BG = (BG(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True));
        self.AddAllyObject(BG(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True));
        #self.AddAllyObject(Player(StartX,StartY,0,1,1,True));    
        
        self.AddUi(Mouse());

        return;

    def Initialize(self):
        player = Player(0,90,0,1,1,True);
        self.AddAllyObject(BG(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True));
        pass;
