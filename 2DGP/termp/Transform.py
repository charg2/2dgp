class Transform:
    def __init__(self, x:float, y:float, angle:float, scx:float, scy:float):
        self.tx     = x;
        self.ty     = y;
        self.sx     = scx;
        self.sy     = scy;
        self.degree = angle;
        return;

    def get_scale(self):
        return self.sx, self.sy;

    def get_position(self):
        return self.tx, self.ty;
    
    def get_degree(self):
        return self.degree;


    def set_degree(self,angle):
        self.degree = self.degree+ angle;
        return;

    def set_position(self,dx,dy):
        self.tx = self.tx + dx;
        self.ty = self.ty + dy;
        return;

    def set_scale(self, dx, dy):
        self.sx = self.sx +dx;
        self.sy = self.sy +dy;
        return;

    def trasnform_position(self, dx, dy):
        self.tx =dx;
        self.ty =dy;
        return;


if(__name__ == "__main__"):
    test =  Transform( 1,2,3,4,5);

    x =();
    x = test.get_scale();
    print("scale = {0}".format(x));
    x = test.get_position();
    print("Pos = {0}".format(x));
    t = test.get_degree();
    print("degree = {0}".format(t));
  
