
from StateMachine import *;
from Const import *;
from Player import *;

from IdleState import *;
from JumpState import *;
from DashState import *;


#PIXEL_PER_METER = (20 / 0.1); # 10pixel 30 cm
#RUN_SPEED_KMPH = 80.0; #km / Hour
#RUN_SPEED_MPH = (RUN_SPEED_KMPH * 1000.0 / 60.0); #km / Hour
#RUN_SPEED_MPS = (RUN_SPEED_KMPH / 60.0); #km / Hour
#RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER); #km / Hour
FORCE_X = 500; 
#FORCE_Y = 500;
class RunStateForPlayer(StateMachine):
    animation_state =0;
    timer = 0;

    def __init__(self,gobj):
        self.obj = gobj;
        self.Fx = 0;
        self.Fy = self.obj.physx.force_y;
        self.obj.is_run = True;

        if(KeyInput.g_d): #r
            self.obj.last_dir = Const.direction_R;
            self.obj.dir = Const.direction_R;
            from Player import Player;
            self.obj.IMG = Player.IMGSForIdleR[0];
            self.Fx= FORCE_X;
            
        if(KeyInput.g_a):#l
            self.obj.last_dir = Const.direction_L;
            self.obj.dir = Const.direction_L;
            from Player import Player
            self.obj.IMG = Player.IMGSForIdleL[0];
            self.Fx = -FORCE_X;

        self.obj.set_velocity(self.Fx, self.Fy);
        #print("RunState 42 line {0}".format(self.Fx))
        return;

    def update(self):
        self.setAnimation();
        
        self.obj.physx.set_force(self.Fx, self.obj.physx.force_y); 

        if KeyInput.g_mouse_rdown :
            self.obj.add_queue(DashStateForPlayer(self.obj));
            temp = self.obj.current_state;
            self.obj.current_state.exit();
            self.obj.current_state = self.obj.state_queue.pop();
            del temp;
            return;

        if (KeyInput.g_w) :
            self.obj.add_queue(JumpStateForPlayer(self.obj));
            temp = self.obj.current_state;
            self.obj.current_state.exit();
            self.obj.current_state = self.obj.state_queue.pop();
            del temp;
            return;

        if(not KeyInput.g_d and not KeyInput.g_a):
            self.obj.add_queue(IdleStateForPlayer(self.obj));
            temp = self.obj.current_state;
            self.obj.current_state.exit();
            self.obj.current_state = self.obj.state_queue.pop();
            del temp;
            return;
    


    def render(self):
        if(self.obj.m_dir == Const.direction_R):self.renderForRight()
        else:self.renderForLeft();
        return;


    def renderForRight(self):
        from Player import Player
        Player.IMGSForRunR[RunStateForPlayer.animation_state].clip_composite_draw(0,0,
                           Player.IMGSForRunR[RunStateForPlayer.animation_state].w,
                           Player.IMGSForRunR[RunStateForPlayer.animation_state].h,
                           0,'',
                           self.obj.transform.tx-GameObject.Cam.camera_offset_x,
                           self.obj.transform.ty-GameObject.Cam.camera_offset_y,
                           );
    

    def renderForLeft(self):
        from Player import Player
        Player.IMGSForRunL[self.animation_state].clip_composite_draw(0,0,
                           Player.IMGSForRunR[RunStateForPlayer.animation_state].w,
                           Player.IMGSForRunR[RunStateForPlayer.animation_state].h,
                           0,'',
                           self.obj.transform.tx-GameObject.Cam.camera_offset_x,
                           self.obj.transform.ty-GameObject.Cam.camera_offset_y,
                           );


    def setAnimation(self):
        RunStateForPlayer.timer += Timer.get_elapsed_time();     
        if RunStateForPlayer.timer > 0.25:
            RunStateForPlayer.animation_state = (RunStateForPlayer.animation_state+1) % 4;
            RunStateForPlayer.timer=0;
        return;

    def exit(self):
        self.obj.is_run = False;
        return;


