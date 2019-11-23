class HitComponent:
    def __init__(self, time):
        self.hit_timer          :float  = 0;
        self.hit_recovery_time  :float  = time;
        self.is_hitted          :bool   = False;

    def update(self, time):
        if True == self.is_hitted : #피격 상태에서 
            self.hit_timer += time;
            if self.hit_recovery_time <= self.hit_timer:
                self.is_hitted  = False;
                self.hit_timer  = 0;
    
    def can_hitted_simple(self):
        if False == self.is_hitted :
            self.is_hitted = True;
            return True;
        else :
            return False;

    def can_hitted(self):
        return self.is_hitted == False; 

    def hit(self):
        self.is_hitted = True;

    



