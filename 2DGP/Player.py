from GameObject import *;
from Graphic import *;
from math import*;
from FrameWork import *;
from KeyIO import *;
from Const import *;


RUN_L, RUN_R, IDLE_R, IDLE_L = range(4);

class Player(GameObject):
    LOAD = False;

    IMGSForIdleL = [];
    IMGSForIdleR = [];
    IMGSForRunL = [];
    IMGSForRunR = [];
    IMGSForJumpL = [];
    IMGSForJumpR = [];
    IMGSForDeathL = [];
    IMGSForDeathR = [];

    def __init__(self, x, y, angle, sx, sy, state):
        super(Player, self).__init__(x, y, angle, sx, sy, state);
        self.has_image = True;
        if Player.LOAD == False:
            Player.IMGSForIdleR.append(pico2d.load_image('assets/Player/Idle/R (1).png'));
            Player.IMGSForIdleR.append(pico2d.load_image('assets/Player/Idle/R (2).png'));
            Player.IMGSForIdleR.append(pico2d.load_image('assets/Player/Idle/R (3).png'));
            Player.IMGSForIdleR.append(pico2d.load_image('assets/Player/Idle/R (4).png'));
            Player.IMGSForIdleR.append(pico2d.load_image('assets/Player/Idle/R (5).png'));
            Player.IMGSForIdleR.append(pico2d.load_image('assets/Player/Idle/L (1).png'));
            Player.IMGSForIdleR.append(pico2d.load_image('assets/Player/Idle/L (2).png'));
            Player.IMGSForIdleR.append(pico2d.load_image('assets/Player/Idle/L (3).png'));
            Player.IMGSForIdleR.append(pico2d.load_image('assets/Player/Idle/L (4).png'));
            Player.IMGSForIdleR.append(pico2d.load_image('assets/Player/Idle/L (5).png'));


            Player.LOAD = True;

        self.IMG = Player.IMGSForIdleR[0];
        self.dir = IDLE_R; 
        self.animation_numb = 0;
        self.tag = 1;
        self.force_x =2600; #cm/s
        self.force_y =2350;
        GameObject.Cam.transform = self.transform;
        self.jump_trigger = False;
        self.jump_timer = 0;
        self.key_timer = 0.5;
        #self.current_state = IdleStateForPlayer(self);



        # ability
        self.hp = 0;
        self.dash = 0;
        self.attack_spped = 0;
        self.critical = 0;

        #animation
        self.animation_numb = 0;
        self.animation_timer = 0.0;
        #self.dir = runR; # dir = last direction , offset = 2;
        #self.last_dir = runR%2;
        #self.current_state = IdleStateForPlayer(self);
        #self.tag = Const.Const.tag_player;

    def render(self): 
        #self.current_state.render();
        Player.IMGSForIdleR[self.animation_numb].draw(self.transform.tx, self.transform.ty);
        return;

    def update(self, time):
        self.animation_numb = (self.animation_numb + 1) % 5;
        pass;

    def on_collision(self, obj):
        pass;
