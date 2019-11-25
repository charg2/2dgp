from MyTimer import *;
from KeyIO import *;
from GameObject import*;

class StateMachine:
    def __init__(self,gobj):
        self.obj = gobj;
        return;

    def update(self, time):
        pass;
    
    def render(self):
        pass;

    def exit(self):
        pass;
