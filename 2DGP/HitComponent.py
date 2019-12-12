from Const import Const;
from pico2d import *;

class HitComponent:
    HIT_MONSTER_SOUND = None;
    HIT_PLAYER_SOUND = None;

    def __init__(self, owner, time):
        if None == HitComponent.HIT_PLAYER_SOUND :
            HitComponent.HIT_MONSTER_SOUND = pico2d.load_wav('assets/Monster/hitMonster.wav');
            HitComponent.HIT_PLAYER_SOUND = pico2d.load_wav('assets/Player/hitPlayer.wav');
            HitComponent.HIT_MONSTER_SOUND.set_volume(50);
            HitComponent.HIT_PLAYER_SOUND .set_volume(50);
            HitComponent.Font = pico2d.load_font('assets/Font/font.TTF', 20);

        self.hit_timer          :float  = 0;
        self.hit_recovery_time  :float  = time;
        self.is_hitted          :bool   = False;
        self.owner                      = owner;
        self.sound                      = None;

        assert not (Const.TAG_DEFAULT == owner.tag);
        if Const.TAG_PLAYER == owner.tag :
            self.sound = HitComponent.HIT_PLAYER_SOUND ;
        elif Const.TAG_MONSTER == owner.tag :
            self.sound = HitComponent.HIT_MONSTER_SOUND ;

    def update(self, time):
        if True == self.is_hitted : #피격 상태에서 
            self.hit_timer += time;
            if self.hit_recovery_time <= self.hit_timer:
                self.is_hitted  = False;
                self.hit_timer  = 0;
    
    #def can_hitted_simple(self):
    #    if False == self.is_hitted :
    #        self.is_hitted = True;
    #        return True;
    #    else :
    #        return False;

    def can_hitted(self):
        return self.is_hitted == False; 

    def hit(self):
        self.is_hitted = True;
        self.sound.play(1);

    



