
from StateMachine import *;
from IdleState import*;
from RunState import*;
from Const import *;
from Player import *;

from Effect import *;


FORCE_X = 500; 
FORCE_Y = 3000;

class JumpStateForPlayer(StateMachine):
    animation_state =0;
    timer           = 0;
    JUMP_SOUND      = None;
    EFFECT_ANIMAION = [];
    def __init__(self,player):
        if None == JumpStateForPlayer.JUMP_SOUND :
            JumpStateForPlayer.JUMP_SOUND = load_wav('assets/Player/Jump/jump.wav');
            for idx in range(0, 4 + 1):
                JumpStateForPlayer.EFFECT_ANIMAION.append( pico2d.load_image( 'assets/Player/JumpEffect/IMG-{0}.png'.format( str(idx) ) ) );

        self.obj = player;
        #gobj.set_grivity(True);

        self.Fy = FORCE_Y;
        #self.Fy = player.force_y + 30;

        self.Fx = 0;
        self.obj.is_jump = True;
        self.jump_timer = 0;
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

        JumpStateForPlayer.JUMP_SOUND.play(1);

        self.obj.set_velocity(self.Fx, self.Fy);

        from FrameWork import FrameWork;
        FrameWork.CurScene.add_effect( EffectStaticAnimation(  self
                                                             , self.obj.transform.tx
                                                             , self.obj.transform.ty
                                                             , JumpStateForPlayer.EFFECT_ANIMAION
                                                             , len(JumpStateForPlayer.EFFECT_ANIMAION)
                                                             , 0.125
                                                             ) ); 
        return;

    # 점프 상승중의 버튼 상태를 조사해 반영함.
    def update(self, time):
        self.jump_timer += time;
        if True == self.obj.physx.is_ground :
            self.obj.is_dash = False;
            self.obj.is_down = False;
            #self.obj.is_jump = False;

        if True == KeyInput.g_w :
                self.obj.physx.velocity_y *= 0.9;
                if KeyInput.g_d :
                    self.obj.physx.velocity_x = FORCE_X;
                elif KeyInput.g_a :
                    self.obj.physx.velocity_x = -FORCE_X ;

        #if self.jump_timer >= 0.016:
        else:
                #self.jump_timer = 0;
            #else:
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
                #temp = self.obj.current_state;aaaaa
                #self.obj.current_state.exit();
                #self.obj.current_state = self.obj.state_queue.pop();
                #del temp;


        return;
    


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

        #print("jump_exit");
        return;




