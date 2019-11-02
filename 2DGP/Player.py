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


RUN_L, RUN_R, IDLE_R, IDLE_L = range(4);
class Player(GameObject):
    LOAD = False;

    IMGSForIdleL = [];
    IMGSForIdleR = [];
    IMGSForRunL = [];
    IMGSForRunR = [];

    IMGSForJump = []; # dash랑 공유

    IMGSForDeathL = [];
    IMGSForDeathR = [];
    DebugImg:pico2d.Image = None;
    DebugImg1:pico2d.Image = None;

    def __init__(self, x, y, angle, sx, sy, state):
        super(Player, self).__init__(x, y, angle, sx, sy, state);
        self.has_image = True;
        if Player.LOAD == False:
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

            Player.LOAD = True;

        #self.colliderForObstacle = CollisionRect(x,y+interpolation_collision_y,10,25);
        self.name:str = "Hero";
        self.IMG = Player.IMGSForIdleR[0];
        #self.force_x:int = 2600; # cm / s
        self.force_x:int = 7; # cm / s
        #self.force_y:int = 2350;
        self.force_y:int = 5;
        self.collider:Collision = CollisionRect(x,y, self.IMG.w // 2, self.IMG.h // 2);
        GameObject.Cam.transform = self.transform;
       
        self.jump_trigger:bool = True;
        self.jump_timer:float = 0;
        self.jump_key_timer:float = 0.2;
        self.jump_start_y = self.transform.ty;

        self.attack_trigger:bool = False;
        self.attack_timer:float = 0;
        self.attack_key_timer:float = 0.5;


        ## ability
        #self.hp:int = 0;
        #self.dash_cnt:int = 0;
        self.attack_speed:float = 0.2;

        # animation code
        self.animation_timer:float = 0.0;
        self.animation_state:int = RUN_R;

        self.m_dir:int = Const.direction_R;
        self.dir:int = RUN_R; 
        self.last_dir:int = RUN_R % 2;
        self.current_state = IdleStateForPlayer(self);
        self.tag:int = Const.TAG_PLAYER;

        # equipment
        self.weapons = [];
        self.current_weapon:Katana = Katana( 30, 30, 0.7, 1, 1, True, self );

    """
    method
    """
    def update(self, time):
        self.update_component();
        self.handle_keyIO();
        self.forStateMachine();
        self.update_timer(time);
        self.clampingInWindow();
        return;

    def render(self): 
        if (False == self.jump_trigger) : self.current_state.render();
        #if (False == self.physx.is_falling()) : self.current_state.render();
        else : self.renderForJump();

        self.weapon_render();
        return;

    def render_debug(self): 
        if self.collider :
            from Graphic import GraphicLib;
            GraphicLib.DebugImg1.draw(self.collider.cx - GameObject.Cam.camera_offset_x, self.collider.cy- GameObject.Cam.camera_offset_y);    
            #GraphicLib.DebugImg1.draw(self.transform.tx, self.transform.ty);    

        return;

    #def renderForJump(self):
    #    Player.IMGSForJump[self.last_dir].clip_composite_draw(0,0,
    #                       self.IMG.w,self.IMG.h,0,'',
    #                       self.transform.tx-GameObject.Cam.camera_offset_x,
    #                       self.transform.ty-GameObject.Cam.camera_offset_y,
    #                       );
    #    return;

    def weapon_render(self):
        self.current_weapon.render();

    def update_component(self):
        self.previous_transform = self.transform;
        self.collider.cx, self.collider.cy = self.transform.tx, self.transform.ty;
        
        GameObject.Cam.transform = self.previous_transform;
        return;

    #def Physx(self, time): 
    #    #self.physx.CalcVelocity(Time);
    #    self.transform.set_position(self.physx.velocity_x,self.physx.velocity_y);       
    #    return;

    def update_timer(self,time):
        self.basictimer += time;
        self.animation_timer += time;
        self.jump_key_timer += time;
        self.attack_key_timer += time;
        self.last_dir = (self.dir%2);

        if(True == self.jump_trigger):
            self.jump_timer += time;
            
        if(self.jump_timer > 0.19):
            self.jump_trigger = False;
            self.jump_timer = 0;

        if self.attack_trigger :
            self.attack_timer += time;
            
        if(self.attack_timer > self.attack_speed):
            self.attack_trigger = False;
            self.attack_timer = 0;
        return;
    

    def forStateMachine(self):
        self.current_state.update();

        if len(self.state_queue) > 0:
            temp = self.current_state;
            self.current_state.exit();
            self.current_state = self.state_queue.pop();
            del temp;
        return;


    def clampingInWindow(self):
        self.transform.tx = Const.clamp(0, self.transform.tx, GameObject.Cam.map_width-self.IMG.w//16);  
        self.transform.ty = Const.clamp(0, self.transform.ty, GameObject.Cam.map_height-self.IMG.h//8);
        return;

    
    def handle_keyIO(self):
        if KeyInput.g_mouse_x > ( self.transform.tx - GameObject.Cam.camera_offset_x) : #right
            self.m_dir = Const.direction_R;
        if KeyInput.g_mouse_x < (self.transform.tx - GameObject.Cam.camera_offset_x): #left
            self.m_dir = Const.direction_L;

        if self.jump_key_timer >0.8 and ( KeyInput.g_space or KeyInput.g_w ) :
            self.jump_trigger = True;
            self.jump_key_timer =0;
            self.add_queue(JumpStateForPlayer(self));
            #self.IMG = Player.IMGSForJump[self.m_dir];

        if False == self.jump_trigger and (KeyInput.g_d or KeyInput.g_a) :
            self.add_queue(RunStateForPlayer(self));


        if KeyInput.g_mouse_ldown: #attack
            if  ( self.attack_key_timer > self.attack_speed ) :  #attack
                self.attack_trigger = True;
                self.attack_key_timer = 0.0;

        if KeyInput.g_mouse_rdown : #dash
            pass;

    

    def renderForJump(self):
        Player.IMGSForJump[self.m_dir].clip_composite_draw(0,0,
                           self.IMG.w, self.IMG.h,0,'',
                           self.transform.tx-GameObject.Cam.camera_offset_x,
                           self.transform.ty-GameObject.Cam.camera_offset_y
                           );



    def on_collision(self, obj):
        tag = obj.tag;

        if Const.TAG_TERRAIN == tag:
                if self.physx.velocity_y <=0 :
                    self.physx.set_falling(False);
                    self.transform = self.previous_transform;
        return;
