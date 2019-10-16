from pico2d import *
from Graphic import *

class FrameWork:
    object_list = [];

    def init():
      Graphiclib.Initialize();
      
      FrameWork.GameState = True;
    
    def update():
        Graphiclib.ClearBuf();

    def input():
        pass;

    def render():
        for obj in object_list:
            obj.render();

    def exit():
        Graphiclib.Exit();
        return;

    Initialize = staticmethod(init);
    Update = staticmethod(update);
    Exit = staticmethod(exit);