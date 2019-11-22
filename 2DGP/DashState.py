
from StateMachine import *;
from IdleState import*;
from RunState import*;
from Const import *;
from Player import *;
from KeyIO import *;


FORCE_X, FORCE_Y = 500, 500;

class DashStateForPlayer(StateMachine):
    animation_state =0;
    timer = 0;

    def __init__(self,gobj):
        self.obj = gobj;
  
        self.obj.is_dash = True;

        self.target_x = KeyInput.g_mouse_x;
        self.target_y = Const.WIN_HEIGHT - KeyInput.g_mouse_y - 1;

        self.before_angle = self.obj.transform.angle;
        self.dash_timer = 0;
        self.obj.dash_count -= 1;
        self.before_vx, self.before_vy = self.obj.physx.velocity_x, self.obj.physx.velocity_y;


        self.radian = ( Const.calc_radian(self.obj.transform.tx - GameObject.Cam.camera_offset_x, self.obj.transform.ty - GameObject.Cam.camera_offset_y, self.target_x, self.target_y) );
        self.obj.physx.velocity_x = FORCE_X * math.sin(self.radian);
        self.obj.physx.velocity_y = FORCE_Y * math.cos(self.radian);

        #print("{0} - {1} - {2} - {3} = {4} ".format(self.obj.transform.tx - GameObject.Cam.camera_offset_x, self.obj.transform.ty - GameObject.Cam.camera_offset_y, self.target_x, self.target_y, self.radian));
      
        if  Const.direction_R == self.obj.m_dir :
            self.obj.last_dir = Const.direction_R;
            self.obj.dir = Const.direction_R;
            from Player import Player;


        if Const.direction_L == self.obj.m_dir :
            self.obj.last_dir = Const.direction_L;
            self.obj.dir = Const.direction_L;
            from Player import Player;


        return;


    def update(self):
        self.setAnimation();
        elapsed_time = Timer.get_elapsed_time();     
        
        self.timer += elapsed_time;
        
        self.obj.physx.velocity_x *= 1.3;
        self.obj.physx.velocity_y *= 1.3;


        if self.timer > 0.2 :
            print("Dashstate.py 76 ");
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

    # 대시하면서 생기는 이펙트..
    def setAnimation(self):
        return;

    def exit(self):
        self.obj.transform.angle = self.before_angle;
        self.obj.is_dash = False;
        self.obj.physx.velocity_x = self.before_vx;
        self.obj.physx.velocity_y =  self.before_vy;
        
        return;



