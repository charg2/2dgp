
from StateMachine import *;
from IdleState import*;
from RunState import*;
from Const import *;
from Player import *;

class DashStateForPlayer(StateMachine):
    animation_state =0;
    timer = 0;

    def __init__(self,gobj):
        self.obj = gobj;
        self.fx = 0;
        self.fy = 0;
        self.is_dash = True;

        if  Const.direction_R == self.obj.m_dir :
            self.obj.last_dir = Const.direction_R;
            self.obj.dir = Const.direction_R;
            from Player import Player;
            self.obj.IMG = Player.IMGSForJump[0];
            self.fx = self.obj.force_x;
            self.fy = self.obj.force_x;

        if Const.direction_L == self.obj.m_dir :
            self.obj.last_dir = Const.direction_L;
            self.obj.dir = Const.direction_L;
            from Player import Player;
            self.obj.IMG = Player.IMGSForJump[0];
            self.fx = -self.obj.force_x;
            self.fy = -self.obj.force_x;
        return;


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
        self.obj.IMGSForJump[self.obj.m_dir].clip_composite_draw(0,0,
                           self.obj.IMG.w,self.obj.IMG.h,0,'',
                           self.obj.transform.tx-GameObject.Cam.camera_offset_x,
                           self.obj.transform.ty-GameObject.Cam.camera_offset_y,
                           );

    # 대시하면서 생기는 이펙트..
    def setAnimation(self):
        return;

    def exit(self):
        return;



