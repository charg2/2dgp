from Const import *;

class Collision:
    def __init__(self):
        self.collision_area_type = Const.collision_none;
        return;

    def get_area(self) :
        pass;

    def get_collision_type(self):
        return self.collision_area_type;
