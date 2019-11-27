from GameObject import *;
from Graphic import *;
from FrameWork import *;
from KeyIO import *;
from Const import *;

class TimerEvent(GameObject):
    def __init__(self, time, event_func, event_arg = None, repeat = 1):
        super(Event, self).__init__(0, 0, 0, 0, 0, True);
        self.has_image = False;
        self.collider:Collision = None;
        self.event_func = event_func;
        self.event_param = event_arg;
        self.timer = 0;
        self.event_time = time;
        self.repeat_count = repeat;
        self.current_count = 0;

    def update(self, time):
        self.timer += time;

        if self.timer <= self.event_time:
            self.do_event();
            self.timer = 0;
            self.current_count += 1;    
            if self.repeat_count >= self.current_count:
                self.state = False;

    def render(self): 
        pass;

    def do_event(self):
        if None == event_param :
            self.event_func(self.event_param);
        else : 
            self.event_func();
        pass;

class ConditionEvent(GameObject):
    def __init__(self, condition_func, event_func, condition_arg = None, event_arg = None, repeat = 1):
        super(ConditionEvent, self).__init__(0, 0, 0, 0, 0, True);
        self.has_image = False;
        self.collider:Collision = None;

        self.event_func = event_func;
        self.event_param = event_arg;

        self.condition_func = condition_func;
        self.condition_param = condition_arg;

        self.repeat_count = repeat;
        self.current_count = 0;

    def update(self, time):
        if self.condition_param == None:
            if True == self.condition_func() :
                self.do_event();
                self.current_count += 1;    
                if self.repeat_count >= self.current_count:
                    self.state = False;
        else :
            if True == self.condition_func(self.condition_param) :
                self.do_event();
                self.current_count += 1;    
                if self.repeat_count >= self.current_count:
                    self.state = False;

    def render(self): 
        pass;

    def do_event(self):
        if None != self.event_param :
            self.event_func(self.event_param);
        else : 
            self.event_func();
        pass;

