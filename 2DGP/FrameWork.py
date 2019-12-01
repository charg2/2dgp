from Graphic import *;
from MyTimer import Timer;
from pico2d import *;
from KeyIO import *;
from Scene import Scene as Scene;
from TitleScene import *;
from Mouse import *;
from Player import *;


from typing import List;

from GameScene import *;
from BossRoomScene import *;
from FoodRoomScene import *;

class FrameWork:
    SceneList:List[Scene] = [];

    def init():
        GraphicLib.Initialize();
        Timer.Initialize();
      
        FrameWork.GameState:bool = True;
        
        FrameWork.SceneList.append(TitleScene()); #타이틀 신 추가.
        FrameWork.SceneList.append(GameScene());
        FrameWork.SceneList.append(FoodRoomScene());
        FrameWork.SceneList.append(BossRoomScene());

        FrameWork.CurScene:Scene = FrameWork.SceneList[0];

    def update():
        Timer.Update();

        GraphicLib.ClearBuf();

        FrameWork.change_scene();        # 씬 변경을 체크

        FrameWork.CurScene.Update();    # logic update
        FrameWork.CurScene.Collide();   # collide
        FrameWork.CurScene.Render();    # render

        GraphicLib.Present();

    def change_scene():
        if(Scene.CurSceneNumber !=  Scene.SceneNumber):
            FrameWork.CurScene = FrameWork.SceneList[Scene.SceneNumber];
            FrameWork.SceneList[Scene.CurSceneNumber].ExitScene();
            Scene.CurSceneNumber = Scene.SceneNumber;
            FrameWork.CurScene.set_cam();
            FrameWork.CurScene.on_change_scene();
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