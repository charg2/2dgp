from pico2d import *
from Const import Const as const;

import os;

class GraphicLib:
    Font:Font = None;
    DebugMode:bool = False;

    def init():
        #os.chdir("assets"); # asset folder
        pico2d.open_canvas(const.WIN_WIDTH, const.WIN_HEIGHT, sync = True);
        pico2d.hide_lattice();
        pico2d.hide_cursor();

        if GraphicLib.Font is None :
            #print(os.listdir());
            GraphicLib.Font= pico2d.load_font('assets/Font/font.TTF', 60);
        return;

    def present():
        pico2d.update_canvas();
        pico2d.print_fps();
        return;

    def exit():
        pico2d.close_canvas();
        return;
        
    def clear_buf():
        pico2d.clear_canvas();
        return;

    def get_debug_mode() -> bool:
        return GraphicLib.DebugMode;

    def set_debug_mode(self, state:bool):
        GraphicLib.DebugMode = state;
        return;

    Initialize  = staticmethod(init);
    Present     = staticmethod(present);
    Exit        = staticmethod(exit);
    ClearBuf    = staticmethod(clear_buf);
    
    #os.chdir("assets");
if '__main__' == __name__:
    GraphicLib.Initialize()
    #character = GraphicLib.Render('character.png')
    
    x = 0
    while (x < 800):
       GraphicLib.ClearBuf();
       GraphicLib.DebugImg.draw_to_origin(200, 0, 1000, 100); 
       x = x + 2 
       GraphicLib.Present() 
       #delay(0.01) 
       #get_events()
    GraphicLib.Exit()