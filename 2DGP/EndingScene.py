
from Scene import Scene;
from EndingBG import EndingBG;
from Const import Const as const;
from Mouse import Mouse;
from Player import Player;

from Belial import *;
from Banshee import *;
from SkeletonArcher import *;
from SkeletonDog import *;

from Terrain import Terrain as terrain;
from Portal import Portal as portal;
from SmallHeal import SmallHeal as small_heal;
from BigHeal import BigHeal as big_heal;
from coin import Coin as coin;

#UI
from HPBar import *;
from Wallet import *;
from DashBar import *;
from MessageBox import *;

from Event import *;

START_X,START_Y = 300, 120;

#이미지 띄우고 

class EndingScene(Scene):
    BGM = None;
    FONT = None;
    def __init__(self):       
        super(EndingScene,self).__init__();
        if None == EndingScene.BGM :
            EndingScene.BGM = load_wav('assets/Sound/jailfield.wav');
            EndingScene.BGM.set_volume(50);

        self.bg = (EndingBG(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True));
        
        self.add_terrain(self.bg);
        self.add_ally_object(Player(START_X,  START_Y + 90,0,1,1,True));          
        
        self.add_event(ConditionEvent( monster_empty, create_portal, self, self, 1));          

        self.add_ui(Wallet.get_instance());
        self.add_ui(DashBar.get_instance());

        
        EndingScene.BGM.play();# 노래 틀어줌.

        mouse:Mouse = Mouse();
        mouse.set_cursor(Const.CURSOR_TARGET);

        self.add_ui(mouse);
        self.add_ally_object(mouse);          
        return;

    def on_change_scene(self):
        #Scene.BGM = EndingScene.BGM;
        #EndingScene.BGM.repeat_play();
        #Scene.BACK_GROUND_MUSIC = EndingScene.BGM;
        pass;

def monster_empty(scene):
    if KeyInput.g_space : # 스페이스가 눌렷다면/
        return True;
    else :
        return False;
        

  # 타이틀 신으로 
  # 프레임워크 초기화ㅣ.

def create_portal(scene):
    print("portal on");
    scene.add_obstacle(portal(90 * 31 - 45, START_Y + 760,0,1,1,True, 2));
