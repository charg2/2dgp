
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
    PORTAL_SOUND = None;
    LOAD = False;
    def __init__(self, x, y, angle, sx, sy, state, sceneNumber): #direction
        super(Portal,self).__init__(x,y,angle,sx,sy,state);
        self.has_image:bool = True;
        if False == Portal.LOAD:
            Portal.IMGSForPortal.append(pico2d.load_image('assets/Portal/1.png'))
            Portal.IMGSForPortal.append(pico2d.load_image('assets/Portal/2.png'))
            Portal.IMGSForPortal.append(pico2d.load_image('assets/Portal/3.png'))
            Portal.IMGSForPortal.append(pico2d.load_image('assets/Portal/4.png'))

            Portal.IMG = Portal.IMGSForPortal[0];
            Portal.PORTAL_SOUND  = load_wav('assets/por.wav');
            Portal.PORTAL_SOUND.set_volume(50);
            Portal.LOAD = True;

        #콜라이더 크기를 조정해서 실제로 문으로 들어가듯이 만ㄷㄹ어 보자. 
        self.collider = CollisionRect(x + (self.IMG.w // 3), y, 0,self.IMG.h);
        self.tag = Const.TAG_DEFAULT;
        self.scene_number = sceneNumber;

        self.animation_timer = 0;
        self.animation_number = 0;
    
    def render(self):
        Portal.IMG.clip_composite_draw(0,0,
                           Portal.IMG.w,Portal.IMG.h,0,'',
                           self.transform.tx-GameObject.Cam.camera_offset_x,
                           self.transform.ty-GameObject.Cam.camera_offset_y,
                           );
        self.render_debug();

        return;


    def render_debug(self): 
        if self.collider :
            draw_rectangle(*self.collider.get_area_offset(GameObject.Cam.camera_offset_x, GameObject.Cam.camera_offset_y));
        return;

        return;    
    def update(self, time):
        self.update_component(time);
        self.update_animation();
        return;

    def update_animation(self):
        if(self.animation_timer >animate_time):
            self.animation_number = (self.animation_number+1) % animation_frame;
            Portal.IMG = Portal.IMGSForPortal[self.animation_number];
            self.animation_timer = 0;

    def update_component(self,time):
        self.animation_timer += time;
        return;

    def set_scene_number(self,number):
        self.scene_number = number;
        return;

    # 콜라이더를 매우 좌우 구석 끝에 배치 후 방향에 따라 <- -> 키 누르면 다음맵으로 가게 함.
    def on_collision(self,obj):# 이후에 콜라이더 구현후, 콜백으로 실행한다.
        tag = obj.tag;

        if(tag == Const.TAG_PLAYER):
            if KeyInput.g_d or KeyInput.g_a :
                from EffectCutton import EffectCutton;
                from FrameWork import FrameWork as framework;
                Portal.PORTAL_SOUND.play(1);
                framework.CurScene.AddUi(EffectCutton(Const.WIN_WIDTH//2,Const.WIN_HEIGHT//2,0,1,1,True, self.scene_number));
                pass;
        return;
