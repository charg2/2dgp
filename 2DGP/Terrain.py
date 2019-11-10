
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
            #GraphicLib.DebugImg1.draw_to_origin(self.collider.cx , self.collider.cy , self.collider.right ,self.collider.top);    
            #GraphicLib.DebugImg1.clip_composite_draw(self.collider.left , self.collider.bottom , self.collider.right ,self.collider.top, self.transform.tx, self.transform.ty);    
            GraphicLib.DebugImg1.clip_composite_draw( self.collider.left 
                                                      ,self.collider.bottom
                                                     , self.collider.right 
                                                     , self.collider.top 
                                                      , 0, ''
                                                      , self.collider.cx  
                                                      , self.collider.cy
                                                      , self.collider.right 
                                                      , self.collider.bottom );  
            #print(self.collider.cy )
            #print(self.collider.cx )
        return;
    def renderForMinimap(self):
        return;    

    def update(self,Time):
        #self.update_component();
        return;

    def update_component(self):
        return;

    def on_collision(self, obj):
        if Const.TAG_PLAYER == obj.tag :
            if True == obj.physx.has_grivity :
                #obj.physx.is_ground = True;
                #pass;
                obj.transform.ty += obj.physx.acceleration_of_gravity;
        #print("Terrain.py collision {0} {1}".format(obj.name, obj.transform.tx));
        return;
