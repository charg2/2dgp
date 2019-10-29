from Const import *;


class Tile:
    IMGSForTILE = [];
    WIDTH = 0;
    HEIGHT = 0;
    LOAD = False;

    def __init__(self):
        self.tile_type = 0;
        self.x = 0;
        self.y = 0;

        if False == Tile.LOAD :
            Tile.IMGSForTILE.pico2d.load_image('assets/Tile/tile(1).png');
            Tile.IMGSForTILE.pico2d.load_image('assets/Tile/tile(2).png');
            Tile.IMGSForTILE.pico2d.load_image('assets/Tile/tile(3).png');
            Tile.IMGSForTILE.pico2d.load_image('assets/Tile/tile(4).png');
            Tile.IMGSForTILE.pico2d.load_image('assets/Tile/tile(5).png');

    def set_tyle(self, type):
        self.type = type;

    def Render(self):
        pass;

    pass;
