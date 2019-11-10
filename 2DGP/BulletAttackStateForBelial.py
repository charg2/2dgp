from StateMachine import *;

from Belial import *;
from Graphic import *;
from BelialBullet import *;



attack_speed = 0.15;
max_attack = 20;
frame = 7;
class BulletAttackStateForBelial(StateMachine):
    LOAD:bool = False;
    IMGSForBulletAttack:List[Image] = [];
    IMGSForIdleHandL:List[Image] = [];
    IMGSForIdleHandR:List[Image] = [];
    def __init__(self, belial):
        self.belial = belial;
        
        #self.start_x, self.start_y = belial.transform.tx, belial.transform.ty;
        self.offset_x, self.offset_y = 100, 100;
        self.turn_timer:float = 0.0;
        
        self.timer = 0;
        self.animation_state = 0;
        self.attack_timer = 0;
        self.attack_count = 0;

        self.shot_angle_offset = 0;

        if BulletAttackStateForBelial.LOAD == False:
            
            BulletAttackStateForBelial.IMGSForBulletAttack.append(pico2d.load_image('assets/Monster/Belial/Attack/boss (14).png'));
            BulletAttackStateForBelial.IMGSForBulletAttack.append(pico2d.load_image('assets/Monster/Belial/Attack/boss (15).png'));
            BulletAttackStateForBelial.IMGSForBulletAttack.append(pico2d.load_image('assets/Monster/Belial/Attack/boss (16).png'));
            BulletAttackStateForBelial.IMGSForBulletAttack.append(pico2d.load_image('assets/Monster/Belial/Attack/boss (17).png'));
            BulletAttackStateForBelial.IMGSForBulletAttack.append(pico2d.load_image('assets/Monster/Belial/Attack/boss (18).png'));
            BulletAttackStateForBelial.IMGSForBulletAttack.append(pico2d.load_image('assets/Monster/Belial/Attack/boss (19).png'));
            BulletAttackStateForBelial.IMGSForBulletAttack.append(pico2d.load_image('assets/Monster/Belial/Attack/boss (20).png'));
            

            BulletAttackStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-10.png'));
            BulletAttackStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-11.png'));
            BulletAttackStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-12.png'));
            BulletAttackStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-13.png'));
            BulletAttackStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-14.png'));
            BulletAttackStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-15.png'));
            BulletAttackStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-16.png'));
            BulletAttackStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-17.png'));
            BulletAttackStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-18.png'));
            BulletAttackStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-19.png'));

            BulletAttackStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-0.png'));
            BulletAttackStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-1.png'));
            BulletAttackStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-2.png'));
            BulletAttackStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-3.png'));
            BulletAttackStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-4.png'));
            BulletAttackStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-5.png'));
            BulletAttackStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-6.png'));
            BulletAttackStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-7.png'));
            BulletAttackStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-8.png'));
            BulletAttackStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-9.png'));


            BulletAttackStateForBelial.LOAD = True;

        self.IMG = BulletAttackStateForBelial.IMGSForBulletAttack[0];
        self.base_img = pico2d.load_image('assets/Monster/Belial/Bullet/img (1).png');

        return;


    def update(self):
        from Const import Const;
        time = Timer.get_elapsed_time();   
        self.timer += time;   
        self.turn_timer += time;
        self.attack_timer += time;
        
        if self.turn_timer > 3.0:
            self.turn_timer = 0;

        if self.timer> 0.125:
            self.animation_state= (self.animation_state+1) % frame;
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
        self.base_img.clip_composite_draw(0,0,
                   self.base_img.w ,
                   self.base_img.h ,
                   0,'', 
                   self.belial.transform.tx-GameObject.Cam.camera_offset_x,
                   self.belial.transform.ty-GameObject.Cam.camera_offset_y,
                   );

        BulletAttackStateForBelial.IMGSForBulletAttack[self.animation_state].clip_composite_draw(0,0,
                   BulletAttackStateForBelial.IMGSForBulletAttack[self.animation_state].w,
                   BulletAttackStateForBelial.IMGSForBulletAttack[self.animation_state].h,
                   0,'', 
                   self.belial.transform.tx-GameObject.Cam.camera_offset_x,
                   self.belial.transform.ty-GameObject.Cam.camera_offset_y,
                   );

        BulletAttackStateForBelial.IMGSForIdleHandR[self.animation_state].clip_composite_draw(0,0,
                   BulletAttackStateForBelial.IMGSForIdleHandR[self.animation_state].w,
                   BulletAttackStateForBelial.IMGSForIdleHandR[self.animation_state].h,
                   0,'', 
                   self.belial.transform.tx-GameObject.Cam.camera_offset_x + 550,
                   self.belial.transform.ty-GameObject.Cam.camera_offset_y - 200,
                   );

        BulletAttackStateForBelial.IMGSForIdleHandL[self.animation_state].clip_composite_draw(0,0,
                   BulletAttackStateForBelial.IMGSForIdleHandL[self.animation_state].w,
                   BulletAttackStateForBelial.IMGSForIdleHandL[self.animation_state].h,
                   0,'', 
                   self.belial.transform.tx-GameObject.Cam.camera_offset_x - 500,
                   self.belial.transform.ty-GameObject.Cam.camera_offset_y - 200,
                   );

    def exit(self):
        pass;

    def fire(self):
        tx = self.belial.transform.tx + 50;
        ty = self.belial.transform.ty;

        from FrameWork import FrameWork;
        FrameWork.CurScene.add_projectile(BelialBullet(FrameWork.CurScene, tx , ty, 0.25 + self.shot_angle_offset,1,1, True)); 
        FrameWork.CurScene.add_projectile(BelialBullet(FrameWork.CurScene, tx , ty, 0.75 + self.shot_angle_offset,1,1, True)); 
        FrameWork.CurScene.add_projectile(BelialBullet(FrameWork.CurScene, tx , ty, -0.25+ self.shot_angle_offset,1,1, True)); 
        FrameWork.CurScene.add_projectile(BelialBullet(FrameWork.CurScene, tx , ty, -0.75+ self.shot_angle_offset,1,1, True)); 
        
        self.shot_angle_offset += 0.04;

        pass;







