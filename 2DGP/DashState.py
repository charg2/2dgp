
from StateMachine import *;
from IdleState import*;
from RunState import*;
from Const import *;
from Player import *;

class DashStateForPlayer(StateMachine):
    animation_state =0;
    timer = 0;
    animation_reverse = False;

    def __init__(self,gobj):
        self.obj = gobj;

        if(KeyInput.g_d):
            self.obj.last_dir = Const.direction_R;
            self.obj.dir = Const.direction_R;
            from Player import Player;
            self.obj.IMG = Player.IMGSForJumpR[0];
            self.Fx = self.obj.force_x;

        if(KeyInput.g_a):
            self.obj.last_dir = Const.direction_L;
            self.obj.dir = Const.direction_L;
            from Player import Player;
            self.obj.IMG = Player.IMGSForJumpL[0];
            self.Fx = -self.obj.force_x;
        return;

    # 충돌시 속도 0으로 바귐.
    def update(self):
        self.setAnimation();
        
        if Player.force_y == 0 :
            self.obj.add_queue(IdleStateForPlayer(self.obj));
            temp = self.obj.current_state;
            self.obj.current_state.exit();
            self.obj.current_state = self.obj.state_queue.pop();
            del temp;
        

        self.obj.transform.tx += self.Fx;
        return;
    
    def render(self):
        if(self.obj.last_dir == Const.direction_R):self.renderForRight()
        else:self.renderForLeft();
        return;

    def renderForRight(self):
        from Player import Player;
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
        return;



