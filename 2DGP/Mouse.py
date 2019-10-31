
from GameObject import *;
from Const import *;
from KeyIO      import KeyInput;

class Mouse(GameObject):
    #LOAD = None;
    #Idle2:pico2d.Image = pico2d.Image;
    #Target:pico2d.Image = pico2d.Image;

    def __init__(self):
        super(Mouse, self).__init__(KeyInput.g_mouse_x , KeyInput.g_mouse_y, 0, 1, 1, True);
        self.name = "Mouse";
        self.state = True;
        self.has_image = True;
        self.x, self.y = 0, 0;
        self.Arrow = pico2d.load_image("assets/Mouse/Cursor00.png");
        self.Target = pico2d.load_image("assets/Mouse/Cursor01.png");
        self.IMG = self.Arrow;
        #if Mouse.LOAD == False:
            #Mouse.Idle2 = pico2d.load_image("assets/Mouse/Cursor00.png");
            #Mouse.Target = pico2d.load_image("assets/Mouse/Cursor01.png");
            #LOAD = True;
        #pass;
    def set_cursor(self, type):
        if type == 0: self.IMG = self.Arrow;
        else : self.IMG = self.Target;


    def update(self, time):
        #print("{0},{1}".format(Const.WIN_WIDTH , KeyInput.g_mouse_y ));
        self.x, self.y = KeyInput.g_mouse_x , Const.WIN_HEIGHT - KeyInput.g_mouse_y - 1 ;

        pass;
    
    def render(self):
        #Mouse.Idle.draw_to_origin(100, 100, 90, 90);
        #self.Idle1.opacify(0.5);
        self.IMG.draw_to_origin(self.x , self.y, self.IMG.w, self.IMG.h);
        pass;

    #충동한 객체의 태그 or name을 얻어서 어떤객체인지 파악.
    def on_collision(self, obj):
        obj.tag;


        pass;



