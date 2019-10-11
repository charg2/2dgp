# fill here

from pico2d import *;
import math;
import os;

KPU_WIDTH, KPU_HEIGHT = 1280, 1024;



kpu_ground:Image;
character:Image;
x, y = 0, 90;
frame_x, frame_y = 0, 100;
dir_x, dir_y  = 0, 0;
running = True;

def initialize():
    global character;
    global kpu_ground;
    
    os.chdir("assets");
    
    pico2d.open_canvas(KPU_WIDTH, KPU_HEIGHT);
    pico2d.hide_cursor();

    character   = load_image('animation_sheet.png');
    kpu_ground  = load_image('kpu_ground.png');

def input():
    global running;
    global x,y;
    global dir_x, dir_y;

    events = pico2d.get_events();

    for event in events:
        if event.type == SDL_QUIT:
            running = False;
        elif event.type == SDL_KEYDOWN :
            if event.key == SDLK_RIGHT:
                dir_x += 1;
            elif event.key == SDLK_LEFT:
                dir_x -= 1;
            elif event.key == SDLK_UP:
                dir_y += 1;
            elif event.key == SDLK_DOWN:
                dir_y -= 1;

            elif event.key == SDLK_ESCAPE:
                running = False;

        elif event.type == SDL_KEYUP :
            if event.key == SDLK_RIGHT:
                dir_x -= 1;
            elif event.key == SDLK_LEFT:
                dir_x += 1;
            elif event.key == SDLK_UP:
                dir_y -= 1;
            elif event.key == SDLK_DOWN:
                dir_y += 1;


def finalize():
    pico2d.close_canvas();

def render():
    global frame_x, frame_y;
    global x,y;
    global dir_x, dir_y;

    clear_canvas();
    kpu_ground.draw(KPU_WIDTH//2, KPU_HEIGHT//2);
    if dir_x == 1 :
        frame_y = 100;
    elif dir_x == -1 :
        frame_y = 0;
    elif dir_x == 0:
        if frame_y == 100 : frame_y = 300;
        elif frame_y == 0 : frame_y = 200;
    character.clip_draw( frame_x * 100 , frame_y, 100, 100, x, y);

    update_canvas();
    
    frame_x = ( frame_x + 1 ) % 8;

    if dir_x == 1 and x >= KPU_WIDTH: 
        pass;
    elif dir_x == -1 and x <= 0:
        pass;
    else:
        x += dir_x * 5;
    if dir_y == 1 and y >= KPU_HEIGHT: 
        pass;
    elif dir_y == -1 and y <= 0:
        pass;
    else:
        y += dir_y * 5;

initialize();

while running:
    render();
    input();

close_canvas()


