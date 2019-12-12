
from GameObject import *;
from Const import *;
from KeyIO      import KeyInput;
from CollisionRect import*;

class Mouse(GameObject):
    Instance: GameObject= None;
    def __init__(self):
        super(Mouse, self).__init__(KeyInput.g_mouse_x , KeyInput.g_mouse_y, 0, 1, 1, True);
        self.name = "Mouse";
        self.state = True;
        self.has_image = True;
        self.x, self.y = 0, 0;
        self.Arrow = pico2d.load_image("assets/Mouse/Cursor00.png");
        self.Target = pico2d.load_image("assets/Mouse/Cursor01.png");
        self.IMG = self.Arrow;
        self.collider:Collision = CollisionRect(self.x,self.y, self.IMG.w // 2, self.IMG.h // 2);
        Instance = self;
        self.tag = Const.TAG_MOUSE;


    def set_cursor(self, type):
        if type == 0: self.IMG = self.Arrow;
        else : self.IMG = self.Target;

    def update(self, time):
        self.update_component();
        self.x, self.y = KeyInput.g_mouse_x , Const.WIN_HEIGHT - KeyInput.g_mouse_y - 1 ;
        #from Player import Player;
        #player = Player.MyPlayer;
        
        #t = Const.calc_degree(player.transform.tx - GameObject.Cam.camera_offset_x, player.transform.ty - GameObject.Cam.camera_offset_y, self.x, self.y);
        #print("{0} - {1} - {2} - {3} = {4} ".format(player.transform.tx - GameObject.Cam.camera_offset_x, player.transform.ty - GameObject.Cam.camera_offset_y, self.x, self.y, t));
      
        pass
    
    def render(self):
        self.IMG.draw(self.transform.tx , self.transform.ty , self.IMG.w, self.IMG.h);
        #draw_rectangle(*self.collider.get_area());
        pass;

    #충동한 객체의 태그 or name을 얻어서 어떤객체인지 파악.
    def on_collision(self, obj):
        #tag = obj.tag;
        #print("Mouse.py - {0} ".format(obj.name));
        pass;

    # 마우스의 경우 호명상의 렌더링 위치는 화면을 벗어 나면 안되기에 
    def update_component(self):
        self.previous_transform = self.transform;
        self.transform.tx = KeyInput.g_mouse_x;
        self.transform.ty = Const.WIN_HEIGHT - KeyInput.g_mouse_y - 1;

        self.collider.cx, self.collider.cy = self.transform.tx + GameObject.Cam.camera_offset_x, self.transform.ty + GameObject.Cam.camera_offset_y;
        return;

    def render_debug(self): 
        #if self.collider :
        #    from Graphic import GraphicLib;
        #    GraphicLib.DebugImg1.draw(self.collider.cx - GameObject.Cam.camera_offset_x, self.collider.cy - GameObject.Cam.camera_offset_y, self.IMG.w, self.IMG.h);
        #    #GraphicLib.DebugImg1.draw(self.x - GameObject.Cam.camera_offset_x, self.y- GameObject.Cam.camera_offset_y);    
        #    #GraphicLib.DebugImg1.draw(self.transform.tx, self.transform.ty);    

        return;

        pass;



