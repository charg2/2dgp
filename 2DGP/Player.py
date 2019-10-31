from GameObject import *;
from Graphic import *;
from math import*;
from FrameWork import *;
from KeyIO import *;
from Const import *;
from Sword import *;

from IdleState import IdleStateForPlayer;
from RunState import RunStateForPlayer;


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

        self.m_dir = RUN_R;
        self.IMG = Player.IMGSForIdleR[0];
        self.force_x =6; 
        self.force_y =8;
        GameObject.Cam.transform = self.transform;
       
        self.attack_trigger = False;
        self.attack_timer = 0;
        self.attack_key_timer:float = 0.5;

        self.jump_trigger = True;
        self.jump_timer = 0;
        self.jump_key_timer:float = 0.5;
        self.jump_start_y = self.transform.ty;

        ## ability
        #self.hp:int = 0;
        #self.dash_cnt:int = 0;
        self.attack_speed:float = 0.2;

        # animation
        self.animation_numb = 0;
        self.animation_timer = 0.0;
        self.animation_state = RUN_R;

        self.dir = RUN_R; 
        self.last_dir = RUN_R % 2;
        self.current_state = IdleStateForPlayer(self);
        self.tag = 1;


        # equipment
        self.weapons = [];
        self.current_weapon:Sword = Sword( 30, 30, 0.7, 1, 1, True, self );


    def render(self): 
        if( not self.jump_trigger ) : self.current_state.render();
        else : self.renderForJump();

        self.weapon_render();
        return;

    def weapon_render(self):
        self.current_weapon.render();

    def update_basicComponent(self):
        GameObject.Cam.transform = self.previous_transform;
        
        return;

    def update_timer(self,time):
        self.basictimer += time;
        self.animation_timer += time;
        self.jump_key_timer += time;
        self.attack_key_timer += time;
        self.last_dir = (self.dir%2);

        if(self.animation_timer >0.1):
            self.animation_numb = self.animation_numb+1;
            self.animation_timer = 0;

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


    def update(self, time):
        self.update_basicComponent();
        self.handle_keyIO();
        self.forStateMachine();
        self.update_timer(time);
        self.clampingInWindow();

        pass;

    def clampingInWindow(self):
        self.transform.tx = Const.clamp(0, self.transform.tx, GameObject.Cam.map_width-self.IMG.w//16)  
        self.transform.ty = Const.clamp(0, self.transform.ty, GameObject.Cam.map_height-self.IMG.h//8)
        return;

    def on_collision(self, obj):
        pass;
    
    def handle_keyIO(self):
        if KeyInput.g_mouse_x > self.transform.tx: #right
            self.m_dir = Const.direction_R;

        if KeyInput.g_mouse_x < self.transform.tx: #left
            self.m_dir = Const.direction_L;

        if KeyInput.g_d or KeyInput.g_a :
            self.add_queue(RunStateForPlayer(self));

        if self.jump_key_timer >0.8 and ( KeyInput.g_space or KeyInput.g_w ) :
            self.jump_trigger = True;
            self.jump_key_timer =0;
            self.IMG = Player.IMGSForJump[self.m_dir];


        if KeyInput.g_mouse_ldown: #attack
            if  ( self.attack_key_timer > self.attack_speed ) :  #attack
                self.attack_trigger = True;
                self.attack_key_timer = 0.0;
        #else :
        #    pass;


        if KeyInput.g_mouse_rdown : #dash
            pass;

    

    def renderForJump(self):
        Player.IMGSForJump[self.m_dir].clip_composite_draw(0,0,
                           self.IMG.w, self.IMG.h,0,'',
                           self.transform.tx-GameObject.Cam.camera_offset_x,
                           self.transform.ty-GameObject.Cam.camera_offset_y,
                           );

    #def equip_weapon(self, weapon:Weapon):
    #    pass;

