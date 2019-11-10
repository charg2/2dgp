from GameObject import *;
from Graphic import *;
from math import*;
from FrameWork import *;
from CollisionRect import*;
from KeyIO import *;
from Const import *;
from Katana import *;

from IdleState import IdleStateForPlayer;
from RunState import RunStateForPlayer;
from JumpState import JumpStateForPlayer;
from DashState import DashStateForPlayer;

from typing import List;


RUN_L, RUN_R, IDLE_R, IDLE_L = range(4);
class Player(GameObject):
    LOAD:bool = False;

    IMGSForIdleL:List[Image] = [];
    IMGSForIdleR:List[Image] = [];
    IMGSForRunL:List[Image] = [];
    IMGSForRunR:List[Image] = [];

    IMGSForJump:List[Image] = []; # dash랑 공유

    IMGSForDeathL:List[Image] = [];
    IMGSForDeathR:List[Image] = [];
    DebugImg:Image = None;
    DebugImg1:Image = None;

    MyPlayer:GameObject = None;

    def __init__(self, x, y, angle, sx, sy, state):
        super(Player, self).__init__(x, y, angle, sx, sy, state);
        self.has_image:bool = True;
        if Player.LOAD == False:
            import FrameWork;
            Player.IMGSForIdleR.append(pico2d.load_image('assets/Player/Idle/R (1).png'));
            Player.IMGSForIdleR.append(pico2d.load_image('assets/Player/Idle/R (2).png'));
            Player.IMGSForIdleR.append(pico2d.load_image('assets/Player/Idle/R (3).png'));
            Player.IMGSForIdleR.append(pico2d.load_image('assets/Player/Idle/R (4).png'));
            Player.IMGSForIdleR.append(pico2d.load_image('assets/Player/Idle/R (5).png'));

            Player.IMGSForIdleL.append(pico2d.load_image('assets/Player/Idle/L (1).png'));
            Player.IMGSForIdleL.append(pico2d.load_image('assets/Player/Idle/L (2).png'));
            Player.IMGSForIdleL.append(pico2d.load_image('assets/Player/Idle/L (3).png'));
            Player.IMGSForIdleL.append(pico2d.load_image('assets/Player/Idle/L (4).png'));
            Player.IMGSForIdleL.append(pico2d.load_image('assets/Player/Idle/L (5).png'));

            Player.IMGSForRunR.append(pico2d.load_image('assets/Player/Run/R (1).png'));
            Player.IMGSForRunR.append(pico2d.load_image('assets/Player/Run/R (2).png'));
            Player.IMGSForRunR.append(pico2d.load_image('assets/Player/Run/R (3).png'));
            Player.IMGSForRunR.append(pico2d.load_image('assets/Player/Run/R (4).png'));
            Player.IMGSForRunR.append(pico2d.load_image('assets/Player/Run/R (5).png'));
            Player.IMGSForRunR.append(pico2d.load_image('assets/Player/Run/R (6).png'));
            Player.IMGSForRunR.append(pico2d.load_image('assets/Player/Run/R (7).png'));
            Player.IMGSForRunR.append(pico2d.load_image('assets/Player/Run/R (8).png'));
            Player.IMGSForRunR.append(pico2d.load_image('assets/Player/Run/R (9).png'));

            Player.IMGSForRunL.append(pico2d.load_image('assets/Player/Run/L (1).png'));
            Player.IMGSForRunL.append(pico2d.load_image('assets/Player/Run/L (2).png'));
            Player.IMGSForRunL.append(pico2d.load_image('assets/Player/Run/L (3).png'));
            Player.IMGSForRunL.append(pico2d.load_image('assets/Player/Run/L (4).png'));
            Player.IMGSForRunL.append(pico2d.load_image('assets/Player/Run/L (5).png'));
            Player.IMGSForRunR.append(pico2d.load_image('assets/Player/Run/L (6).png'));
            Player.IMGSForRunR.append(pico2d.load_image('assets/Player/Run/L (7).png'));
            Player.IMGSForRunR.append(pico2d.load_image('assets/Player/Run/L (8).png'));
            Player.IMGSForRunR.append(pico2d.load_image('assets/Player/Run/L (9).png'));

            Player.IMGSForJump.append(pico2d.load_image('assets/Player/Jump/L (1).png'));
            Player.IMGSForJump.append(pico2d.load_image('assets/Player/Jump/R (1).png'));

            Player.IMGSForDeathL.append(pico2d.load_image('assets/Player/Death/L (1).png'));
            Player.IMGSForDeathL.append(pico2d.load_image('assets/Player/Death/L (2).png'));

            Player.IMGSForDeathR.append(pico2d.load_image('assets/Player/Death/R (1).png'));
            Player.IMGSForDeathR.append(pico2d.load_image('assets/Player/Death/R (2).png'));

            # singletone
            Player.MyPlayer = self;

            Player.LOAD = True;

        #self.colliderForObstacle = CollisionRect(x,y+interpolation_collision_y,10,25);
        self.name   :str = "Hero";
        self.IMG    :Image = Player.IMGSForIdleR[0];

        self.move_velocity  :int = 10;
        self.force_x        :int = 10;
        self.force_y        :int = 5;

        self.transform.angle = 1;
        self.collider:Collision = CollisionRect(x,y, self.IMG.w // 2, self.IMG.h // 2);
        GameObject.Cam.transform = self.transform;
       
        self.jump_trigger:bool = True;
        self.jump_timer:float = 0;
        self.jump_key_timer:float = 0.2;
        self.jump_start_y = self.transform.ty;

        self.attack_trigger:bool = False;
        self.attack_timer:float = 0;
        self.attack_key_timer:float = 0.5;
        
        self.skill_trigger  :bool = False;
        self.skill_key_timer:float = 0;
        self.skill_timer    :float = 0;

        self.dash_key_timer :float = 0;
        self.dash_charge_timer     :float = 0;
        self.dash_count     :int = 2;
        self.dash_trigger   :bool = True;

        self.current_hp = 100;
        self.max_hp = 100;

        self.is_jump:bool = False;
        self.is_dash:bool = False;
        self.is_run :bool = False;
        self.is_down:bool = False;

        ## ability
        #self.hp:int = 0;
        #self.dash_cnt:int = 0;
        self.attack_speed:float = 0.2;

        # animation code
        self.animation_timer:float = 0.0;
        self.animation_state:int = RUN_R;

        self.m_dir          :int = Const.direction_R;
        self.dir            :int = RUN_R; 
        self.last_dir       :int = RUN_R % 2;
        self.tag            :int = Const.TAG_PLAYER;
        self.current_state = IdleStateForPlayer(self);

        # equipment
        self.weapons = [];
        self.current_weapon:Katana = Katana( 30, 30, 0.7, 1, 1, True, self );

        self.set_grivity(True);
        self.set_acceleration_of_gravity(7);

    """
    method
    """
    def update(self, time):
        self.update_component();
        self.handle_keyIO();
        self.forStateMachine();

        self.Physx(time);
        self.update_timer(time);
        self.clampingInWindow();
        return;

    def render(self): 
        self.current_state.render();
        self.weapon_render();
        return;

    def render_debug(self): 
        if self.collider :
            from Graphic import GraphicLib;
            GraphicLib.DebugImg1.draw(self.collider.cx - GameObject.Cam.camera_offset_x, self.collider.cy- GameObject.Cam.camera_offset_y);    
        return;


    def weapon_render(self):
        self.current_weapon.render();

    def update_component(self):
        self.previous_transform = self.transform;
        self.collider.cx, self.collider.cy = self.transform.tx, self.transform.ty;
        
        GameObject.Cam.transform = self.previous_transform;
        return;

    def update_timer(self,time):
        self.basictimer += time;
        self.jump_key_timer += time;
        self.attack_key_timer += time;
        self.skill_key_timer += time;
        #self.last_dir = (self.dir%2);

        if self.dash_count < Const.MAX_DASH_COUNT :
            self.dash_charge_timer += time;
            if Const.DASH_CHARGE_TIME <= self.dash_charge_timer:
                self.dash_count += 1;

#        if self.attack_trigger :
#            self.attack_timer += time;
            
#        if(self.attack_timer > self.attack_speed):
#            self.attack_trigger = False;
#            self.attack_timer = 0;
##################
#        if self.skill_trigger :
#            self.skill_timer += time;
        return;
    

    def forStateMachine(self):
        self.current_state.update();

        if len(self.state_queue) > 0:
            temp = self.current_state;
            self.current_state.exit();
            self.current_state = self.state_queue.pop();
            #print(type(self.current_state));
            del temp;

        #self.physx.set_force(self.physx.force_x, self.physx.force_y);
        return;


    def clampingInWindow(self):
        self.transform.tx = Const.clamp(0, self.transform.tx, GameObject.Cam.map_width-self.IMG.w//16);  
        self.transform.ty = Const.clamp(0, self.transform.ty, GameObject.Cam.map_height-self.IMG.h // 10);
        return;

    
    def handle_keyIO(self):
        if KeyInput.g_mouse_x > ( self.transform.tx - GameObject.Cam.camera_offset_x) : #right
            self.m_dir = Const.direction_R;
        if KeyInput.g_mouse_x < ( self.transform.tx - GameObject.Cam.camera_offset_x): #left
            self.m_dir = Const.direction_L;
        # 런. # 공격. # 스킬.
        self.check_action();

        
        return;

    #idle에서 다른 상태로 변화하는걸 감지한다.
  
    def check_action(self):
        if ( False == self.is_dash ) and (False == self.is_jump) and (False == self.is_run) :
        #if ( False == self.is_dash ) and ( False == self.is_jump ) and (False == self.is_run) :
            if True == KeyInput.g_w  :
                print("Player.py JumpState");
                self.add_queue(JumpStateForPlayer(self));
                self.is_jump = True;

            #if (False == self.is_jump) and ( False == self.is_run ) and ( KeyInput.g_a or KeyInput.g_d ) : 
            if ( KeyInput.g_a or KeyInput.g_d ) : 
                print("Player.py RunState");
                self.add_queue(RunStateForPlayer(self));

        # 대시. # 상태에서 다른 상태이동은 그상태에서 정의 현재 아이들 상태에서만 가능. 
            #if ( False == self.is_dash ) and ( False == self.is_jump ) and (False == self.is_run) :
            if 0 < self.dash_count and False == self.is_dash:
                if True == KeyInput.g_mouse_rdown :
                    #if  ( False == self.is_dash ) and ((True == self.dash_trigger) and 
                    print("Player.py DashState");
                    self.add_queue(DashStateForPlayer(self));


    def Physx(self,time):
        grivity_offset_y = 0; 
        if True == self.has_grivity() :
            #if True == self.physx.is_falling:
            #    grivity_offset_y = self.physx.acceleration_of_gravity * 1.1; 
            #else:
                grivity_offset_y = self.physx.acceleration_of_gravity; 
        
        
        #v_x = self.physx.velocity_x * self.transform.angle;
        #v_y = self.physx.velocity_y * self.transform.angle;

        #radian = self.transform.angle * math.pi;
        
        v_x = self.physx.velocity_x #* math.cos(self.transform.angle);
        v_y = self.physx.velocity_y #* math.sin(self.transform.angle);

        #self.transform.set_position(self.physx.velocity_x, self.physx.velocity_y - grivity_offset_y);
        self.transform.set_position(v_x, v_y - grivity_offset_y);

        #if False == self.physx.is_ground:
            #grivity_offset_y = -5;
        #self.transform.set_position(self.physx.velocity_x, self.physx.velocity_y + grivity_offset_y);       
        return;
    
    def on_collision(self, obj):
        tag = obj.tag;

        if Const.TAG_TERRAIN == tag:
                if self.physx.velocity_y <=0 :
                    self.physx.set_falling(False);
                    self.transform = self.previous_transform;
        return;
