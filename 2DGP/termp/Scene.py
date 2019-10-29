from GameObject import *
from pico2d import *
from MyTimer import *

class Scene:
    SceneNumber = 0;
    CurSceneNumber = 0;
    Pause = False;
    Time = 0;

    def __init__(self):
        self.bg = None;
        self.game_object_list_ally = [];
        self.game_object_list_terrain = [];
        self.game_object_list_obstacle = [];
        self.game_ui_list = [];

        self.start_x, self.start_y = 0, 0;

    def Iniatialize(self):
        pass;

    def Update(self):
        self.GameControl();
        
        #update
        for gobj in self.game_object_list_ally:
            gobj.update(Scene.Time);

        for terrain in self.game_object_list_terrain:
            terrain.update(Scene.Time); 
            
        for obs in self.game_object_list_obstacle:
            obs.update(Scene.Time);    

        for ui in self.game_ui_list:
            ui.update(Scene.Time);


        #remove
        for gobj in self.game_object_list_ally:
            if gobj.state == False:
                self.game_object_list_ally.remove(gobj);
                del gobj; # 가비지 콜렉터 호출로 지워줌.

        for terrain in self.game_object_list_terrain:
            if terrain.state == False:
                self.game_object_list_terrain.remove(terrain);
                del terrain;

        for obs in self.game_object_list_obstacle:
            if obs.state == False:
                self.game_object_list_obstacle.remove(obs);   
                del obs;
                
        for gui in self.game_ui_list:
            if gui.state == False:
                self.game_ui_list.remove(gui);
                del gui;

    def Collide(self):
        pass;

    def Render(self):
        for terrain in self.game_object_list_terrain:
            if(terrain.has_image == True and terrain.state):               
                terrain.render();

        for gobj in self.game_object_list_ally:
            if(gobj.has_image == True and gobj.state):               
                gobj.render();

        for obstacle in self.game_object_list_obstacle:
            if(obstacle.has_image == True and obstacle.state):               
                obstacle.render();

        for gui in self.game_ui_list:
            if(gui.has_image == True and gui.state):               
                gui.render();
    

    def ExitScene(self):
        pass;

    def GameControl(self):
        if(Scene.Pause == True) : 
            Scene.Time = 0;
        else : 
            Scene.Time = Timer.GetElapsedTime();
        return;

    def AddAllyObject(self, obj):
        self.game_object_list_ally.append(obj);
        return;

    def AddTerrainObject(self, obj):
        self.game_object_list_terrain.append(obj);
        return;

    def AddObstacleObject(self, obj):
        self.game_object_list_obstacle.append(obj);
        return;

    def AddUi(self, obj):
        self.game_ui_list.append(obj);
        return;

    def SetPause(state):
        Scene.Pause = state;
        return;

    def setStartPosition(self,x,y):
        self.start_x ,self.start_y = x,y;
        return;

    def getStartPosition(self):
        return self.start_x ,self.start_y;
                #lowx lowy   maxx maxy


if __name__ == "__main__":
    test = Scene();

    test.AddAllyObject(GameObject(10,10,10,10,10,True));

    while True:
        test.update();
        test.Render();
