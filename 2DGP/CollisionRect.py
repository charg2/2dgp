from Collision import *


class CollisionRect(Collision):
    def __init__(self, x ,y, halfwidth, halfheight):
        self.half_width = halfwidth;
        self.half_height = halfheight;
        self.cx = x;
        self.cy = y;
        self.left, self.bottom = x-self.half_width, y- self.half_height;
        self.right, self.top = x+self.half_width, y+ self.half_height;
        self.collision_area_type = Const.COLLISION_RECT;

    def get_area(self) -> tuple:
        return (self.cx-self.half_width, self.cy- self.half_height, self.cx+self.half_width, self.cy+ self.half_height)


if __name__ == "__main__":
    x1,x2 ,y1,y2 = 0,0,0,0;
    Box = CollisionRect(50,50,25,25);

    x1,y1, x2, y2 = Box.get_area();
    print("{0} , {1} , {2} , {3}".format(x1,y1,x2,y2));

    string = "rr";
    print(string);

