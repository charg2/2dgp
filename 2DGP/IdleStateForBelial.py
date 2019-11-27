from StateMachine import *;

from Belial import *;
from Graphic import *;

from BulletAttackStateForBelial import *;
from SwordAttackStateForBelial  import *;
from LaserAttackStateForBelial  import *;


frame = 10;
attack_table = { 0: SwordAttackStateForBelial , 1 : BulletAttackStateForBelial, 2 : LaserAttackStateForBelial };

class IdleStateForBelial(StateMachine):
    LOAD:bool = False;
    IMGSForIdle:List[Image] = [];
    IMGSForIdleHandL:List[Image] = [];
    IMGSForIdleHandR:List[Image] = [];
    def __init__(self, belial):
        self.belial = belial;
        
        #self.start_x, self.start_y = belial.transform.tx, belial.transform.ty;
        self.offset_x, self.offset_y = 100, 100;
        self.turn_timer:float = 0.0;
        
        self.timer = 0;
        self.animation_state = 0;

        self.attack_trigger:bool = False;
        self.idx = 0;
        if IdleStateForBelial.LOAD == False:
            
            IdleStateForBelial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (1).png'));
            IdleStateForBelial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (2).png'));
            IdleStateForBelial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (3).png'));
            IdleStateForBelial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (4).png'));
            IdleStateForBelial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (5).png'));
            IdleStateForBelial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (6).png'));
            IdleStateForBelial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (7).png'));
            IdleStateForBelial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (8).png'));
            IdleStateForBelial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (9).png'));
            IdleStateForBelial.IMGSForIdle.append(pico2d.load_image('assets/Monster/Belial/Idle/boss (10).png'));
    
            IdleStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-10.png'));
            IdleStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-11.png'));
            IdleStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-12.png'));
            IdleStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-13.png'));
            IdleStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-14.png'));
            IdleStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-15.png'));
            IdleStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-16.png'));
            IdleStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-17.png'));
            IdleStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-18.png'));
            IdleStateForBelial.IMGSForIdleHandL.append(pico2d.load_image('assets/Monster/Belial/Idle/HandL/IMG-19.png'));

            IdleStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-0.png'));
            IdleStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-1.png'));
            IdleStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-2.png'));
            IdleStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-3.png'));
            IdleStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-4.png'));
            IdleStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-5.png'));
            IdleStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-6.png'));
            IdleStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-7.png'));
            IdleStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-8.png'));
            IdleStateForBelial.IMGSForIdleHandR.append(pico2d.load_image('assets/Monster/Belial/Idle/HandR/IMG-9.png'));






            IdleStateForBelial.LOAD = True;

        self.IMG = IdleStateForBelial.IMGSForIdle[0];

        return;


    def update(self):
        from Const import Const;
        time = Timer.get_elapsed_time();   
        self.timer += time;   
        self.turn_timer += time;
        
        if self.turn_timer > 3.0:
            self.turn_timer = 0;
            import random;
            #self.idx = random.randint(0,1);
            self.idx = (self.idx + 1) % 2;
            #attack_table[idx](slef.belial)
            self.belial.add_queue(attack_table[self.idx](self.belial));
            #self.belial.add_queue(SwordAttackStateForBelial(self.belial));
            temp = self.belial.current_state;
            self.belial.current_state.exit();
            self.belial.current_state = self.belial.state_queue.pop();
            del temp;

        if self.timer>0.125:
            self.animation_state= (self.animation_state+1) % frame;
            self.timer=0;


        

        return;
    

    def render(self):

        IdleStateForBelial.IMGSForIdle[self.animation_state].clip_composite_draw(0,0,
                   IdleStateForBelial.IMGSForIdle[self.animation_state].w,
                   IdleStateForBelial.IMGSForIdle[self.animation_state].h,
                   0,'', 
                   self.belial.transform.tx-GameObject.Cam.camera_offset_x ,
                   self.belial.transform.ty-GameObject.Cam.camera_offset_y,
                   );

        IdleStateForBelial.IMGSForIdleHandR[self.animation_state].clip_composite_draw(0,0,
                   IdleStateForBelial.IMGSForIdleHandR[self.animation_state].w,
                   IdleStateForBelial.IMGSForIdleHandR[self.animation_state].h,
                   0,'', 
                   self.belial.transform.tx-GameObject.Cam.camera_offset_x + 550,
                   self.belial.transform.ty-GameObject.Cam.camera_offset_y - 200,
                   );

        IdleStateForBelial.IMGSForIdleHandL[self.animation_state].clip_composite_draw(0,0,
                   IdleStateForBelial.IMGSForIdleHandL[self.animation_state].w,
                   IdleStateForBelial.IMGSForIdleHandL[self.animation_state].h,
                   0,'', 
                   self.belial.transform.tx-GameObject.Cam.camera_offset_x - 500,
                   self.belial.transform.ty-GameObject.Cam.camera_offset_y - 200,
                   );

    def exit(self):
        pass;





