
from GameObject import *;
from CollisionRect import *;


class Terrain(GameObject):
    UNIQUE_ID:int = 0;
    def __init__(self,x,y,sx,sy):
        super(Terrain,self).__init__(x,y,0,sx,sy,True);
        self.has_image = True;
        self.IMG = None
        self.collider = CollisionRect(x,y,sx,sy);
        self.tag = Const.TAG_TERRAIN;

        self.name = "Terrain_" + str(Terrain.UNIQUE_ID);
        Terrain.UNIQUE_ID += 1;

    def render(self):
        return;

    def render_debug(self): 
        if self.collider :
            from Graphic import GraphicLib;
            GraphicLib.DebugImg1.draw(self.collider.cx -GameObject.Cam.camera_offset_x , self.collider.cy - GameObject.Cam.camera_offset_y, self.collider.right ,self.collider.top);    
            #GraphicLib.DebugImg.clip_draw(self.previous_transform.tx , self.previous_transform.ty - GameObject.Cam.camera_offset_y, 5000, 100,);    
            #GraphicLib.DebugImg1.draw(self.transform.tx, self.transform.ty);    
        return;
    def renderForMinimap(self):
        return;    

    def update(self,Time):
        #self.update_component();
        return;

    def update_component(self):
        return;

    def on_collision(self, obj):
        #print("Terrain.py collision {0} {1}".format(obj.name, obj.transform.tx));
        return;
