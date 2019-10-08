import pico2d;
import os;

os.chdir("C:\\_Git\\2dgp\\2DGP\\assets");

pico2d.open_canvas();

image = pico2d.load_image('character.png');


while True:
    image.draw(400, 300);
    image.draw(100, 100, 200, 100);

    pico2d.clear_canvas();
    pico2d.update_canvas();

