
from GameObject import *;
from Const import *;
from KeyIO      import KeyInput;

class Mouse(GameObject):
    #LOAD = None;
    #Idle2:pico2d.Image = pico2d.Image;
    #Target:pico2d.Image = pico2d.Image;

    def __init__(self):
        super(Mouse, self).__init__(KeyInput.g_mouse_x , KeyInput.g_mouse_y, 1, 40, 40, True);
        self.name = "Mouse";
        self.state = True;
        self.has_image = True;
        self.x, self.y = 0, 0;
        self.Idle1 = pico2d.load_image("assets/Mouse/Cursor00.png");
        self.Target1 = pico2d.load_image("assets/Mouse/Cursor01.png");
        #if Mouse.LOAD == False:
            #Mouse.Idle2 = pico2d.load_image("assets/Mouse/Cursor00.png");
            #Mouse.Target = pico2d.load_image("assets/Mouse/Cursor01.png");
            #LOAD = True;
        #pass;



    def update(self, time):
        #print(type(self.Idle));
        self.x, self.y = KeyInput.g_mouse_x , Const.WIN_WIDTH - KeyInput.g_mouse_y - 1 ;
        pass;
    
    def render(self):
        #print( type(Mouse.Target));
        #Mouse.Idle.draw_to_origin(100, 100, 90, 90);
        #self.Idle1.opacify(0.5);
        self.Idle1.draw_to_origin(self.x , self.y, self.Idle1.w, self.Idle1.h);
        pass;



