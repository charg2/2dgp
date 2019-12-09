
from GameObject import *;
from Graphic import *;
from math import*;
from FrameWork import *;
from KeyIO import *;
from Const import *;

from typing import List;

# 4가지 타입을지원함.
# 제자리에서 애니메이션
# 제자리에서 멈춘 이미지
# 움직이면서 애니메이션
# 움직이면서 멈춘 이미지

STATIC_ANIMATION, STATIC_SPRITE, DYNAMIC_ANIMATION, DYNAMIC_SPRITE = range(4);

class EffectStaticAnimation(GameObject) :
    def __init__(self, owner, tx, ty, animation ,max_frame, interval_time, is_immortal = False):
        super(EffectStaticAnimation, self).__init__(tx, ty, 1, 1, 1, True);
        self.animation_frame        = 0;
        self.animation_max_frame    = max_frame;
        self.interval_time          = interval_time;
        self.animation_timer        = 0;
        self.animation              = animation;
        self.img                    = self.animation[0];
        self.has_image              = True;
        self.owner                  = owner;
        self.tag                    = Const.TAG_EFFECT;
        self.is_immortal            = is_immortal;

    #frame 끝 +1하면 종료.
    def update(self, time):
        self.animation_timer += time;

        if self.animation_timer >= self.interval_time:
            self.animation_timer = 0;
            temp_frame = self.animation_frame + 1 ;
            if self.animation_max_frame == temp_frame :
                if False == self.is_immortal :
                    self.state = False;
                else :
                    self.animation_frame = temp_frame % self.animation_max_frame;
            else:
                self.animation_frame = temp_frame;
            
    def render(self):
        self.animation[self.animation_frame].composite_draw( 0, "", self.transform.tx - GameObject.Cam.camera_offset_x, self.transform.ty - GameObject.Cam.camera_offset_y, self.img.w, self.img.h);
        #print("{0}".format(self.animation_frame));

class EffectStaticSprite(GameObject) :
    def __init__(self, owner, tx, ty, sprite, end_time, lambda_func = None):
        super(EffectStaticSprite, self).__init__(tx, ty, 1, 1, 1, True);
        self.has_image      = True;
        self.tag            = Const.TAG_EFFECT;
        self.end_time       = end_time;
        self.end_timer      = 0;
        self.img            = sprite;
        self.owner          = owner;
        self.lambda_func    = lambda_func;

    def update(self, time):
        self.end_timer += time;
        if self.end_timer >= self.end_time:
            #self.end_timer = 0;
            self.state = False;
            #print("삭제");
            if None != self.lambda_func : #and self.state :
                self.lambda_func(self.img);
                pass;

    def render(self):
        self.img.composite_draw( 0, "", self.transform.tx - GameObject.Cam.camera_offset_x, self.transform.ty - GameObject.Cam.camera_offset_y, self.img.w, self.img.h);

class EffectStaticSprite2(GameObject) :
    def __init__(self, owner, tx, ty, sprite, end_time, lambda_func = None):
        super(EffectStaticSprite2, self).__init__(tx, ty, 1, 1, 1, True);
        self.has_image      = True;
        self.tag            = Const.TAG_EFFECT;
        self.end_time       = end_time;
        self.end_timer      = 0;
        self.img            = sprite;
        self.owner          = owner;
        self.lambda_func    = lambda_func;

    def update(self, time):
        self.end_timer += time;
        if self.end_timer >= self.end_time:
            #self.end_timer = 0;
            self.state = False;
            #print("삭제");
            if None != self.lambda_func : #and self.state :
                self.lambda_func(self.img);
                pass;

    def render(self):
        self.img.draw_to_origin( self.transform.tx, self.transform.ty, self.img.w, self.img.h);



    
