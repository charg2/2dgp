from MyTimer import*
from GameObject import *
from Graphic import *
from math import*
import pico2d;
import Const;
import KeyIO;
import Scene;


class TitleBG(GameObject):
    def __init__(self, x ,y, angle, sx, sy, state):
        super(TitleBG, self).__init__(x,y,angle,sx,sy,state);
        self.has_image = True;

        self.IMG = pico2d.load_image('assets/KPU_GROUND.png');
        self.timer_for_changing = 0.0;
    
    def Render(self):
        #left x 최소 bottom y 최소
        self.IMG.draw_to_origin( 0, 0, Const.WIN_WIDTH, Const.WIN_HEIGHT)
        return;

    #def RenderForMinimap(self):
        #self.IMG.draw_to_origin(400, 0,Const.WIN_WIDTH//4, Const.WIN_HEIGHT//4)
        #return;


    def Update(self,Time):
        self.timer_for_changing += Time;
        if(self.timer_for_changing>1.0):
            pass;
            #import FrameWork;
            #import EffectCutton;
            #FrameWork.FrameWork.CurScene.AddUi(EffectCutton.EffectCutton(const.WIN_WIDTH//2,const.WIN_HEIGHT//2,0,1,1,True,Const.title));
        return;