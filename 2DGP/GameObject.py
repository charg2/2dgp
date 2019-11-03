from Transform import Transform;
from Camera import *;
from Collision import *;

from Const import *;
from pico2d import *;

from physx import Physx;


class GameObject:
    Font = None;
    Cam = Camera(0, 0, 0, 0, 0, True);
    def __init__(self ,x , y, angle, sx, sy, state):
        self.name:str = "default";
        self.transform:Transform = Transform(x, y, angle, sx, sy);
        self.previous_transform:Transform = Transform(0,0,0,0,0);

        self.physx = Physx();

        self.state:bool = state;
        self.has_image:bool = False;
        self.basictimer:float =0.0;

        self.state_queue:list = [];
        self.tag:int = 0;

        self.collider:Collision = None;        
        self.colliderForObstacle:Collision = None;

        if GameObject.Font == None :
            GameObject.Font= pico2d.load_font('assets/Font/font.TTF', 16);
    
    def add_queue(self, State):
        self.state_queue.insert(0, State); 
        #print(self.state_queue);
        return;

    def update(self, Time):
        pass;

    def render(self):
        pass;

    def render_debug(self):
        pass;

    def set_state(self,state):
        self.state = state;
        return;

    def on_collision(self,GObj):
        pass;

    def has_image(self):
        return self.has_image;

    def Physx(self,time):
        grivity_offset_y = 0; 
        if True == self.has_grivity() :
            grivity_offset_y = self.physx.acceleration_of_gravity; 
            
        self.transform.set_position(self.physx.velocity_x, self.physx.velocity_y - grivity_offset_y);

        #if False == self.physx.is_ground:
            #grivity_offset_y = -5;
        #self.transform.set_position(self.physx.velocity_x, self.physx.velocity_y + grivity_offset_y);       
        return;

    def set_force(self,x,y):
        self.physx.set_force(x,y);
        return;

    def set_velocity(self,vx,vy):
        self.physx.velocity_x = vx;
        self.physx.velocity_y = vy;
        return;

    def has_grivity(self) -> bool :
        return self.physx.has_grivity;

    def set_grivity(self, onoff:bool):
        self.physx.has_grivity = onoff;

    def set_acceleration_of_gravity(self, grivity:float):
        self.physx.acceleration_of_gravity = grivity;
        return;
