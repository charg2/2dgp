from Transform import Transform;
from Camera import *;
import Graphic;
from Const import *;
from pico2d import *;



class GameObject:
    Font = None;
    Cam = Camera(0, 0, 0, 0, 0, True);
    def __init__(self ,x , y, angle, sx, sy, state):
        self.name = "default";
        self.transform = Transform(x, y, angle, sx, sy);
        self.previous_transform = Transform(0,0,0,0,0);

        self.state = state;
        self.has_image = False;
        self.basictimer =0.0;

        self.state_queue:list = [];
        self.tag = 0;

        if GameObject.Font == None :
            GameObject.Font= pico2d.load_font('assets/font.TTF', 16);
    
    def add_queue(self, State):
        self.state_queue.insert(0, State); # 맨처음 위치에 추가.
        #print(self.state_queue);
        return;

    def update(self, Time):
        pass;

    def render(self):
        pass;

    def set_state(self,state):
        self.state = state;
        return;

    def on_collision(self,GObj):
        pass;

    def has_image(self):
        return self.has_image;