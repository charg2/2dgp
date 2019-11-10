
from StateMachine import *;
from IdleState import*;
from RunState import*;
from Const import *;
from Player import *;
from KeyIO import *;


class DashStateForPlayer(StateMachine):
    animation_state =0;
    timer = 0;

    def __init__(self,gobj):
        self.obj = gobj;
        self.fx = 0;
        self.fy = 0;
        self.obj.is_dash = True;

        self.target_x = KeyInput.g_mouse_x;
        self.target_y = Const.WIN_HEIGHT - KeyInput.g_mouse_y - 1;

        self.before_angle = self.obj.transform.angle;
        self.dash_timer = 0;
        self.before_vx, self.before_vy = self.obj.physx.velocity_x, self.obj.physx.velocity_y;

        if self.target_x > (self.obj.transform.tx - GameObject.Cam.camera_offset_x) :
            self.obj.physx.velocity_x = 5;
        elif self.target_x < (self.obj.transform.tx - GameObject.Cam.camera_offset_x) :
            self.obj.physx.velocity_x = -5;
        else :
            self.obj.physx.velocity_x = 0;
            


        if self.target_y < (self.obj.transform.ty - GameObject.Cam.camera_offset_y) :
            self.obj.physx.velocity_y = -5;
        else:
            self.obj.physx.velocity_y = 5;

        self.obj.transform.angle = ( Const.calc_degree(self.obj.transform.tx - GameObject.Cam.camera_offset_x, self.obj.transform.ty - GameObject.Cam.camera_offset_y, self.target_x, self.target_y) ) / 180;
        t = ( Const.calc_degree(self.obj.transform.tx - GameObject.Cam.camera_offset_x, self.obj.transform.ty - GameObject.Cam.camera_offset_y, self.target_x, self.target_y) ) / 180;

        #print("DashState.py 24.");
        print(self.obj.transform.angle);
        print("{0} - {1} - {2} - {3} = {4} ".format(self.obj.transform.tx - GameObject.Cam.camera_offset_x, self.obj.transform.ty - GameObject.Cam.camera_offset_y, self.target_x, self.target_y, t));
      
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
        elapsed_time = Timer.get_elapsed_time();     
        
        self.timer += elapsed_time;
        
        self.obj.physx.velocity_x *= 1.13;
        self.obj.physx.velocity_y *= 1.13;

        #self.obj.physx.velocity_x * math.cos(self.obj.transform.angle);
        #self.obj.physx.velocity_y * math.sin(self.obj.transform.angle);

        if self.timer > 0.4 :
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



