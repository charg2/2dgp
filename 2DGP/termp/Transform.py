class Transform:
    def __init__ (self, x:float, y:float, angle:float, scx:float, scy:float):
        self.tx     = x;
        self.ty     = y;
        self.sx     = scx;
        self.sy     = scy;
        self.degree = angle;
        return;

    def ReturnScale(self):
        return self.sx, self.sy;

    def ReturnPosition(self):
        return self.tx, self.ty;

    def ReturnDegree(self):
        return self.degree;


    def SetDegree(self,angle):
        self.degree = self.degree+ angle;
        return;

    def SetPosition(self,dx,dy):
        self.tx = self.tx + dx;
        self.ty = self.ty + dy;
        return;

    def SetScale(self, dx, dy):
        self.sx = self.sx +dx;
        self.sy = self.sy +dy;
        return;

    def TransformPos(self, dx, dy):
        self.tx =dx;
        self.ty =dy;
        return;


if(__name__ == "__main__"):
    test =  Transform( 1,2,3,4,5);

    x =();
    x = test.ReturnScale();
    print("scale = {0}".format(x));
    x = test.ReturnPosition();
    print("Pos = {0}".format(x));
    t = test.ReturnDegree();
    print("degree = {0}".format(t));
  
