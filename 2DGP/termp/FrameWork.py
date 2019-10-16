from pico2d import *;
from Graphic import *;
from KeyIO import *;

class FrameWork:
    object_list = [];

    def init():
      GraphicLib.Initialize();
      
      FrameWork.GameState = True;
    
    def update():
        GraphicLib.ClearBuf();

    def input():
        KeyIO.Update();
        pass;

    def render():
        for obj in object_list:
            obj.render();

    def finalize():
        pass;

    def exit():
        Graphiclib.Exit();
        return;

    Initialize = staticmethod(init);
    Update = staticmethod(update);
    Input = staticmethod(input);
    Exit = staticmethod(exit);