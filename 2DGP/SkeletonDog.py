from GameObject import *;
from Graphic import *;
from math import*;
from FrameWork import *;
from KeyIO import *;
from Const import *;
from CollisionRect import*;
from BehaviorTree import *;
from Player import Player;
#from IdleStateForSkeletonDog import *; Behavior Tree 로 해보장
import random;

#component
from HitComponent import *;

#ui
from HPBarForMonster import *;

from typing import List;

# 플레이어에게 접근 하는 패턴만 추가하면 완성.
attack_speed = 3;
RUN_L, RUN_R, IDLE_R, IDLE_L = range(4);
RUN, IDLE = range(2);
DAMAGE = 7;

hit_recovery_time = 0.2;
class SkeletonDog(GameObject):
    LOAD        :bool = False;
    UNIQUE_ID   :int = 0;
    IMGSForIdleL:List[Image] = [];
    IMGSForIdleR:List[Image] = [];
    IMGSForRunL :List[Image] = [];
    IMGSForRunR :List[Image] = [];
    FieldOfView :float = 0.0;
    
    def __init__(self, x, y, angle, sx, sy, state):
        super(SkeletonDog, self).__init__(x, y, angle, sx, sy, state);
        self.has_image = True;
        if SkeletonDog.LOAD == False:
            for idx in range(1, 5 + 1):
                SkeletonDog.IMGSForIdleR.append( pico2d.load_image( 'assets/Monster/SkeletonDog/Idle/R ({0}).png'.format( str(idx) ) ) );
                SkeletonDog.IMGSForIdleL.append( pico2d.load_image( 'assets/Monster/SkeletonDog/Idle/L ({0}).png'.format( str(idx) ) ) );

            for idx in range(1, 7 + 1):
                SkeletonDog.IMGSForRunR.append( pico2d.load_image( 'assets/Monster/SkeletonDog/Move/R ({0}).png'.format( str(idx) ) ) );
                SkeletonDog.IMGSForRunL.append( pico2d.load_image( 'assets/Monster/SkeletonDog/Move/L ({0}).png'.format( str(idx) ) ) );

            SkeletonDog.FieldOfView = Const.BANSHEE_FIELD_OF_VIEW;
            #SkeletonDog.FieldOfView = 100;

            SkeletonDog.DIE_SOUND = load_wav('assets/Monster/MonsterDie.wav');
            SkeletonDog.DIE_SOUND.set_volume(50);

            SkeletonDog.LOAD = True;
        
        self.name = "SkeletonDog_" + str(SkeletonDog.UNIQUE_ID);
        SkeletonDog.UNIQUE_ID += 1;

        self.m_dir = RUN_R;
        self.IMG = SkeletonDog.IMGSForIdleR[0];
        self.force_x =600; 
        self.force_y =800;
        self.collider:Collision = CollisionRect(x,y, self.IMG.w // 2, self.IMG.h // 2);


        # status
        self.current_hp = 50;
        self.max_hp     = 50;

        # attack
        self.attack_trigger:bool = False;
        self.attack_timer:float = 0;
        self.attack_key_timer:float = 0.5;

        # animation
        self.animation_numb = 0;
        self.animation_timer = 0.0;
        self.animation_state = IDLE;

        # hit component
        self.hit_component = HitComponent(hit_recovery_time);
        self.hp_ui = HPBarForMonster(self, self.transform.tx, self.transform.ty, 1, 1, 1, True);
        
        self.dir = Const.direction_L; 
        self.last_dir = RUN_L % 2;
        
        #tag
        self.tag = Const.TAG_MONSTER;

        #behavior tree
        self.behavior_tree = None;
        self.build_behavior_tree();

        self.dir_timer = 0;


    def render(self): 
        if IDLE == self.animation_state : self.animate_idle();
        else : self.animate_run();
        if False == self.hit_component.can_hitted():
            self.hp_ui.render();

    def animate_run(self):
        if 1 == self.dir :
            SkeletonDog.IMGSForRunR[self.animation_numb].clip_composite_draw(0,0,
               self.IMG.w,
               self.IMG.h,
               0,'', 
               self.transform.tx-GameObject.Cam.camera_offset_x,
               self.transform.ty-GameObject.Cam.camera_offset_y,
               );
        else :
            SkeletonDog.IMGSForRunL[self.animation_numb].clip_composite_draw(0,0,
               self.IMG.w,
               self.IMG.h,
               0,'', 
               self.transform.tx-GameObject.Cam.camera_offset_x,
               self.transform.ty-GameObject.Cam.camera_offset_y,
               );

    def animate_idle(self):
        if 1 == self.dir :
            SkeletonDog.IMGSForIdleR[self.animation_numb].clip_composite_draw(0,0,
               self.IMG.w,
               self.IMG.h,
               0,'', 
               self.transform.tx-GameObject.Cam.camera_offset_x,
               self.transform.ty-GameObject.Cam.camera_offset_y,
               );
        else :
            SkeletonDog.IMGSForIdleL[self.animation_numb].clip_composite_draw(0,0,
               self.IMG.w,
               self.IMG.h,
               0,'', 
               self.transform.tx-GameObject.Cam.camera_offset_x,
               self.transform.ty-GameObject.Cam.camera_offset_y,
               );


    def render_debug(self): 
        if self.collider :
            draw_rectangle(*self.collider.get_area_offset(GameObject.Cam.camera_offset_x, GameObject.Cam.camera_offset_y));

    def update(self, time):
        self.behavior_tree.run(time);
        self.update_component(time);
        self.clampingInWindow();
        pass;


    def update_component(self, time):
        self.previous_transform = self.transform;
        self.collider.cx, self.collider.cy = self.transform.tx, self.transform.ty;
        self.hit_component.update(time);
        #self.hp_ui.update(time);
        return;

    def clampingInWindow(self):
        self.transform.tx = Const.clamp(0, self.transform.tx, GameObject.Cam.map_width-self.IMG.w//16)  
        self.transform.ty = Const.clamp(0, self.transform.ty, GameObject.Cam.map_height-self.IMG.h//8)
        return;

    def on_collision(self, obj):
        if Const.TAG_PLAYER == obj.tag :
            obj.calc_hp(DAMAGE);
        
    def calc_hp(self, damage):
        if self.hit_component.can_hitted() :
            self.hit_component.hit();
            self.current_hp -= damage;
            if self.current_hp <= 0:
                SkeletonDog.DIE_SOUND.play(1);
                self.current_hp = 0;
                self.state = False;

#------------------------------------------------------------------------
    def wander(self, time):
        self.animation_state = IDLE;
        self.animation_timer += time;
        self.dir_timer += time;

        if(self.animation_timer >0.1):
            self.animation_numb = (self.animation_numb +1  ) % 5;
            self.animation_timer = 0;

        if self.dir_timer >= 1.0:
            self.dir_timer = 0;
            self.dir = random.randint(-1, 2);

        self.calculate_current_position(time);


    def move_to_player(self, time):
        self.animation_state = RUN;
        self.animation_timer += time;

        if(self.animation_timer >0.1):
            self.animation_numb = (self.animation_numb +1  ) % 5;
            self.animation_timer = 0;

        self.speed = self.force_x;

        self.calculate_current_position(time);


    def calculate_current_position(self, time):
        self.transform.tx += self.force_x * self.dir * time;
        #self.y += self.force_y * self.dir * time;


    def find_player(self, time):
        self.dir_timer += time;
        if SkeletonDog.FieldOfView >= Const.distance(  self.transform.tx
                                                         , self.transform.ty
                                                         , Player.MyPlayer.transform.tx
                                                         , Player.MyPlayer.transform.ty ) :

            if self.dir_timer >= 1.2:
                self.dir_timer = 0;
                if self.transform.tx < Player.MyPlayer.transform.tx : # 더 오른쪽에 있으면????
                    self.dir = 1;
                if self.transform.tx > Player.MyPlayer.transform.tx : 
                    self.dir = -1;

            return BehaviorTree.SUCCESS;
        else:
            self.force_y = 0;
            return BehaviorTree.FAIL;


    def build_behavior_tree(self):
        chase_node = SequenceNode("Chase");
        find_player_node = LeafNode("Find Player", self.find_player);
        move_to_player_node = LeafNode("Move to Player", self.move_to_player);
        
        chase_node.add_children(find_player_node, move_to_player_node);
        
        wander_node = LeafNode("Wander", self.wander);
        wander_chase_node = SelectorNode("WanderChase");
        wander_chase_node.add_children(chase_node, wander_node);

        self.behavior_tree = BehaviorTree(wander_chase_node);
