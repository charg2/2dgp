from GameObject import *;
from pico2d import *;
from MyTimer import *;

from typing import List;

class Scene:
    SceneNumber = 0;
    CurSceneNumber = 0;
    Pause = False;
    Time = 0;
    RenderDebug = False;
    BACK_GROUND_MUSIC = None;

    def __init__(self):
        self.bg = None;
        self.game_object_list_ally          :List[GameObject] = [];
        self.game_object_list_terrain       :List[GameObject] = [];
        self.game_object_list_obstacle      :List[GameObject] = [];
        self.game_object_list_monster       :List[GameObject] = [];
        self.game_object_list_effect        :List[GameObject] = [];
        self.game_ui_list                   :List[GameObject] = [];
        self.game_object_list_bullet        :List[GameObject] = [];
        self.game_object_list_player_weapon :List[GameObject] = [];
        
        self.render_debug                   :bool = False;

        self.start_x, self.start_y = 0, 0;

    def Iniatialize(self):
        pass;

    def Update(self):
        self.GameControl();
        
        #update
        for gobj in self.game_object_list_ally:
            gobj.update(Scene.Time);

        for gobj in self.game_object_list_monster:
            gobj.update(Scene.Time);

        for gobj in self.game_object_list_player_weapon:
            gobj.update(Scene.Time);

        for terrain in self.game_object_list_terrain:
            terrain.update(Scene.Time); 
        
        for obstacle in self.game_object_list_obstacle:
            obstacle.update(Scene.Time);    

        for effect in self.game_object_list_effect:
            effect.update(Scene.Time);

        for ui in self.game_ui_list:
            ui.update(Scene.Time);


        #remove
        for gobj in self.game_object_list_ally:
            if gobj.state == False:
                self.game_object_list_ally.remove(gobj);
                del gobj; 

        for gobj in self.game_object_list_monster:
            if gobj.state == False:
                self.game_object_list_monster.remove(gobj);
                del gobj; 

        for gobj in self.game_object_list_player_weapon:
            if gobj.state == False:
                self.game_object_list_player_weapon.remove(gobj);
                del gobj; 

        for terrain in self.game_object_list_terrain:
            if terrain.state == False:
                self.game_object_list_terrain.remove(terrain);
                del terrain;

        for obstacle in self.game_object_list_obstacle:
            if obstacle.state == False:
                self.game_object_list_obstacle.remove(obstacle);   
                del obstacle;

        for effect in self.game_object_list_effect:
            if effect.state == False:
                self.game_object_list_effect.remove(effect);
                del effect;

        for gui in self.game_ui_list:
            if gui.state == False:
                self.game_ui_list.remove(gui);
                del gui;
        

    def Collide(self):
        #obj 끼리의 충돌 검사.
        #monster
        for obj in self.game_object_list_ally:
            if None != obj.collider:
                if Const.COLLISION_RECT == obj.collider.get_collision_type() :
                    for mob in self.game_object_list_monster :
                        if None != mob.collider:
                            if Const.COLLISION_RECT == mob.collider.get_collision_type() :
                                aleft,abottom,aright,atop = mob.collider.get_area();
                                bleft,bbottom,bright,btop = obj.collider.get_area();

                                if(True == Const.is_collided(aleft,abottom,aright,atop,bleft,bbottom,bright,btop)):
                                    obj.on_collision(mob);
                                    mob.on_collision(obj);
        
        # p vs ter
        for obj in self.game_object_list_ally:
            if None != obj.collider:
                if Const.COLLISION_RECT == obj.collider.get_collision_type() :

                    for ter in self.game_object_list_terrain :
                        if None != ter.collider:
                            if Const.COLLISION_RECT == ter.collider.get_collision_type() :
                                aleft,abottom,aright,atop = ter.collider.get_area();
                                bleft,bbottom,bright,btop = obj.collider.get_area();

                                if(True == Const.is_collided(aleft,abottom,aright,atop,bleft,bbottom,bright,btop)):
                                    obj.on_collision(ter);
                                    ter.on_collision(obj);

        for obj in self.game_object_list_ally:
            if None != obj.collider:
                if Const.COLLISION_RECT == obj.collider.get_collision_type() :
                    for obs in self.game_object_list_obstacle :
                        if None != obs.collider:
                            if Const.COLLISION_RECT == obs.collider.get_collision_type() :
                                aleft,abottom,aright,atop = obs.collider.get_area();
                                bleft,bbottom,bright,btop = obj.collider.get_area();
                                if(True == Const.is_collided(aleft,abottom,aright,atop,bleft,bbottom,bright,btop)):
                                    obj.on_collision(obs);
                                    obs.on_collision(obj);


        for obj in self.game_object_list_player_weapon:
            if None != obj.collider:
                if Const.COLLISION_RECT == obj.collider.get_collision_type() :
                    for mob in self.game_object_list_monster :
                        if None != mob.collider:
                            if Const.COLLISION_RECT == mob.collider.get_collision_type() :
                                aleft,abottom,aright,atop = mob.collider.get_area();
                                bleft,bbottom,bright,btop = obj.collider.get_area();

                                if(True == Const.is_collided(aleft,abottom,aright,atop,bleft,bbottom,bright,btop)):
                                    obj.on_collision(mob);
                                    mob.on_collision(obj);
        # 더 세분화 하자..
        #monster vs terrain
        for mob in self.game_object_list_monster:
            if mob.collider:
                if Const.COLLISION_RECT == mob.collider.get_collision_type() :
                    for ter in self.game_object_list_terrain :
                        if None != ter.collider:
                            if Const.COLLISION_RECT == ter.collider.get_collision_type() :
                                aleft,abottom,aright,atop = ter.collider.get_area();
                                bleft,bbottom,bright,btop = mob.collider.get_area();

                                if(True == Const.is_collided(aleft,abottom,aright,atop,bleft,bbottom,bright,btop)):
                                    mob.on_collision(ter);
                                    ter.on_collision(obj);

        for obj in self.game_object_list_player_weapon:
            if None != obj.collider:
                if Const.COLLISION_RECT == obj.collider.get_collision_type() :
                    for ter in self.game_object_list_terrain :
                        if None != ter.collider:
                            if Const.COLLISION_RECT == ter.collider.get_collision_type() :
                                aleft,abottom,aright,atop = ter.collider.get_area();
                                bleft,bbottom,bright,btop = obj.collider.get_area();
                                if(True == Const.is_collided(aleft,abottom,aright,atop,bleft,bbottom,bright,btop)):
                                    obj.on_collision(ter);
                                    ter.on_collision(obj);

    ## bullet check
    #from Player import Player;
    #player = Player.MyPlayer;
    #for bullet in self.game_object_list_bullet :
    #    aleft,abottom,aright,atop = bullet.collider.get_area();
    #    bleft,bbottom,bright,btop = obj.collider.get_area();
    #    if(True == Const.is_collided(aleft,abottom,aright,atop,bleft,bbottom,bright,btop)):
    #        obj.on_collision(bullet);
    #        ter.on_collision(obj);




    def Render(self):
        for terrain in self.game_object_list_terrain:
            if(terrain.has_image == True and terrain.state):               
                terrain.render();

        for gobj in self.game_object_list_ally:
            if(gobj.has_image == True and gobj.state):               
                gobj.render();

        # 몹끼리의 충돌은 없고 p vs m
        for gobj in self.game_object_list_monster:
            if(gobj.has_image == True and gobj.state):               
                gobj.render();

        for gobj in self.game_object_list_player_weapon:
            if(gobj.has_image == True and gobj.state):               
                gobj.render();

        for obstacle in self.game_object_list_obstacle:
            if(obstacle.has_image == True and obstacle.state):               
                obstacle.render();

        for effect in self.game_object_list_effect:
            if(effect.has_image == True and effect.state):               
                effect.render();

        for gui in self.game_ui_list:
            if(gui.has_image == True and gui.state):               
                gui.render();

        from Graphic import GraphicLib;
        if True == GraphicLib.get_debug_mode() :
            #print("");
            for terrain in self.game_object_list_terrain:
                if(terrain.has_image == True and terrain.state): 
                    terrain.render_debug();

            for gobj in self.game_object_list_ally:
                if(gobj.has_image == True and gobj.state):               
                    gobj.render_debug();

            # 몹끼리의 충돌은 없고 p vs m
            for gobj in self.game_object_list_monster:
                if(gobj.has_image == True and gobj.state):               
                    gobj.render_debug();

    


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
    
    def AddMonsterObject(self, mob ):
        self.game_object_list_monster.append(mob);
        return;

    def AddTerrainObject(self, obj):
        self.game_object_list_terrain.append(obj);
        return;

    def AddObstacleObject(self, obj):
        self.game_object_list_obstacle.append(obj);
        return;

    def add_ui(self, obj):
        self.game_ui_list.append(obj);
        return;

    def add_effect(self, effect):
        self.game_object_list_effect.append(effect);
        return;

    def add_player_weapon(self, obj):
        self.game_object_list_player_weapon.append(obj);
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

    #def remove_projectile(self, bullet):
    #    try:
    #    #if bulliet in self.game_object_list_monster:
    #        self.game_object_list_monster.remove(bullet);
    #    except ValueError:
    #        print("Scene::remove_procjectile(slef) error?");
    #    del bullet;
    


    def add_projectile(self, bullet):
        self.game_object_list_monster.append(bullet);
        return;

    def set_cam(self):
        if self.bg :
            #GameObject.Cam.SetMapSize(self.bg.IMG.w, self.bg.IMG.h);
            GameObject.Cam.SetMapSize(self.bg.map.width, self.bg.map.height);
        return;

    def on_change_scene(self):
        pass;

    def set_pause(self, state):
        Scene.Pause = state;
        return;

    
    def game_control(self):
        if(Scene.Pause == True) : 
            Scene.Time = 0;
        else : 
            Scene.Time = Timer.ReturnElapsedTime();
        return;


#if __name__ == "__main__":
#    test = Scene();

#    test.AddAllyObject(GameObject(10,10,10,10,10,True));

#    while True:
#        test.update();
#        test.Render();
