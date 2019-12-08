from MyTimer import*
from GameObject import *
from Graphic import *
from math import*
from Const import Const as const;
import pico2d;
from KeyIO import *;
import Scene;


class TitleBG(GameObject):
    def __init__(self, x ,y, angle, sx, sy, state):
        super(TitleBG, self).__init__(x,y,angle,sx,sy,state);
        self.IMG = pico2d.load_image('assets/TitleScene/Town00.png');
        self.has_image = True;
        self.timer_for_changing = 0.0;
        self.name = "TitleBG";
        self.collider:Collision = None;        
        self.colliderForObstacle:Collision = None;
        self.trigger = False;

    def render(self):
        #left x 최소 bottom y 최소
        self.IMG.draw_to_origin( 0, 0, const.WIN_WIDTH, const.WIN_HEIGHT);
        return;


    def update(self, Time):
        if self.trigger == False:
            if KeyInput.g_space :
                from EffectCutton import EffectCutton;
                from FrameWork import FrameWork as framework;
                framework.CurScene.add_ui(EffectCutton(Const.WIN_WIDTH//2,Const.WIN_HEIGHT//2,0,1,1,True, 1));
                self.trigger = True;
        return;