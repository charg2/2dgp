from pico2d import *
import os;

os.chdir("C:\\_Git\\2dgp\\2DGP\\assets");

pico2d.open_canvas();

grass = pico2d.load_image('grass.png');
character = pico2d.load_image('character.png')

grass.draw_now(400, 30);
character.draw_now(400, 90);

delay(5);

pico2d.close_canvas();
