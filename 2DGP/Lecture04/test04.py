from pico2d import *;
import os;

def move_left():
    global character;
    global grass;
    frame_x = 0;
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
    frame_x = 0;
    for x in range(0, 800, 8):
        clear_canvas();
        grass.draw(400, 30);
        character.clip_draw(frame_x * 100, 100 ,100, 100, x, 90);
        frame_x = ( frame_x +1 ) % 8;
        update_canvas();
        delay(0.01);


def initialize():
    global character;
    global grass;
    
    os.chdir("C:\\_Git\\2dgp\\2DGP\\assets");
    
    pico2d.open_canvas();
    pico2d.hide_cursor();

    character   = load_image('animation_sheet.png');
    grass       = load_image('grass.png');

def finalize():
    pico2d.close_canvas();





initialize();

while True:
    move_right();
    move_left();

finalize();