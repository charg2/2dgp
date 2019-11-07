from StateMachine import *;

from Belial import *;
from Graphic import *;

#from AttackStateForBelial import *;

attack_speed = 0.125;
frame = 7;
class BulletAttackStateForBelial(StateMachine):
    LOAD:bool = False;
    IMGSForBulletAttack:List[Image] = [];
    def __init__(self, belial):
        self.belial = belial;
        
        #self.start_x, self.start_y = belial.transform.tx, belial.transform.ty;
        self.offset_x, self.offset_y = 100, 100;
        self.turn_timer:float = 0.0;
        
        self.timer = 0;
        self.animation_state = 0;

        if BulletAttackStateForBelial.LOAD == False:
            
            BulletAttackStateForBelial.IMGSForBulletAttack.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (14).png'));
            BulletAttackStateForBelial.IMGSForBulletAttack.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (15).png'));
            BulletAttackStateForBelial.IMGSForBulletAttack.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (16).png'));
            BulletAttackStateForBelial.IMGSForBulletAttack.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (17).png'));
            BulletAttackStateForBelial.IMGSForBulletAttack.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (18).png'));
            BulletAttackStateForBelial.IMGSForBulletAttack.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (19).png'));
            BulletAttackStateForBelial.IMGSForBulletAttack.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (20).png'));
    
            BulletAttackStateForBelial.LOAD = True;

        self.IMG = BulletAttackStateForBelial.IMGSForBulletAttack[0];
        self.base_img = BulletAttackStateForBelial.IMGSForBulletAttack[0];

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
        
        return;
    

    def render(self):
        self.base_img.clip_composite_draw(0,0,
                   self.base_img.w,
                   self.base_img.h,
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


    def exit(self):
        pass;

    def fire(self):
        tx = self.transform.tx;
        ty = self.transform.ty;

        from FrameWork import FrameWork;

        FrameWork.CurScene.add_projectile(BelialBullet(FrameWork.CurScene, tx, ty, 0.25,1,1, True)); 
        FrameWork.CurScene.add_projectile(BelialBullet(FrameWork.CurScene, tx, ty, 0.5,1,1, True)); 
        FrameWork.CurScene.add_projectile(BelialBullet(FrameWork.CurScene, tx, ty, 0.75,1,1, True)); 
        FrameWork.CurScene.add_projectile(BelialBullet(FrameWork.CurScene, tx, ty, 1,1,1, True)); 
        FrameWork.CurScene.add_projectile(BelialBullet(FrameWork.CurScene, tx, ty, -0.25,1,1, True)); 
        FrameWork.CurScene.add_projectile(BelialBullet(FrameWork.CurScene, tx, ty, -0.5,1,1, True)); 
        FrameWork.CurScene.add_projectile(BelialBullet(FrameWork.CurScene, tx, ty, -0.75,1,1, True)); 

        pass;







