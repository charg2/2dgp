from MyTimer import*;
from GameObject import *;
from Graphic import *;
from math import*;
from Const import Const as const;
import pico2d;
import KeyIO;
import Scene;


class GameBG(GameObject):
    def __init__(self, x ,y, angle, sx, sy, state):
        super(GameBG, self).__init__(x,y,angle,sx,sy,state);
        self.has_image = True;

        self.IMG = pico2d.load_image('assets/DUNGREED_GAME.png');
    
    def Render(self):
        #left x 최소 bottom y 최소
        self.IMG.draw_to_origin( 0, 0, const.WIN_WIDTH, const.WIN_HEIGHT)
        return;


    def Update(self,Time):
        #self.timer_for_changing += Time;
        pass;
        return;
