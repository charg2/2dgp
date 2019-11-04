from Graphic import *;
from MyTimer import Timer;
from pico2d import *;
from KeyIO import *;
from Scene import Scene as Scene;
from TitleScene import *;
from GameScene import *;
from Mouse import *;
from typing import List;


class FrameWork:
    SceneList:List[Scene] = [];

    def init():
        GraphicLib.Initialize();
      
        FrameWork.GameState:bool = True;
        
        FrameWork.SceneList.append(TitleScene()); #타이틀 신 추가.
        FrameWork.SceneList.append(GameScene());

        FrameWork.CurScene:Scene = FrameWork.SceneList[1];

    def update():
        delay(0.016);
        Timer.Update();
        
        GraphicLib.ClearBuf();

        FrameWork.changeScene();        # 씬 변경을 체크
        FrameWork.CurScene.Update();    # logic update
        FrameWork.CurScene.Collide();   # collide
        FrameWork.CurScene.Render();    # render

        GraphicLib.Present();

    def changeScene():
        pass;


    def finalize():
        pass;

    def exit():
        GraphicLib.Exit();
        return;


    Initialize = staticmethod(init);
    Update = staticmethod(update);
    Input = staticmethod(input);
    Exit = staticmethod(exit);