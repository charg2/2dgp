from Scene import *;
from TitleBG import TitleBG as BG;
from Const import Const as const;


class TitleScene(Scene):
    def __init__(self):       
        super(TitleScene,self).__init__();
        self.AddAllyObject(BG(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True));
        return;

    def Initialize(self):
        self.AddAllyObject(BG(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True));
        pass;