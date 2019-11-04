from Tile import *;
from typing import List;

class TileMapLoader:
    def __init__(self, map_file_name:str):
        self.tiles:List[Tile] = [];
        mapfile = open(map_file_name, "r", encoding = "UTF8");
        
        string = mapfile.read();
        tile_lists = string.splitlines();
        #tile_lists.reverse(); #for window coordinate

        self.x, self.y = 0, 0
        for tile_list in tile_lists : 
            tile_list2 = tile_list.split();
            temp_tile = [];
            for tile in tile_list2:
                temp_tile.append(Tile(int(tile), self.x, self.y));
            self.tiles.append(temp_tile);
            self.y += 1;

    def get_map(self):
        return self.tiles;

    def display(self):
        for y in self.tiles:
            #for x in y:
            print(y);

    def render_map(self):
        import pico2d;

        while True:
            pico2d.clear_canvas();
            a, b = 0, 0;
            for x in self.tiles:
                a = 0;
                for y in x:
                    y.get_tile().draw_to_origin(a, b);
                    a += Tile.WIDTH;
                b += Tile.HEIGHT;
            pico2d.update_canvas();

            


if __name__ == "__main__" :
    import pico2d;
    pico2d.open_canvas(900, 900);
    map = TileMapLoader("stage1.map");
    map.display();
    map.render_map();
    

    #print("시작");