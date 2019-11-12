
from StateMachine import *;

from Belial import *;
from Graphic import *;
from BelialSword import *;



attack_speed = 0.15;
sword_spwan_speed = 0.15;
max_attack_count = 6;
animaion_upeating_time = 0.125;
frame = 10;
class SwordAttackStateForBelial(StateMachine):
    LOAD:bool = False;
    IMGSForIdle:List[Image] = [];
    IMGSForIdleHandL:List[Image] = [];
    IMGSForIdleHandR:List[Image] = [];

    def __init__(self, belial):
        self.belial = belial;
        
        #self.start_x, self.start_y = belial.transform.tx, belial.transform.ty;
        self.offset_x, self.offset_y = 100, 100;
        self.timer = 0;
        self.animation_state = 0;
        self.attack_timer = 0;
        self.attack_count = 0;
        self.shot_angle_offset = 0;
        self.offset_shoh_x = -200;
        if SwordAttackStateForBelial.LOAD == False:
            
            SwordAttackStateForBelial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (1).png'));
            SwordAttackStateForBelial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (2).png'));
            SwordAttackStateForBelial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (3).png'));
            SwordAttackStateForBelial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (4).png'));
            SwordAttackStateForBelial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (5).png'));
            SwordAttackStateForBelial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (6).png'));
            SwordAttackStateForBelial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (7).png'));
            SwordAttackStateForBelial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (8).png'));
            SwordAttackStateForBelial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (9).png'));
            SwordAttackStateForBelial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (10).png'));
    

            SwordAttackStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-10.png'));
            SwordAttackStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-11.png'));
            SwordAttackStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-12.png'));
            SwordAttackStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-13.png'));
            SwordAttackStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-14.png'));
            SwordAttackStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-15.png'));
            SwordAttackStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-16.png'));
            SwordAttackStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-17.png'));
            SwordAttackStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-18.png'));
            SwordAttackStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-19.png'));

            SwordAttackStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-0.png'));
            SwordAttackStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-1.png'));
            SwordAttackStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-2.png'));
            SwordAttackStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-3.png'));
            SwordAttackStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-4.png'));
            SwordAttackStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-5.png'));
            SwordAttackStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-6.png'));
            SwordAttackStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-7.png'));
            SwordAttackStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-8.png'));
            SwordAttackStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-9.png'));


            SwordAttackStateForBelial.LOAD = True;

        self.IMG = SwordAttackStateForBelial.IMGSForIdle[0];
        self.base_img = pico2d.load_image('assets/Monster/Belial/Bullet/img (1).png');

        return;


    def update(self):
        from Const import Const;
        time = Timer.get_elapsed_time();   
        self.timer += time;   
        self.attack_timer += time;
        
        if self.timer> animaion_upeating_time:
            self.animation_state= (self.animation_state+1) % frame;
            self.timer=0;
        
        if self.attack_timer > attack_speed :
            if self.attack_count < max_attack_count:
                self.fire();
                self.attack_timer = 0;
                self.attack_count +=1;
            else:
                from IdleStateForBelial import IdleStateForBelial;
                self.belial.add_queue(IdleStateForBelial(self.belial));
                temp = self.belial.current_state;
                self.belial.current_state.exit();
                self.belial.current_state = self.belial.state_queue.pop();
                del temp;
        
        return;
    

    def render(self):
        self.base_img.clip_composite_draw(0,0,
                   self.base_img.w ,
                   self.base_img.h ,
                   0,'', 
                   self.belial.transform.tx-GameObject.Cam.camera_offset_x,
                   self.belial.transform.ty-GameObject.Cam.camera_offset_y,
                   );

        SwordAttackStateForBelial.IMGSForIdle[self.animation_state].clip_composite_draw(0,0,
                   SwordAttackStateForBelial.IMGSForIdle[self.animation_state].w,
                   SwordAttackStateForBelial.IMGSForIdle[self.animation_state].h,
                   0,'', 
                   self.belial.transform.tx-GameObject.Cam.camera_offset_x,
                   self.belial.transform.ty-GameObject.Cam.camera_offset_y,
                   );

        SwordAttackStateForBelial.IMGSForIdleHandR[self.animation_state].clip_composite_draw(0,0,
                   SwordAttackStateForBelial.IMGSForIdleHandR[self.animation_state].w,
                   SwordAttackStateForBelial.IMGSForIdleHandR[self.animation_state].h,
                   0,'', 
                   self.belial.transform.tx-GameObject.Cam.camera_offset_x + 550,
                   self.belial.transform.ty-GameObject.Cam.camera_offset_y - 200,
                   );

        SwordAttackStateForBelial.IMGSForIdleHandL[self.animation_state].clip_composite_draw(0,0,
                   SwordAttackStateForBelial.IMGSForIdleHandL[self.animation_state].w,
                   SwordAttackStateForBelial.IMGSForIdleHandL[self.animation_state].h,
                   0,'', 
                   self.belial.transform.tx-GameObject.Cam.camera_offset_x - 500,
                   self.belial.transform.ty-GameObject.Cam.camera_offset_y - 200,
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

        from FrameWork import FrameWork;
        FrameWork.CurScene.add_projectile(BelialSword(FrameWork.CurScene, tx, ty, angle ,1,1, True)); 
        
        self.offset_shoh_x += 100;

        pass;







