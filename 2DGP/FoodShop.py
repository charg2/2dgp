from GameObject import *;
from Graphic import *;
from KeyIO import *;

from FrameWork import *;
from Const import *;
from CollisionRect import*;

from typing import List;

class FoodShop(GameObject):
    IMG:Image           = None;
    SHOP_UI_BG:Image    = None;
    Instance:GameObject = None;

    def __init__(self, x, y, angle, sx, sy, state):
        super(FoodShop, self).__init__(x, y, angle, sx, sy, state);
        if None == FoodShop.IMG :
            FoodShop.IMG = pico2d.load_image('assets/UI/A_DungeonInn(1188x552).png');
            FoodShop.SHOP_UI_BG = pico2d.load_image('assets/UI/UIrestaurant2(1920x1080).png');
            Instance = self;
            
        self.name = "FoodShop";
        self.state = True;
        self.has_image = True;

        self.is_opend = False;

        self.current_index = 0;

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

        if self.is_opend :
            FoodShop.SHOP_UI_BG.draw_to_origin(0, 0, Const.WIN_WIDTH, Const.WIN_HEIGHT);
        return;

    def update(self, time):
        if self.is_opend : # 상점 열린 상황
            pass;
        pass;

    def render_debug(self): 
        return;

    def on_collision(self, obj):
        # 마우스 충돌체랑 목록 충돌체랑 겹치면 
        # 인덱스 바꿈.
        # 우클릭 햇다면 먹고 emty로 바꿈.
        # ㅇㅇ;
        pass;

    def open(self):
        if self.is_opend == False :
            self.is_opend = True;
            # c충돌 목록 추가.

            # foodshop scene로감.

        return ;

    def close(self):
        if self.is_opend == True :
            self.is_opend = False;
        return ;


    def get_instance():
        if None == FoodShop.Instance :
            FoodShop.Instance = FoodShop(START_X + 800, 200 + 256 ,0,1,1,True);

        return FoodShop.Instance;
