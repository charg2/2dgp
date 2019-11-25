
from GameObject import *;
from CollisionRect import *;


LEFT, TOP, RIGHT, BOTTOM = range(4);

class Terrain(GameObject):
    UNIQUE_ID:int = 0;
    def __init__(self,x,y,sx,sy):
        super(Terrain,self).__init__(x,y,0,sx,sy,True);
        self.has_image = True;
        self.IMG = None
        self.collider = CollisionRect(x,y,sx,sy);
        self.tag = Const.TAG_TERRAIN;
        self.type = BOTTOM;
        self.name = "Terrain_" + str(Terrain.UNIQUE_ID);
        Terrain.UNIQUE_ID += 1;

    def render(self):
        return;

    def render_debug(self): 
        if self.collider :
            #draw_rectangle(*self.collider.get_area());
            draw_rectangle(*self.collider.get_area_offset(GameObject.Cam.camera_offset_x, GameObject.Cam.camera_offset_y));
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
                obj.transform.ty += obj.physx.acceleration_of_gravity;
                #obj.physx.is_ground = True;
                #pass;

                #obj.transform.ty = self.collider.top + obj.collider.half_height;
                #obj.physx.is_ground = True;
                #obj.physx.velocity_x = 0;
                #obj.physx.velocity_y = 0;


                #print("Terrain.py player.ty {0}".format(obj.transform.ty));

        return;
