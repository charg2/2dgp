from GameObject import *;
from Graphic import *;
from math import*;
from FrameWork import *;
from KeyIO import *;
from Const import *;


IdleR, IdleL = range(2);

class Player(GameObject):
    IMGSForIdleL = [];
    IMGSForIdleR = [];
    IMGSForRunL = [];
    IMGSForRunR = [];

    def __init__(self, x, y, angle, sx, sy, state):
        super(Player, self).__init__(x, y, angle, sx, sy, state);
        self.has_image = True;
        if Player.LOAD == False:
            #Player.IMGSForIdleL.append(pico2d.load_image('assets/Player/Idle/L1.png'));
            #Player.IMGSForIdleL.append(pico2d.load_image('assets/Player/Idle/L2.png'));
            #Player.IMGSForIdleL.append(pico2d.load_image('assets/Player/Idle/L3.png'));
            #Player.IMGSForIdleL.append(pico2d.load_image('assets/Player/Idle/L4.png'));
            Player.IMGSForIdleR.append(pico2d.load_image('assets/Player/Idle/R (1).png'));
            Player.IMGSForIdleR.append(pico2d.load_image('assets/Player/Idle/R (2).png'));
            Player.IMGSForIdleR.append(pico2d.load_image('assets/Player/Idle/R (3).png'));
            Player.IMGSForIdleR.append(pico2d.load_image('assets/Player/Idle/R (4).png'));
            Player.IMGSForIdleR.append(pico2d.load_image('assets/Player/Idle/R (5).png'));

            Player.LOAD = True;
        self.dir = IdleR; 
        self.animation_numb = 0;
        self.tag = 1;

    def render(self): 
        self.current_state.render();
        return;

    def update(slef, time):
        pass;

