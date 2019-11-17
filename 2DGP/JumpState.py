
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
        #gobj.set_grivity(True);

        self.Fy = gobj.force_y + 30;

        self.Fx = 0;
        self.obj.is_jump = True;

        if Const.direction_R == self.obj.m_dir :
            self.obj.last_dir = Const.direction_R;
            self.obj.dir = Const.direction_R;
            from Player import Player;
            self.obj.IMG = Player.IMGSForJump[0];
            self.Fx = 0;

        if Const.direction_L == self.obj.m_dir :
            self.obj.last_dir = Const.direction_L;
            self.obj.dir = Const.direction_L;
            from Player import Player;
            self.obj.IMG = Player.IMGSForJump[1];
            self.Fx = 0;
        
        self.obj.set_velocity(self.Fx, self.Fy);
        #self.obj.jump_sound.play(1);
        return;

    # 점프 상승중의 버튼 상태를 조사해 반영함.
    def update(self):
        
        if True == self.obj.physx.is_ground :
            self.obj.is_dash = False;
            self.obj.is_down = False;
            #self.obj.is_jump = False;

        if True == KeyInput.g_w :
            self.obj.physx.velocity_y *= 0.9;
            if KeyInput.g_d :
                self.obj.physx.velocity_x = self.obj.force_x;
            elif KeyInput.g_a :
                self.obj.physx.velocity_x = -self.obj.force_x ;
        else:
            self.obj.physx.velocity_y *= 0.05;
            self.obj.physx.is_ground = False;
            self.obj.is_jump = False;
            self.obj.add_queue(IdleStateForPlayer(self.obj));
            temp = self.obj.current_state;
            self.obj.current_state.exit();
            self.obj.current_state = self.obj.state_queue.pop();
            del temp;

        #dash state 로 이동
        #if dash_key :
            #self.obj.add_queue(DashStateForPlayer(self.obj));
            #temp = self.obj.current_state;
            #self.obj.current_state.exit();
            #self.obj.current_state = self.obj.state_queue.pop();
            #del temp;

 


        return;
    
    #def check_jump_timer(self) :
    #    if self.obj.physx.velocity_y < -self.jump_velocity:
    #        self.obj.add_queue(IdleStateForPlayer(self.obj));
    #        temp = self.obj.current_state;
    #        self.obj.current_state.exit();
    #        self.obj.current_state = self.obj.state_queue.pop();
    #        del temp;
    #    return;

    def render(self):
        self.obj.IMGSForJump[self.obj.m_dir].clip_composite_draw(0,0,
                           self.obj.IMG.w,self.obj.IMG.h,0,'',
                           self.obj.transform.tx-GameObject.Cam.camera_offset_x,
                           self.obj.transform.ty-GameObject.Cam.camera_offset_y,
                           );

 

    def exit(self):
        self.obj.jump_trigger = False;
        self.obj.is_jump = False;
        self.obj.physx.is_falling = True;

        print("jump_exit");
        return;




