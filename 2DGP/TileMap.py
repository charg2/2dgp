
from Tile import Tile;
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

    # IO 연산을 줄이기 위해 최소 그려야 하는 타일만 그림.
    def clip_render_to_origin(self, left:int, bottom:int, in_width:int, in_height:int):
        
        # 최소 그려야 하는 타일 계산.
        # LT/RB를 구해서
        top = bottom - in_height;
        right = left + in_width;

        # 인덱스 범위 구해서
        # 인덱스 범위 구해서
        min_width, max_width    = ( left // 90 ) -1 , ( right // 90 ) ;
        min_height, max_height  = ( top // 90 ) -1 , ( bottom // 90 ) ;

        # offset 계산
        if bottom % 90 > 0:
            max_height += 1;


        for y in range(min_height, max_height ):
            for x in range( min_width, max_width) :
                #print("x:{0} y:{1}".format(x, y));
                self.tiles[y][x].get_tile().draw_to_origin( x * 90, y * 90);
    # for test
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
    map.render_map();
    

    #print("시작");