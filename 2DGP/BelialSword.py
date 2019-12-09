
from GameObject import *;
from Graphic import *;
from math import*;
from FrameWork import *;
from KeyIO import *;
from Const import *;
from CollisionRect import*;

from Player import Player;
#from IdleStateForBelial import *;

from typing import List;

frame_time = 0.2;
frame = 10;
damage = 10;
count = 6;
extinction_time = 5;
start_time = 1;
velocity = 1800;

class BelialSword(GameObject):
    LOAD:bool = False;
    UNIQUE_ID:int = 0;
    IMG:Image = None;

    def __init__(self, owner, x, y, angle, sx, sy, state):
        super(BelialSword, self).__init__(x, y, angle, sx, sy, state);
        if BelialSword.LOAD == False:
            BelialSword.IMG = pico2d.load_image('assets/Monster/Belial/Sword/IMG-0.png');
            BelialSword.LOAD = True;

        self.name = "BelialSword_" + str(BelialSword.UNIQUE_ID);
        BelialSword.UNIQUE_ID += 1;

        self.has_image = True;
        self.velocity = 0; 
        self.owner = owner;
        self.extinction_timer = 0.0;
        self.start_timer = 0.0;

        self.collider:Collision = CollisionRect(x,y, self.IMG.w // 2, self.IMG.h // 2);
        self.count = 0;
        self.offset_x = 0;
        pass;

    def update(self, time):
        self.update_component();
        self.update_timer(time);
        self.clampingInWindow();
        self.Physx(time);
        pass;

    def update_component(self):
        self.previous_transform = self.transform;
        self.collider.cx, self.collider.cy = self.transform.tx, self.transform.ty;

    def Physx(self, time):
        radian = self.transform.angle * math.pi;
        
        self.physx.velocity_x = velocity * math.sin(radian) * time;
        self.physx.velocity_y = velocity * math.cos(radian) * time;
        
        self.transform.set_position(self.physx.velocity_x, self.physx.velocity_y);

    def render(self):
        BelialSword.IMG.rotate_draw(self.transform.angle, self.transform.tx - GameObject.Cam.camera_offset_x, self.transform.ty - GameObject.Cam.camera_offset_y);    
        pass;

    def render_debug(self): 
        if self.collider :
            draw_rectangle(*self.collider.get_area_offset(GameObject.Cam.camera_offset_x, GameObject.Cam.camera_offset_y));

        return;
    def on_collision(self, obj):
        if Const.TAG_PLAYER == obj.tag :
            obj.calc_hp(damage);
            self.state = False;

        elif Const.TAG_TERRAIN == obj.tag:
            self.state = False;
        pass;
    
    def update_timer(self,time):
        self.start_timer += time;
        self.extinction_timer += time;
        # 시간 지나면 사라짐.
        if self.start_timer > start_time:
            self.velocity = velocity;

        if self.extinction_timer > extinction_time:
            self.state = False;

    def clampingInWindow(self):
        self.transform.tx = Const.clamp(0, self.transform.tx, GameObject.Cam.map_width-self.IMG.w//16)  
        self.transform.ty = Const.clamp(0, self.transform.ty, GameObject.Cam.map_height-self.IMG.h//8)
        return;
