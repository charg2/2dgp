from StateMachine import *;

from Player import *;
from Graphic import *;

from IdleState import *;

animation_frame = 2;
animation_timer = 0.3;

class DeathStateForPlayer(StateMachine):
    def __init__(self, player):
        self.player = player;
        self.Fx ,self.Fy = 0,0;
        self.timer = 0;
        #현재 마우스 방향을얻어서 그방향으로만 죽은 모션 하고 끝.
        if player.m_dir == Const.direction_R : self.imgs = Player.IMGSForDeathR;
        else : self.imgs = Player.IMGSForDeathL;
        self.img = self.imgs[0];

        self.animation_state = 0;
        self.player.set_velocity(self.Fx, self.Fy);
        return;

    def update(self):
        self.timer += Timer.get_elapsed_time();
        #self.player.physx.set_force(0,0);

        if self.timer > animation_timer:
            self.animation_state= (self.animation_state+1)% animation_frame;
            self.timer=0;

        # 리스폰 시간이면 다시 부활...
                
        return;
    
    def render(self):
        from Const import Const;
        Player.imgs[self.animation_state].clip_composite_draw(0,0,
                           Player.img.w,
                           Player.img.h,
                           0,'',
                           self.player.transform.tx-GameObject.Cam.camera_offset_x,
                           self.player.transform.ty-GameObject.Cam.camera_offset_y,
                           );
    def exit(self):
        
        pass;




