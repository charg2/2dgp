from Scene import *;
from TitleBG import TitleBG as BG;
from TitleLogo import TitleLogo as LOGO;
from Const import Const as const;
from Mouse import Mouse;


class TitleScene(Scene):
    START_IMG = None;
    def __init__(self):       
        super(TitleScene, self).__init__();
        self.add_ally_object(BG(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True));
        if None == TitleScene.START_IMG:
            TitleScene.START_IMG = pico2d.load_image('assets/UI/complete2.png');
            TitleScene.BGM       = load_wav('assets/Sound/title.wav');
            TitleScene.BGM.set_volume(50);

        # 마지막 보여줄 마우스 마지막 배치
        #mouse = Mouse();
        Scene.BACK_GROUND_MUSIC = TitleScene.BGM;
        Scene.BACK_GROUND_MUSIC.repeat_play();


        self.add_ui(LOGO(300, 300, 0, 1.5, 1.5, True));
        self.add_ui(Mouse());

        #from Effect import EffectStaticSprite2;
        #self.add_ui(EffectStaticSprite2(self, 0, Const.WIN_HEIGHT // 2 - 300, TitleScene.START_IMG, 1000, None )); # 일단 포털을 넣어놨지만 
        #return;

    def on_change_scene(self):
        #Scene.BACK_GROUND_MUSIC.__del__();
        #BossRoomScene.BGM.repeat_play();
        pass;

    def Initialize(self):
        self.add_ally_object(BG(const.WIN_WIDTH//2, const.WIN_HEIGHT//2, 0,1,1,True));
        pass;