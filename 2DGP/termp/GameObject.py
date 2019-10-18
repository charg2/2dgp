from Transform import *;
import Graphic;
from Const import *;
from pico2d import *;



class GameObject:
    def __init__(self ,x , y, angle, sx, sy, state):
        self.name = "default";
        self.transform = Transform(x, y, angle, sx, sy);
        self.previous_transform = Transform(0,0,0,0,0);

        self.state = state;
        self.has_image = False;

        self.collider:Collision = None;        
        self.colliderForObstacle:Collision = None;

        self.tag = 0;

    def update(self, Time):
        pass;
    def render(self):
        pass;

    def set_state(self,state):
        self.state = state;
        return;

    def get_state(self):
        return self.state;
    def get_tag(self):
        return self.tag;

    def on_collision(self,GObj):
        pass;

    def has_image(self):
        return self.has_image;