
from pico2d import *;
import os;

KPU_WIDTH, KPU_HEIGHT = 1280, 1024;

destination_x, destination_y = 0 , 0;  
position_x, position_y = 0 , 0;  
mouse_x, mouse_y = 0, 0;
frame_x, frame_y = 0, 0;
dir = 0;

running = True;

character:Image;
arrow:Image;
ground:Image;

def initialize():
    global character;
    global ground;
    global arrow;
    
    os.chdir("D:\\_Git\\2dgp\\2DGP\\assets");
    
    pico2d.open_canvas(KPU_WIDTH, KPU_HEIGHT);
    #pico2d.hide_cursor();

    character   = load_image('animation_sheet.png');
    ground      = load_image('KPU_GROUND.png');
    arrow       = load_image('hand_arrow.png');

def finalize():
    pico2d.close_canvas();

   
def render():
    global mouse_x, mouse_y;
    global position_x, position_y;
    global frame_x, frame_y;

    pico2d.clear_canvas();
    ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2);

    if destination_x != position_x or destination_y != position_y :
        position_x, position_y = destination_x, destination_y;
        pass;
    
    if dir == 1:
        frame_y = 100;
    
    if dir == -1:
        frame_y = 0;

    character.clip_draw(frame_x * 100, frame_y ,100, 100, position_x, position_y);
    frame_x = (frame_x +1) % 8;
    
    arrow.draw(mouse_x, mouse_y);
    update_canvas();
    delay(0.01);

def input():
    global mouse_x, mouse_y;
    global destination_x, destination_y;
    global running;

    events = pico2d.get_events();
    for event in events:
        if event.type == SDL_QUIT:
            running = False;
        #elif event.type == SDL_KEYDOWN and event.type == SDL_ESCAPE:
        #    running = False;

        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, KPU_HEIGHT - 1-  event.y;
            
        elif event.type == SDL_MOUSEBUTTONDOWN and event.type == SDL_MOUSEBUTTONDOWN:
            print( event.x, event.y ); #클릭시 
            destination_x, destination_y = event.x, KPU_HEIGHT - 1-  event.y;
        #elif event.type == SDL_MOUSEWHEEL:
        #    pass;



# 
initialize();

while running:
    input();
    render();

finalize();