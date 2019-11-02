
from StateMachine import *;
from IdleState import*;
from RunState import*;
from Const import *;
from Player import *;

class JumpStateForPlayer(StateMachine):
    animation_state =0;
    timer           = 0;
    
    def __init__(self,gobj):
        self.obj = gobj;
        self.Fy =0.0;

        self.jump_velocity   = 8;
        self.jump_accelation = -0.4; 
    

        #self.jump_start_time   = gobj.basictimer;
        self.jump_end_time   = gobj.basictimer + 0.8;
        self.jump_timer   = gobj.basictimer;

        if Const.direction_R == self.obj.m_dir :
            self.obj.last_dir = Const.direction_R;
            self.obj.dir = Const.direction_R;
            from Player import Player;
            self.obj.IMG = Player.IMGSForJump[0];
            self.Fx = self.obj.force_x;

        if Const.direction_L == self.obj.m_dir :
            self.obj.last_dir = Const.direction_L;
            self.obj.dir = Const.direction_L;
            from Player import Player;
            self.obj.IMG = Player.IMGSForJump[1];
            self.Fx = -self.obj.force_x;
        return;

    # 점프 상승중의 버튼 상태를 조사해 반영함.
    def update(self):
        self.check_jump_timer();

        if self.jump_timer < self.obj.basictimer :
            self.jump_timer += 0.02;
            self.obj.transform.ty += self.jump_velocity;
            self.jump_velocity += self.jump_accelation;

        return;
    
    def check_jump_timer(self) :
        print("JumpState.py 56   {0} -- {1}".format(self.jump_end_time , self.obj.basictimer));
        if self.jump_end_time < self.obj.basictimer:
            self.obj.add_queue(IdleStateForPlayer(self.obj));
            temp = self.obj.current_state;
            self.obj.current_state.exit();
            self.obj.current_state = self.obj.state_queue.pop();
            del temp;
        return;

    def render(self):
        self.obj.IMGSForJump[self.obj.m_dir].clip_composite_draw(0,0,
                           self.obj.IMG.w,self.obj.IMG.h,0,'',
                           self.obj.transform.tx-GameObject.Cam.camera_offset_x,
                           self.obj.transform.ty-GameObject.Cam.camera_offset_y,
                           );

 

    def exit(self):
        print("jump_exit");
        return;




