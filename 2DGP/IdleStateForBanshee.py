from StateMachine import *;

from Banshee import *;
from Graphic import *;

#from AttackStateForBanshee import *;


LEFT, CENTER, RIGHT =range(-1,2);

class IdleStateForBanshee(StateMachine):
    def __init__(self, banshee):
        self.banshee = banshee;
        
        self.banshee.animation_state = 0;

        #self.start_x, self.start_y = banshee.transform.tx, banshee.transform.ty;
        self.offset_x, self.offset_y = 100, 100;
        self.turn_timer:float = 0.0;
        
        self.timer = 0;
        self.animation_state = 0;
        return;


    def update(self):
        from Const import Const;
        self.timer += Timer.get_elapsed_time();   
        self.turn_timer += Timer.get_elapsed_time();   
        
        if self.banshee.m_dir == Const.direction_R :
            self.banshee.transform.tx += 2;

            if self.turn_timer > 3.0:
                self.turn_timer = 0;
                self.banshee.m_dir = Const.direction_L;
        else :
            self.banshee.transform.tx -= 2;

            if self.turn_timer > 3.0:
                self.turn_timer = 0;
                self.banshee.m_dir = Const.direction_R;

        if self.timer>0.225:
            self.animation_state= (self.animation_state+1) % 2;
            self.timer=0;


        return;
    

    def render(self):
        from Const import Const;
        #if(self.banshee.last_dir == Const.direction_R) :
        if(self.banshee.m_dir == Const.direction_R) :
            self.renderForRight();
        else:
            self.renderForLeft();
        return;


    def renderForRight(self):
        from Banshee import Banshee;
        Banshee.IMGSForIdleR[self.animation_state].clip_composite_draw(0,0,
                           Banshee.IMGSForIdleR[self.animation_state].w,
                           Banshee.IMGSForIdleR[self.animation_state].h,
                           0,'', 
                           self.banshee.transform.tx-GameObject.Cam.camera_offset_x,
                           self.banshee.transform.ty-GameObject.Cam.camera_offset_y,
                           );

    def renderForLeft(self):
        from Banshee import Banshee
        Banshee.IMGSForIdleL[self.animation_state].clip_composite_draw(0,0,
                           Banshee.IMGSForIdleL[self.animation_state].w,
                           Banshee.IMGSForIdleL[self.animation_state].h,
                           0,'',
                           self.banshee.transform.tx-GameObject.Cam.camera_offset_x,
                           self.banshee.transform.ty-GameObject.Cam.camera_offset_y,
                           );
    def exit(self):
        pass;




