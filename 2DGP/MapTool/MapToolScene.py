from Scene import *;
from Const import Const as const;
from Mouse import Mouse;
from KeyIO import *;

class MapToolScene(Scene):
    def __init__(self):       
        super(MapToolScene, self).__init__();
        self.AddAllyObject(BG(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True));
        self.AddUi(Mouse());

        # 맵 그리는칸과
        # 타일 팔레트. 
        return;

    def Initialize(self):
        self.AddAllyObject(BG(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True));
        pass;