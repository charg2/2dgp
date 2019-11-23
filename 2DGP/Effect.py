
from GameObject import *;
from Graphic import *;
from math import*;
from FrameWork import *;
from KeyIO import *;
from Const import *;

from typing import List;

class DashEffect(GameObject) :
    LOAD = False;

    def __init__(self, owner, x, y, angle, sx, sy, state):
        self.animation_frame = 0;
        self.animation_max_frame = 0;
        self.has_image = True;
        
        if Effect.LOAD == False:
            pass;



    
