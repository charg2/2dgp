from MyTimer import *
from GameObject import *
from CollisionRect import*
from KeyIO import KeyInput as Key;


animation_frame = 1;
increase,decrease = range(2);
class EffectCutton(GameObject):
    LOAD = False;
    IMG = None;
    IMGSForEffect = [];
    def __init__(self,x,y,angle,sx,sy,state,scene_numb):
        super(EffectCutton,self).__init__(x,y,angle,sx,sy,state);
        self.has_image = True;
        if False == EffectCutton.LOAD:
            EffectCutton.IMGSForEffect.append(pico2d.load_image('assets/Effect/Cutton/PointLight00.png'))
            EffectCutton.IMG = EffectCutton.IMGSForEffect[0];

            EffectCutton.LOAD = True;

        self.collider = CollisionRect(x,y-15,EffectCutton.IMG.w/3.5,EffectCutton.IMG.h/3.5);
        self.tag = Const.TAG_DEFAULT;

        self.animation_timer = 0;
        self.animation_number = 0;

        self.alpha_val = 0;
        self.scene_number = scene_numb;

    def render(self):
        EffectCutton.IMG.opacify(self.alpha_val);
        EffectCutton.IMG.clip_composite_draw(0,0,
                           EffectCutton.IMG.w,EffectCutton.IMG.h,0,'',
                           self.transform.tx,
                           self.transform.ty,
                           EffectCutton.IMG.w * 2,EffectCutton.IMG.h * 2
                           );
        return;


        return;    
    def update(self,Time):
        self.update_component(Time);
        self.update_animation();
        return;

    def update_animation(self):
        global increase, decrease;
        if(self.animation_number == increase):
            self.alpha_val +=  self.animation_timer;
            if(self.alpha_val >=1) : 
                self.animation_number = decrease;
        else:
            self.alpha_val -=  self.animation_timer;
            self.animation_timer = 0;
            if(self.alpha_val <= 0.15):
                self.state = False;                      
                self.on_scene_change();

        self.animation_timer = 0;

    def update_component(self,time):
        self.animation_timer += time;
        return;

    def on_scene_change(self):
        #from FrameWork import FrameWork;
        from Scene import Scene;
        Scene.SceneNumber = self.scene_number;
        
        return;

    def on_collision(self,GObj):# 이후에 콜라이더 구현후, 콜백으로 실행한다.
        tag = GObj.tag;
        return;


