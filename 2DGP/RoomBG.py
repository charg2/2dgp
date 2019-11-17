
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
class RoomBG(GameObject):
    UINQUE_INDEX:int = 0;
    def __init__(self, x ,y, angle, sx, sy, state, room_map_file_name:str):
        super(RoomBG, self).__init__(x,y,angle,sx,sy,state);
        
        self.has_image = True;
        self.map = TileMap(room_map_file_name);
        self.cam_x = 0;
        self.cam_y = 0;
        self.cam:GameObject = None;
        self.name = "RoomBG" + str(RoomBG.UINQUE_INDEX);
        RoomBG.UINQUE_INDEX += 1;

        GameObject.Cam.SetMapSize(self.map.width, self.map.height);

    def render(self):
        vx = Const.clamp(0, int(self.cam_x) - Const.WIN_WIDTH//2,  self.map.width - Const.WIN_WIDTH);
        vy = Const.clamp(0, int(self.cam_y) - Const.WIN_HEIGHT//2, self.map.height - Const.WIN_HEIGHT);

        GameObject.Cam.SetCamOffset(vx, vy);

        self.map.clip_render_to_origin(vx, vy, Const.WIN_WIDTH, Const.WIN_HEIGHT);
        return;


    def update(self, time):
        self.cam_x, self.cam_y =  GameObject.Cam.transform.tx, GameObject.Cam.transform.ty;
        return;
