from StateMachine import *;

from Belial import *;
from Graphic import *;
from BelialLaser import BelialLaser as bl;

#손의 x좌표는 바뀌지 않고 y좌표만 플레이어를 따라가서 레이저를 쏨. 일정시간 동안. LR 은 랜덤인듯
attack_speed = 0.15;
max_attack = 7;
body_frame = 7;
hand_frame = 10;
laser_frame = 7;

LASER_L, LASER_R = range(2);

class LaserAttackStateForBelial(StateMachine):
    LOAD:bool = False;
    IMGSForLaserAttack          :List[Image] = [];
    IMGSForLaserAttackHandL     :List[Image] = [];
    IMGSForLaserAttackHandR     :List[Image] = [];
    IMGSForLaserL               :List[Image] = [];
    IMGSForLaserR               :List[Image] = [];

    def __init__(self, belial):
        self.belial = belial;
        
        self.offset_x, self.offset_y = 100, 100;
        
        self.timer = 0;
        self.animation_state = 0;
        self.animation_hand_state =0;
        self.attack_timer = 0;
        self.attack_count = 0;
        
        from random import randint;
        self.type = randint(0,2);

        if LaserAttackStateForBelial.LOAD == False:
            
            LaserAttackStateForBelial.IMGSForLaserAttack.append(pico2d.load_image('assets/Monster/Belial/Attack/boss (14).png'));
            LaserAttackStateForBelial.IMGSForLaserAttack.append(pico2d.load_image('assets/Monster/Belial/Attack/boss (15).png'));
            LaserAttackStateForBelial.IMGSForLaserAttack.append(pico2d.load_image('assets/Monster/Belial/Attack/boss (16).png'));
            LaserAttackStateForBelial.IMGSForLaserAttack.append(pico2d.load_image('assets/Monster/Belial/Attack/boss (17).png'));
            LaserAttackStateForBelial.IMGSForLaserAttack.append(pico2d.load_image('assets/Monster/Belial/Attack/boss (18).png'));
            LaserAttackStateForBelial.IMGSForLaserAttack.append(pico2d.load_image('assets/Monster/Belial/Attack/boss (19).png'));
            LaserAttackStateForBelial.IMGSForLaserAttack.append(pico2d.load_image('assets/Monster/Belial/Attack/boss (20).png'));
            
            LaserAttackStateForBelial.IMGSForLaserAttackHandL.append(pico2d.load_image('assets/Monster/Belial/Attack/HandL/IMG-30.png'));
            LaserAttackStateForBelial.IMGSForLaserAttackHandL.append(pico2d.load_image('assets/Monster/Belial/Attack/HandL/IMG-31.png'));
            LaserAttackStateForBelial.IMGSForLaserAttackHandL.append(pico2d.load_image('assets/Monster/Belial/Attack/HandL/IMG-32.png'));
            LaserAttackStateForBelial.IMGSForLaserAttackHandL.append(pico2d.load_image('assets/Monster/Belial/Attack/HandL/IMG-33.png'));
            LaserAttackStateForBelial.IMGSForLaserAttackHandL.append(pico2d.load_image('assets/Monster/Belial/Attack/HandL/IMG-34.png'));
            LaserAttackStateForBelial.IMGSForLaserAttackHandL.append(pico2d.load_image('assets/Monster/Belial/Attack/HandL/IMG-35.png'));
            LaserAttackStateForBelial.IMGSForLaserAttackHandL.append(pico2d.load_image('assets/Monster/Belial/Attack/HandL/IMG-36.png'));
            LaserAttackStateForBelial.IMGSForLaserAttackHandL.append(pico2d.load_image('assets/Monster/Belial/Attack/HandL/IMG-37.png'));
            LaserAttackStateForBelial.IMGSForLaserAttackHandL.append(pico2d.load_image('assets/Monster/Belial/Attack/HandL/IMG-38.png'));
            LaserAttackStateForBelial.IMGSForLaserAttackHandL.append(pico2d.load_image('assets/Monster/Belial/Attack/HandL/IMG-39.png'));

            LaserAttackStateForBelial.IMGSForLaserAttackHandR.append(pico2d.load_image('assets/Monster/Belial/Attack/HandR/IMG-20.png'));
            LaserAttackStateForBelial.IMGSForLaserAttackHandR.append(pico2d.load_image('assets/Monster/Belial/Attack/HandR/IMG-21.png'));
            LaserAttackStateForBelial.IMGSForLaserAttackHandR.append(pico2d.load_image('assets/Monster/Belial/Attack/HandR/IMG-22.png'));
            LaserAttackStateForBelial.IMGSForLaserAttackHandR.append(pico2d.load_image('assets/Monster/Belial/Attack/HandR/IMG-23.png'));
            LaserAttackStateForBelial.IMGSForLaserAttackHandR.append(pico2d.load_image('assets/Monster/Belial/Attack/HandR/IMG-24.png'));
            LaserAttackStateForBelial.IMGSForLaserAttackHandR.append(pico2d.load_image('assets/Monster/Belial/Attack/HandR/IMG-25.png'));
            LaserAttackStateForBelial.IMGSForLaserAttackHandR.append(pico2d.load_image('assets/Monster/Belial/Attack/HandR/IMG-26.png'));
            LaserAttackStateForBelial.IMGSForLaserAttackHandR.append(pico2d.load_image('assets/Monster/Belial/Attack/HandR/IMG-27.png'));
            LaserAttackStateForBelial.IMGSForLaserAttackHandR.append(pico2d.load_image('assets/Monster/Belial/Attack/HandR/IMG-28.png'));
            LaserAttackStateForBelial.IMGSForLaserAttackHandR.append(pico2d.load_image('assets/Monster/Belial/Attack/HandR/IMG-29.png'));

            #LaserAttackStateForBelial.IMGSForLaserL.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserL/IMG-0.png'));
            #LaserAttackStateForBelial.IMGSForLaserL.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserL/IMG-1.png'));
            #LaserAttackStateForBelial.IMGSForLaserL.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserL/IMG-2.png'));
            #LaserAttackStateForBelial.IMGSForLaserL.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserL/IMG-3.png'));
            #LaserAttackStateForBelial.IMGSForLaserL.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserL/IMG-4.png'));
            #LaserAttackStateForBelial.IMGSForLaserL.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserL/IMG-5.png'));
            #LaserAttackStateForBelial.IMGSForLaserL.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserL/IMG-6.png'));

            #LaserAttackStateForBelial.IMGSForLaserR.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserR/IMG-0.png'));
            #LaserAttackStateForBelial.IMGSForLaserR.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserR/IMG-1.png'));
            #LaserAttackStateForBelial.IMGSForLaserR.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserR/IMG-2.png'));
            #LaserAttackStateForBelial.IMGSForLaserR.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserR/IMG-3.png'));
            #LaserAttackStateForBelial.IMGSForLaserR.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserR/IMG-4.png'));
            #LaserAttackStateForBelial.IMGSForLaserR.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserR/IMG-5.png'));
            #LaserAttackStateForBelial.IMGSForLaserR.append(pico2d.load_image('assets/Monster/Belial/Attack/LaserR/IMG-6.png'));
            
            LaserAttackStateForBelial.LOAD = True;

        self.IMG = LaserAttackStateForBelial.IMGSForLaserAttack[0];
        self.base_img = pico2d.load_image('assets/Monster/Belial/Laser/img (1).png');

        return;


    def update(self):
        from Const import Const;
        time = Timer.get_elapsed_time();   

        self.timer += time;   
        self.attack_timer += time;
        

        if self.timer> 0.125:
            self.animation_state= (self.animation_state+1) % body_frame;
            self.animation_hand_state= (self.animation_state+1) % hand_frame;
            self.timer=0;
        
        if(self.attack_timer > attack_speed):
            self.fire();
            self.attack_timer = 0;
            self.attack_count +=1;

            if self.attack_count >= max_attack:
                from IdleStateForBelial import IdleStateForBelial;
                self.belial.add_queue(IdleStateForBelial(self.belial));
                temp = self.belial.current_state;
                self.belial.current_state.exit();
                self.belial.current_state = self.belial.state_queue.pop();
                del temp;
        
        return;
    

    def render(self):
        cam_offset_x = self.belial.transform.tx- GameObject.Cam.camera_offset_x;
        cam_offset_y = self.belial.transform.ty-GameObject.Cam.camera_offset_y;

        hand_width = BulletAttackStateForBelial.IMGSForLaserAttackHandR[self.animation_hand_state].w;
        hand_height = BulletAttackStateForBelial.IMGSForLaserAttackHandR[self.animation_hand_state].h;


        self.base_img.clip_composite_draw(0,0,
                   self.base_img.w,
                   self.base_img.h,
                   0,'', 
                   cam_offset_x,
                   cam_offset_y,
                   );

        LaserAttackStateForBelial.IMGSForLaserAttack[self.animation_state].clip_composite_draw(0,0,
                   LaserAttackStateForBelial.IMGSForLaserAttack[self.animation_state].w,
                   LaserAttackStateForBelial.IMGSForLaserAttack[self.animation_state].h,
                   0,'', 
                   cam_offset_x,
                   cam_offset_y,
                   );

        BulletAttackStateForBelial.IMGSForLaserAttackHandR[self.animation_hand_state].clip_composite_draw(0,0,
                   hand_width,
                   hand_height,
                   0,'', 
                   cam_offset_x + 550,
                   cam_offset_y - 200,
                   );

        BulletAttackStateForBelial.IMGSForLaserAttackHandL[self.animation_hand_state].clip_composite_draw(0,0,
                   hand_width,
                   hand_height,
                   0,'', 
                   cam_offset_x - 500,
                   cam_offset_y - 200,
                   );

    def exit(self):
        pass;


    def fire(self):
        tx = self.belial.transform.tx + self.offset_shoh_x;
        ty = self.belial.transform.ty + 200;
        #angle = 0.0;
        
        px = Player.MyPlayer.transform.tx;
        py = Player.MyPlayer.transform.ty + 100;
        angle = Const.calc_radian( tx, ty, px, py) / math.pi;


        # x는 고정 두개 랜덤으로 
        # y는 플에이어의 위치를 따라감.


        self.offset_shoh_x += 100;
        from FrameWork import FrameWork;
        FrameWork.CurScene.add_projectile(bl(self, START_X + 1000, py ,0,1,1, True));        
        #self.AddMonsterObject(bl(self, START_X + 1000, START_Y + 400 ,0,1,1, True));        
        pass;








