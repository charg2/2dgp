from StateMachine import *;

from Graphic import *;

from IdleState import *;
from Player import *;

animation_frame = 2;
animation_timer = 0.3;

class DeathStateForPlayer(StateMachine):
    LOAD = False;
    IMGSForL= [];
    IMGSForR= [];
    def __init__(self, player):
        if False == DeathStateForPlayer.LOAD :
            DeathStateForPlayer.IMGSForL.append(pico2d.load_image('assets/Player/Death/L (1).png'));
            DeathStateForPlayer.IMGSForL.append(pico2d.load_image('assets/Player/Death/L (2).png'));

            DeathStateForPlayer.IMGSForR.append(pico2d.load_image('assets/Player/Death/R (1).png'));
            DeathStateForPlayer.IMGSForR.append(pico2d.load_image('assets/Player/Death/R (2).png'));
            DeathStateForPlayer.LOAD = True;

        self.player = player;
        self.Fx ,self.Fy = 0,0;
        player.is_death = True;

        self.timer = 0;
        #현재 마우스 방향을얻어서 그방향으로만 죽은 모션 하고 끝.
        self.img = None;
        if player.m_dir == Const.direction_R : 
            self.imgs = DeathStateForPlayer.IMGSForR;
        else : 
            self.imgs = DeathStateForPlayer.IMGSForL;


        self.img = self.imgs[0];

        self.animation_state = 0;
        self.player.set_velocity(0, 0);
        return;

    def update(self):
        self.timer += Timer.get_elapsed_time();
        #self.player.physx.set_force(0,0);

        if self.timer > animation_timer:
            self.animation_state= (self.animation_state+1)% animation_frame;
            self.img = self.imgs[self.animation_state];
            self.timer=0;

        # 리스폰 시간이면 다시 부활...
        return;
    
    def render(self):
        from Const import Const;
        self.img.clip_composite_draw(0,0,
                           self.img.w,
                           self.img.h,
                           0,'',
                           self.player.transform.tx-GameObject.Cam.camera_offset_x,
                           self.player.transform.ty-GameObject.Cam.camera_offset_y,
                           );
    def exit(self):
        self.player.is_death = False;

        #self.player.set_grivity(True);
        #self.player.turnoff_invincibility();
        pass;




