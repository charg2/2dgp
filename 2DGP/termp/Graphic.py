from pico2d import *
from Const import *
import os;

class GraphicLib:
    Font = None;
    def init():
        pico2d.open_canvas(Const.WIN_WIDTH,Const.WIN_HEIGHT,True);
        pico2d.hide_lattice();
        pico2d.hide_cursor();

        return;

    def present():
        pico2d.update_canvas();
        pico2d.print_fps();
        return;

    def exit():
        pico2d.close_canvas();
        return;
        
    def clearbuf():
        pico2d.clear_canvas();
        return;


    Initialize  = staticmethod(init);
    Present     = staticmethod(present);
    Exit        = staticmethod(exit);
    ClearBuf    = staticmethod(clearbuf);

if(__name__ == "__main__"):
    os.chdir("assets");
    GraphicLib.Initialize()
    #grass = GraphicLib.Render('grass.png') 
    #character = GraphicLib.Render('character.png')

    x = 0
    while (x < 800):
       GraphicLib.ClearBuf() 
       grass.draw(400, 30) 
       character.draw(x, 90) 
       x = x + 2 
       GraphicLib.Present() 
       #delay(0.01) 
       #get_events()
    GraphicLib.Exit()