from Transform import *

#offset을 이용해 화면에 그려줄 위치를 보여줌.
class Camera:
    def __init__(self, x, y, angle, sx, sy, state):
        self.transform = Transform(x,y,angle,sx,sy);
        self.map_width = 0;
        self.map_height = 0;
        self.camera_offset_x =0;
        self.camera_offset_y = 0;
        return;

    def SetMapSize(self,x,y):
        self.map_width = x;
        self.map_height = y;

    def SetCamOffset(self,x,y):
        self.camera_offset_x =x;
        self.camera_offset_y =y;

