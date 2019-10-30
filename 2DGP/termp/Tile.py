from Const import *;
import pico2d;


class Tile:
    IMGSForTILE = [];
    WIDTH = 0;
    HEIGHT = 0;
    LOAD = False;

    def __init__(self, type, x:int, y:int):
        self.tile_type = type;
        self.x = x;
        self.y = y;
        if False == Tile.LOAD :
            Tile.IMGSForTILE.append(pico2d.load_image('assets/Tile/tile (1).png'));
            Tile.IMGSForTILE.append(pico2d.load_image('assets/Tile/tile (2).png'));
            Tile.IMGSForTILE.append(pico2d.load_image('assets/Tile/tile (3).png'));
            Tile.IMGSForTILE.append(pico2d.load_image('assets/Tile/tile (4).png'));
            Tile.IMGSForTILE.append(pico2d.load_image('assets/Tile/tile (5).png'));
            Tile.IMGSForTILE.append(pico2d.load_image('assets/Tile/tile (6).png'));
            Tile.IMGSForTILE.append(pico2d.load_image('assets/Tile/tile (7).png'));
            Tile.IMGSForTILE.append(pico2d.load_image('assets/Tile/tile (8).png'));
            Tile.IMGSForTILE.append(pico2d.load_image('assets/Tile/tile (9).png'));
            #Tile.IMGSForTILE.append(pico2d.load_image('assets/Tile/tile (10).png'));

            Tile.LOAD = True;

    def set_tile(self, type):
        self.type = type;

    def render(self):
        pass;

    def update(self, time):
        pass;

if __name__ == "__main__" :
    pico2d.open_canvas();
    tile = Tile(1, 2 , 3);
    print("{0}, {1}, {2}".format(tile.tile_type, tile.x, tile.y))

    print("시작");