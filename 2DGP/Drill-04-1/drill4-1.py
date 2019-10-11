# fill here

from pico2d import *;
import math;
import os;




KPU_WIDTH, KPU_HEIGHT = 1280, 1024;
grass:Image;
character:Image;
x = 0;
frame_x, frame_y = 0, 100;
dir  = 0;
running = True;

def input():
    global running;
    global x, dir;
    
    events = pico2d.get_events();

    for event in events:
        if event.type == SDL_QUIT:
            running = False;
        elif event.type == SDL_KEYDOWN :
            if event.key == SDLK_RIGHT:
                dir += 1;
            elif event.key == SDLK_LEFT:
                dir -= 1;
            elif event.key == SDLK_ESCAPE:
                running = False;
        elif event.type == SDL_KEYUP :
            if event.key == SDLK_RIGHT:
                dir -= 1;
            elif event.key == SDLK_LEFT:
                dir += 1;

def initialize():
    global character;
    global grass;
    
    os.chdir("C:\\_Git\\2016184041-Drills\\Drill-04-1\\assets");
    
    pico2d.open_canvas();
    pico2d.hide_cursor();

    character   = load_image('animation_sheet.png');
    grass       = load_image('grass.png');

    
def finalize():
    pico2d.close_canvas();

def render():
    global frame_x, frame_y;
    global dir, x;

    clear_canvas();
    grass.draw(400, 30);
    if dir == 1 :
        frame_y = 100;
        character.clip_draw( frame_x * 100 , frame_y, 100, 100, x, 90);
    elif dir == -1 :
        frame_y = 0;
        character.clip_draw( frame_x * 100 , frame_y, 100, 100, x, 90);
    elif dir == 0:
        if frame_y == 100 : frame_y = 300;
        elif frame_y == 0 : frame_y = 200;
        character.clip_draw(  frame_x * 100 , frame_y, 100, 100, x, 90);

    update_canvas();
    input();
    
    frame_x = ( frame_x + 1 ) % 8;

    if dir == 1 and x >= 800: 
        pass;
    elif dir == -1 and x <= 0:
        pass
    else:
        x += dir * 5;

initialize();

while running:
    render();
    input();

close_canvas()


