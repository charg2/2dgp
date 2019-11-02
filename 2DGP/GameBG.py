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
class GameBG(GameObject):
    def __init__(self, x ,y, angle, sx, sy, state):
        super(GameBG, self).__init__(x,y,angle,sx,sy,state);
        
        self.has_image = True;
        self.map = TileMap("room1.map");
        self.cam_x = 0;
        self.cam_y = 0;
        self.cam:GameObject = None;
        self.name = "GameBG";

        GameObject.Cam.SetMapSize(self.map.width, self.map.height);

    def render(self):
        vx = Const.clamp(0, int(self.cam_x) - Const.WIN_WIDTH//2,  self.map.width - Const.WIN_WIDTH);
        vy = Const.clamp(0, int(self.cam_y) - Const.WIN_HEIGHT//2, self.map.height - Const.WIN_HEIGHT);

        GameObject.Cam.SetCamOffset(vx, vy);

        #self.map.render();
        self.map.clip_render_to_origin(vx, vy, Const.WIN_WIDTH, Const.WIN_HEIGHT);

        #left x 최소 bottom y 최소
        #self.IMG.draw_to_origin( 0, 0, const.WIN_WIDTH, const.WIN_HEIGHT);
        return;


    def update(self, time):
        self.cam_x, self.cam_y =  GameObject.Cam.transform.tx, GameObject.Cam.transform.ty;
        return;
