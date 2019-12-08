from MyTimer import*;
from GameObject import *;
from Graphic import *;
from math import*;
from Const import Const as const;
from TileMap import *;
import pico2d;
import KeyIO;
import Scene;


#타일 맵.
class FoodShopBG(GameObject):
    SHOP_BG = None;
    def __init__(self, x ,y, angle, sx, sy, state):
        super(FoodShopBG, self).__init__(x,y,angle,sx,sy,state);
        if None == FoodShopBG.SHOP_BG :
            FoodShopBG.SHOP_BG = pico2d.load_image('assets/UI/UIrestaurant2(1920x1080).png');

        self.has_image = True;
        self.cam_x = 0;
        self.cam_y = 0;
        self.cam:GameObject = None;
        self.name = "FoodShopBG";
        #GameObject.Cam.SetMapSize(self.map.width, self.map.height);

    def render(self):
        GameObject.Cam.SetCamOffset(0, 0);
        self.SHOP_BG.draw_to_origin(0,0, Const.WIN_WIDTH, Const.WIN_HEIGHT);
        return;

    def update(self, time):
        self.cam_x, self.cam_y =  GameObject.Cam.transform.tx, GameObject.Cam.transform.ty;
        return;

