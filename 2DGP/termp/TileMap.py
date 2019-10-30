
from Tile import *;
from TileMapLoader import TileMapLoader as Loader;


#타일맵 설정값을 읽어서 불러옴..
class TileMap:
    def __init__(self, map_file_name:str):
        self.loader = Loader(map_file_name);
        self.tiles = loader.get_map();
        #self.x, self.y =      
        del self.loader;
        


        pass;
    def update(self, time):

        pass;

    def render(self):
        a, b = 0, 0;
        for x in self.tiles:
            a = 0;
            for y in x:
                y.get_tile().draw_to_origin(a, b);
                a += 90;
            b += 90;
        pass;