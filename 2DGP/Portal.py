
from MyTimer import *;
from GameObject import *;
from CollisionRect import*;
from KeyIO import KeyInput;

from typing import List;

animate_time = 0.142 # 2초에 애니메이션 1바퀴.
animation_frame = 4;
class Portal(GameObject):
    IMG:Image = None;
    IMGSForPortal:List[Image] = [];
    def __init__(self, x, y, angle, sx, sy, state, sceneNumber):
        super(Portal,self).__init__(x,y,angle,sx,sy,state);
        self.has_image:bool = True;
        if None == Portal.IMG:
            Portal.IMGSForPortal.append(pico2d.load_image('assets/Portal/1.png'))
            Portal.IMGSForPortal.append(pico2d.load_image('assets/Portal/2.png'))
            Portal.IMGSForPortal.append(pico2d.load_image('assets/Portal/3.png'))
            Portal.IMGSForPortal.append(pico2d.load_image('assets/Portal/4.png'))

            Portal.IMG = Portal.IMGSForPortal[0];

        self.collider = CollisionRect(x,y-15,self.IMG.w/3.5,self.IMG.h/3.5);
        self.tag = Const.tag_default;
        self.scene_number = sceneNumber;

        self.animation_timer = 0;
        self.animation_number = 0;
    
    def render(self):
        Portal.IMG.clip_composite_draw(0,0,
                           Portal.IMG.w,Portal.IMG.h,0,'',
                           self.transform.tx-GameObject.Cam.camera_offset_x,
                           self.transform.ty-GameObject.Cam.camera_offset_y,
                           );
        

        return;

        return;    
    def update(self, time):
        self.update_basicComponent(time);
        self.animation();
        return;

    def animation(self):
        global animate_time;
        global animation_frame;
        if(self.animation_timer >animate_time):
            self.animation_number = (self.animation_number+1)%animation_frame
            Portal.IMG = Portal.IMGSForPortal[self.animation_number]
            self.animation_timer = 0;
            #print(self.animation_number);

    def update_basicComponent(self,time):
        self.animation_timer += time;
        return;

    def set_scene_number(self,number):
        self.scene_number = number;
        return;


    # 콜라이더를 매우 좌우 구석 끝에 배치 후 방향에 따라 <- -> 키 누르면 다음맵으로 가게 함.
    def on_collision(self,obj):# 이후에 콜라이더 구현후, 콜백으로 실행한다.
        tag = obj.get_tag();

        if(tag == Const.Const.TAG_PLAYER):
            if(KeyInput.g_up_arrow):
                pass;
        return;
