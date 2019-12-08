from GameObject import *;
from Graphic import *;
from math import*;
from FrameWork import *;
from CollisionRect import*;
from KeyIO import *;
from Const import *;

from IdleState import IdleStateForPlayer;
from RunState import RunStateForPlayer;
from JumpState import JumpStateForPlayer;
from DashState import DashStateForPlayer;
from DeathState import DeathStateForPlayer;

from Katana import *;
from Gun import *;

from typing import List;

# component
from HitComponent import *;

RUN_L, RUN_R, IDLE_R, IDLE_L = range(4);
DASH_CHARGE_TIME  = 1.25;
HIT_RECOVERY_TIME = 0.3;
ALPHA_VALUE = 70;
class Player(GameObject):
    LOAD:bool                   = False;
    HIT_SOUND:Wav               = None;
    IMGSForIdleL:List[Image]    = [];
    IMGSForIdleR:List[Image]    = [];
    IMGSForRunL:List[Image]     = [];
    IMGSForRunR:List[Image]     = [];
    IMGSForJump:List[Image]     = []; # dash랑 공유
    IMGSForDeathL:List[Image]   = [];
    IMGSForDeathR:List[Image]   = [];

    IMGSForIdleLAlpha:List[Image]    = [];
    IMGSForIdleRAlpha:List[Image]    = [];
    IMGSForRunLAlpha:List[Image]     = [];
    IMGSForRunRAlpha:List[Image]     = [];
    IMGSForJumpAlpha:List[Image]     = [];
    IMGSForDeathLAlpha:List[Image]   = [];
    IMGSForDeathRAlpha:List[Image]   = [];

    MyPlayer:GameObject = None;

    def __init__(self, x, y, angle, sx, sy, state):
        super(Player, self).__init__(x, y, angle, sx, sy, state);
        self.has_image:bool = True;

        if Player.LOAD == False:
            import FrameWork;
            for idx in range(1, 5 + 1):
                Player.IMGSForIdleR.append( pico2d.load_image( 'assets/Player/Idle/R ({0}).png'.format( str(idx) ) ) );
                Player.IMGSForIdleL.append( pico2d.load_image( 'assets/Player/Idle/L ({0}).png'.format( str(idx) ) ) );
                Player.IMGSForIdleRAlpha.append( pico2d.load_image( 'assets/Player/Idle/R ({0}).png'.format( str(idx) ) ) );
                Player.IMGSForIdleLAlpha.append( pico2d.load_image( 'assets/Player/Idle/L ({0}).png'.format( str(idx) ) ) );

            for idx in range(1, 9 + 1):
                Player.IMGSForRunR.append(pico2d.load_image('assets/Player/Run/R ({0}).png'.format( str(idx) ) ) );
                Player.IMGSForRunL.append(pico2d.load_image('assets/Player/Run/L ({0}).png'.format( str(idx) ) ) );
                Player.IMGSForRunRAlpha.append(pico2d.load_image('assets/Player/Run/R ({0}).png'.format( str(idx) ) ) );
                Player.IMGSForRunLAlpha.append(pico2d.load_image('assets/Player/Run/L ({0}).png'.format( str(idx) ) ) );

            Player.IMGSForJump.append(pico2d.load_image('assets/Player/Jump/L (1).png'));
            Player.IMGSForJump.append(pico2d.load_image('assets/Player/Jump/R (1).png'));
            Player.IMGSForJumpAlpha.append(pico2d.load_image('assets/Player/Jump/L (1).png'));
            Player.IMGSForJumpAlpha.append(pico2d.load_image('assets/Player/Jump/R (1).png'));

            for idx in range(1, 2 + 1):
                Player.IMGSForDeathL.append(pico2d.load_image('assets/Player/Death/L ({0}).png'.format( str(idx) )));
                Player.IMGSForDeathR.append(pico2d.load_image('assets/Player/Death/R ({0}).png'.format( str(idx) )));
                Player.IMGSForDeathLAlpha.append( pico2d.load_image('assets/Player/Death/L ({0}).png'.format( str(idx) )));
                Player.IMGSForDeathRAlpha.append(pico2d.load_image('assets/Player/Death/R ({0}).png'.format( str(idx) )));

            for img in Player.IMGSForIdleRAlpha:
                img.opacify(ALPHA_VALUE);
            for img in Player.IMGSForIdleLAlpha:
                img.opacify(ALPHA_VALUE);
            for img in Player.IMGSForRunRAlpha:
                img.opacify(ALPHA_VALUE);
            for img in Player.IMGSForRunLAlpha:
                img.opacify(ALPHA_VALUE);
            for img in Player.IMGSForJumpAlpha:
                img.opacify(ALPHA_VALUE);
            for img in Player.IMGSForDeathLAlpha:
                img.opacify(ALPHA_VALUE);
            for img in Player.IMGSForDeathRAlpha:
                img.opacify(ALPHA_VALUE);

            Player.HIT_SOUND = pico2d.load_wav('assets/Player/hit.wav');
            Player.HIT_SOUND.set_volume(50);
            # singletone
            Player.MyPlayer = self;

            Player.LOAD = True;

        #self.colliderForObstacle = CollisionRect(x,y+interpolation_collision_y,10,25);
        self.name   :str = "Hero";
        self.IMG    :Image = Player.IMGSForIdleR[0];

        #self.move_velocity  :int = 10;
        #self.force_x        :int = 10;
        #self.force_y        :int = 5;

        self.transform.angle = 1;
        self.collider:Collision = CollisionRect(x ,y, self.IMG.w // 3, self.IMG.h // 2);
        self.has_collider = True;
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

        self.dash_key_timer         :float  = 0;
        self.dash_charge_timer      :float  = 0;
        self.dash_count             :int    = 2;
        self.max_dash_count         :int    = 2;
        self.dash_trigger           :bool   = True;

        self.is_jump    :bool = False;
        self.is_dash    :bool = False;
        self.is_run     :bool = False;
        self.is_down    :bool = False;
        self.is_death   :bool = False;

        ## ability
        #self.dash_cnt:int = 0;
        self.current_hp     :int = 100;
        self.max_hp         :int = 100;
        self.attack_speed   :float = 0.2;
        self.current_coin   :int = 0;

        # animation code
        self.animation_timer :float = 0.0;
        self.animation_state :int = RUN_R;
        self.m_dir           :int = Const.direction_R;
        self.dir             :int = RUN_R; 
        self.last_dir        :int = RUN_R % 2;
        self.tag             :int = Const.TAG_PLAYER;
        self.current_state = IdleStateForPlayer(self);


        # weapon
        self.weapons = [];
        self.weapons.append(Katana( 30, 30, 0.7, 1, 1, True, self ));
        self.weapons.append(Gun( 30, 30, 0.7, 1, 1, True, self ));
        self.current_weapon = self.weapons[1];

        self.attack_speed_offset     = 0.0;
        self.max_attack_speed_offset = 0.3;

        self.set_grivity(True);
        self.set_acceleration_of_gravity(7);
        
        #hit component
        self.hit_component = HitComponent(self, HIT_RECOVERY_TIME);

    def update(self, time):
        self.handle_keyIO();
        self.forStateMachine(time);
        self.Physx(time);
        self.update_component(time);
        self.update_timer(time);
        self.current_weapon.update(time);
        self.clampingInWindow();

        self.physx.is_ground = False;

        return;

    def render(self): 
        self.current_state.render();
        self.weapon_render();
        return;


    def render_debug(self): 
        if self.collider :
            draw_rectangle(*self.collider.get_area_offset(GameObject.Cam.camera_offset_x, GameObject.Cam.camera_offset_y));
        return;


    def weapon_render(self):
        self.current_weapon.render();

    def update_component(self, time):
        self.previous_transform = self.transform;
        GameObject.Cam.transform = self.previous_transform;
        #GameObject.Cam.transform = self.transform;
        
        #if True == self.has_collider:
        self.collider.cx, self.collider.cy = self.transform.tx, self.transform.ty;

        self.hit_component.update(time);
        return;

    def update_timer(self,time):
        self.basictimer += time;
        self.jump_key_timer += time;
        self.attack_key_timer += time;
        self.skill_key_timer += time;

        if self.dash_count < self.max_dash_count :
            self.dash_charge_timer += time;
            if DASH_CHARGE_TIME <= self.dash_charge_timer:
                self.dash_count += 1;
                self.dash_charge_timer = 0;
        return;
    

    def forStateMachine(self, time):
        self.current_state.update(time);

        if len(self.state_queue) > 0:
            temp = self.current_state;
            self.current_state.exit();
            self.current_state = self.state_queue.pop();
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
        if self.is_death == False:
            self.check_state();

        return;

    #idle에서 다른 상태로 변화하는걸 감지한다.
  
    def check_state(self):
        if self.current_hp <= 0:
            self.add_queue(DeathStateForPlayer(self));
        else:
            if ( False == self.is_dash ) and (False == self.is_jump) and (False == self.is_run) :
                if True == KeyInput.g_w : #and False == self.has_grivity() :
                    self.add_queue(JumpStateForPlayer(self));
                    self.is_jump = True;
                if ( KeyInput.g_a or KeyInput.g_d ) :
                        self.add_queue(RunStateForPlayer(self));
                # 대시. # 상태에서 다른 상태이동은 그상태에서 정의 현재 아이들 상태에서만 가능. 
                if 0 < self.dash_count and False == self.is_dash:
                        if True == KeyInput.g_mouse_rdown :
                            #if  ( False == self.is_dash ) and ((True == self.dash_trigger) and 
                            self.add_queue(DashStateForPlayer(self));

    #각 상태별로 velocity 값이 지정되어 이슴.
    def Physx(self, time):
        grivity_offset_y = 0; 
        #if True == self.has_grivity() :
        if False == self.physx.is_ground :
            #if True == self.physx.is_falling:
            #    grivity_offset_y = self.physx.acceleration_of_gravity * 1.1; 
            #else:
                grivity_offset_y = self.physx.acceleration_of_gravity; 
        
        
        v_x = self.physx.velocity_x * time;#* math.cos(self.transform.angle) ;
        v_y = self.physx.velocity_y * time;#* math.sin(self.transform.angle) ;

        #self.transform.set_position(self.physx.velocity_x, self.physx.velocity_y - grivity_offset_y);
        self.transform.set_position(v_x, v_y - grivity_offset_y);

        #if False == self.physx.is_ground:
            #grivity_offset_y = -5;
        #self.transform.set_position(self.physx.velocity_x, self.physx.velocity_y + grivity_offset_y);       
        return;
    
    def on_collision(self, obj):
        if True == self.has_collider:
            tag = obj.tag;

            if Const.TAG_TERRAIN == tag:
                    if self.physx.velocity_y <=0 :
                        self.physx.set_falling(False);
                        self.transform = self.previous_transform;
            
        return;

    def calc_hp(self, damage):
        if False == self.is_death and self.hit_component.can_hitted() :
            self.hit_component.hit();
            Player.HIT_SOUND.play(1);
            self.current_hp -= damage;
            if self.current_hp < 0:
                self.current_hp = 0;


# for weapon
    def swap_weapon(self):
        self.current_weapon = (self.current_weapon + 1 )% 2;
        self.current_weapon = self.weapons[self.current_weapon];
        pass;

