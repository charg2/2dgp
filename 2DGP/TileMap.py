
from Tile import Tile;
from Const import *;
from TileMapLoader import TileMapLoader as Loader;

#타일맵 설정값을 읽어서 불러옴..
class TileMap:
    def __init__(self, map_file_name:str):
        loader = Loader(map_file_name);
        self.tiles = loader.get_map();

        self.width = len(self.tiles[0]) * Tile.WIDTH;
        self.height = len(self.tiles) * Tile.HEIGHT;

        self.tile_x = len(self.tiles[0]);
        self.tile_y = len(self.tiles);

        del loader;

    def update(self, time):
        pass;

    #걍 다 그림.
    def render(self):
        for y in range(len(self.tiles)):
            for x in range(len(self.tiles[y])):
                #print("x:{0} y:{1}".format(x, y));
                self.tiles[y][x].get_tile().draw_to_origin( x * 90, y * 90);
    
                
    # 좌표계는 윈도우를 따름.
    # IO 연산을 줄이기 위해 최소 그려야 하는 타일만 그림.
    def clip_render_to_origin(self, left:int, bottom:int, window_width:int, window_height:int):
        from GameObject import GameObject;

        # LT/RB를 구해서
        cam_top = bottom + GameObject.Cam.camera_offset_y ;
        cam_bottom = cam_top + window_height;
        cam_right = left + window_width;


        # tile_range index
        min_width, max_width    = ( left // Tile.WIDTH ) , ( cam_right // Tile.WIDTH ) +1;
        min_height, max_height  = ( cam_top // Tile.HEIGHT ) , ( cam_bottom // Tile.HEIGHT ) + 1;

        #print("{0} - {1} - {2} - {3}".format(min_width, max_width, min_height, max_height ));


        if max_width > len(self.tiles[0]):
            max_width = len(self.tiles[0]);

        if max_height > len(self.tiles):
            max_height = len(self.tiles);

        offset_x:int = GameObject.Cam.camera_offset_x % Tile.WIDTH;
        offset_y:int = GameObject.Cam.camera_offset_y % Tile.HEIGHT;
        
        map_x:int = 0;
        map_y:int = 0;
        for y in range( min_height, max_height ):
            map_x = 0;
            for x in range( min_width, max_width ) :
                self.tiles[y][x].get_tile().draw_to_origin( map_x - offset_x, map_y - offset_y, Tile.WIDTH, Tile.WIDTH);
                map_x += Tile.WIDTH;
            map_y += Tile.WIDTH;


    ## for test
    #def render_map(self):
    #    import pico2d;

    #    while True:
    #        pico2d.clear_canvas();
    #        a, b = 0, 0;
    #        for x in self.tiles:
    #            a = 0;
    #            for y in x:
    #                y.get_tile().draw_to_origin(a, b);
    #                a += Tile.WIDTH;
    #            b += Tile.HEIGHT;
    #        pico2d.update_canvas();



if __name__ == "__main__" :
    import pico2d;
    pico2d.open_canvas(1610, 1080);
    map = TileMap("room1.map");
    #map.render_map();
    

    #print("시작");