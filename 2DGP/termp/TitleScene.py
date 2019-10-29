from Scene import *;
from TitleBG import TitleBG as BG;
from Const import Const as const;
from Mouse import Mouse;


class TitleScene(Scene):
    def __init__(self):       
        super(TitleScene, self).__init__();
        self.AddAllyObject(BG(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True));
        
        
        # 마지막 보여줄 마우스 마지막 배치
        mouse = Mouse();
        self.AddUi(mouse);
        return;

    def Initialize(self):
        self.AddAllyObject(BG(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True));
        pass;