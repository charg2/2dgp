
from GameObject import *;
from Graphic import *;
from math import*;
from FrameWork import *;
from KeyIO import *;
from Const import *;
from CollisionRect import*;

from Player import Player;

from IdleStateForBelial import *;

from typing import List;

#2~3가지 패턴을 가지고 있음
# 일정시간 마다 공격을 하며
# 공격 상태에서 쿨ㅇ타임이 아닌 공격을 해야 하는데
# 그렇게 쿨타임이 길어야 하는지 모르겟으니 그냥 쿨타임 없이 랜덤으로 패턴 공격.

attack_speed = 3;
RUN_L, RUN_R, IDLE_R, IDLE_L = range(4);
frame = 10;
class Belial(GameObject):
    LOAD:bool = False;
    IMGSForIdle:List[Image] = [];
    FieldOfView:float = 0.0;
    IMG:Image = None;
    def __init__(self, x, y, angle, sx, sy, state):
        super(Belial, self).__init__(x, y, angle, sx, sy, state);
        self.has_image = True;
        if Belial.LOAD == False:
            Belial.IMG = pico2d.load_image('assets/Monster/Belial/Idle/boss (1).png');

            Belial.FieldOfView = Const.BANSHEE_FIELD_OF_VIEW;
            Belial.LOAD = True;
        
        self.name = "Belial";

        self.force_x =6; 
        self.force_y =8;

        # attack
        # bullet 공격의 경우 .1초 간격으로 4방향 30발 
        # laser 공격의 경우 3번 연속 레이저
        # 검 날리기 인데 이건 아직 고려 중.
        self.attack_trigger:bool = False;
        self.attack_timer:float = 0;
        self.attack_key_timer:float = 0.5;

        # animation
        self.animation_numb = 0;
        self.animation_timer = 0.0;
        self.animation_state = RUN_L;

        self.current_state = IdleStateForBelial(self);
        self.dir = Const.direction_L; 
        self.last_dir = RUN_L % 2;
        self.tag = Const.TAG_MONSTER;

        self.collider:Collision = CollisionRect(x,y, Belial.IMG.w // 2, Belial.IMG.h // 2);

        #self.bullets:List[BelialBullet] = [];

    def render(self): 
        self.current_state.render();


    def render_debug(self): 
        if self.collider :
            from Graphic import GraphicLib;
            GraphicLib.DebugImg1.draw(self.previous_transform.tx - GameObject.Cam.camera_offset_x, self.previous_transform.ty - GameObject.Cam.camera_offset_y);    

        return;

    def update(self, time):
        # 플레이어와의 거리 체크 해서 어느 근처 거리면 다가가기 시작.
        self.update_component();
        self.forStateMachine();
        self.update_timer(time);
        self.clampingInWindow();
        pass;

    def update_timer(self,time):
        self.basictimer += time;
        self.animation_timer += time;
        self.attack_key_timer += time;

        if(self.animation_timer >0.1):
            self.animation_numb = (self.animation_numb+1 ) % frame;
            self.animation_timer = 0;

        #if False == self.attack_trigger :
        
        #self.attack_timer += time;

        #if(self.attack_timer > attack_speed):
        #    self.fire();
        #    self.attack_timer = 0;
        


        return;
    

    def forStateMachine(self):
        self.current_state.update();

        if len(self.state_queue) > 0:
            temp = self.current_state;
            self.current_state.exit();
            self.current_state = self.state_queue.pop();
            del temp;

    def update_component(self):
        self.previous_transform = self.transform;
        #self.collider.cx, self.collider.cy = self.transform.tx, self.transform.ty;
        return;

    def clampingInWindow(self):
        self.transform.tx = Const.clamp(0, self.transform.tx, GameObject.Cam.map_width-Belial.IMG.w//16)  
        self.transform.ty = Const.clamp(0, self.transform.ty, GameObject.Cam.map_height-Belial.IMG.h//8)
        return;

    def on_collision(self, obj):
        #print("Belial.py {0}-{1}".format(self.tag, obj.tag));
        pass;


