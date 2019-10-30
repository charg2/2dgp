
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
        for y in self.y:
        pass;