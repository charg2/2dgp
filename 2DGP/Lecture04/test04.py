from pico2d import *;
import os;

frame_x = 0;

def move_left():
    global character;
    global grass;
    global frame_x;
    for x in range(800, 0, -8):
        pico2d.clear_canvas();
        grass.draw(400, 30);
        character.clip_draw(frame_x * 100, 0 ,100, 100, x, 90);
        frame_x = ( frame_x +1 ) % 8;
        update_canvas();
        delay(0.01);

def move_right():
    global character;
    global grass;
    global frame_x;
    for x in range(0, 800, 8):
        clear_canvas();
        grass.draw(400, 30);
        character.clip_draw(frame_x * 100, 100 ,100, 100, x, 90);
        frame_x = ( frame_x +1 ) % 8;
        update_canvas();
        delay(0.01);

pico2d.open_canvas();

os.chdir("D:\\_Git\\2dgp\\2DGP\\assets");
#character   = load_image('character.png');
character   = load_image('animation_sheet.png');
grass       = load_image('grass.png');

while True:
    move_right();
    move_left();
