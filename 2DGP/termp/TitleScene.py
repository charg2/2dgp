from Scene import *;
from TitleBG import TitleBG as BG;
import Const;

class TitleScene(Scene):
    def __init__(self):       
        super(TitleScene,self).__init__();
        self.AddAllyObject(BG(Const.WIN_WIDTH//2, Const.WIN_HEIGHT//2, 0,1,1,True));
        return;

    def Initialize(self):
        self.AddAllyObject(BG(Const.WIN_WIDTH//2, Const.WIN_HEIGHT//2, 0,1,1,True));
        pass;