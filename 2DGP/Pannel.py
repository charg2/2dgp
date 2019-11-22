from GameObject import *;
from Graphic import *;
#from math import*;
from FrameWork import *;
from Const import *;
from CollisionRect import*;

from typing import List;

class FoodShop(GameObject):
    IMG:Image = None;
    def __init__(self, x, y, angle, sx, sy, state):
        super(FoodShop, self).__init__(x, y, angle, sx, sy, state);
        if None == FoodShop.IMG :
            FoodShop.IMG = pico2d.load_image('assets/UI/A_DungeonInn(1188x552).png');
            pass;
        
        self.name = "FoodShop";
        self.state = True;
        self.has_image = True;

    def render(self): 
        FoodShop.IMG.clip_composite_draw(0,0,
                   FoodShop.IMG.w,
                   FoodShop.IMG.h,
                   0,'', 
                   self.transform.tx-GameObject.Cam.camera_offset_x,
                   self.transform.ty-GameObject.Cam.camera_offset_y,
                   FoodShop.IMG.w,
                   FoodShop.IMG.h,
                   );

        self.render_debug();
        return;


    def render_debug(self): 
        if self.collider :
            draw_rectangle(*self.collider.get_area_offset(GameObject.Cam.camera_offset_x, GameObject.Cam.camera_offset_y));
        return;

    def on_collision(self, obj):
        pass;