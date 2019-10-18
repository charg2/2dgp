
from pico2d import *;
import os;

KPU_WIDTH, KPU_HEIGHT = 1280, 1024;
MOUSE_WIDTH, MOUSE_HEIGHT = 50, 52;
CHARACTER_WIDTH, CHARACTER_HEIGHT = 42, 92;

destination_x, destination_y = 0 , 0;  
position_x, position_y = 0 , 0;  
mouse_x, mouse_y = 0, 0;
frame_x, frame_y = 0, 0;
dir = 0;
p = 0;
state = 0;

running = True;

character:Image;
arrow:Image;
kpu_ground:Image;

def initialize():
    global character;
    global kpu_ground;
    global arrow;
    
    os.chdir("assets");
    
    pico2d.open_canvas(KPU_WIDTH, KPU_HEIGHT);
    #pico2d.hide_cursor();

    character   = load_image('animation_sheet.png');
    kpu_ground  = load_image('KPU_GROUND.png');
    arrow       = load_image('hand_arrow.png');

def finalize():
    pico2d.close_canvas();

   
def render():
    global mouse_x, mouse_y;
    global position_x, position_y;
    global frame_x, frame_y;
    global dir;

    pico2d.clear_canvas();
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2);

    #if destination_x != position_x or destination_y != position_y :
    #    position_x, position_y = destination_x, destination_y;
    


    if state == 1:
        move_line((position_x, position_y), (destination_x, destination_y));
        if dir == 1: frame_y = 100;
        elif dir == -1: frame_y = 0;
        #elif dir == 0: 
        #    if frame_y == 100 : frame_y = 300;
        #    elif frame_y == 0 : frame_y = 200;
    if state == 0:
        if frame_y == 100 : frame_y = 300;
        elif frame_y == 0 : frame_y = 200;

    character.clip_draw(frame_x * 100, frame_y ,100, 100, position_x, position_y);
    frame_x = (frame_x +1) % 8;
    
    arrow.draw(mouse_x, mouse_y);

    update_canvas();
    delay(0.05);


def move_line(p1, p2):
    global position_x, position_y;
    global MOUSE_WIDTH, MOUSE_HEIGHT;
    global p, state;
    for i in range(p, 100 + 1, 1):
        t = i / 100; #%로 맹그러줌.
        position_x = (1-t) * p1[0] + t * p2[0];
        position_y = (1-t) * p1[1] + t * p2[1];
        p+=2;
        if p >= 50:
            state = 0;
            p = 0;
        break;

def input():
    global mouse_x, mouse_y;
    global position_x, position_y;
    global destination_x, destination_y;
    global MOUSE_WIDTH, MOUSE_HEIGHT;
    global running, dir, state;
    global CHARACTER_WIDTH;

    events = pico2d.get_events();
    for event in events:
        if event.type == SDL_QUIT:
            running = False;
        #elif event.type == SDL_KEYDOWN and event.type == SDL_ESCAPE:
        #    running = False;

        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, KPU_HEIGHT - 1-  event.y;
            
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            print( event.x, event.y ); #클릭시 
            destination_x, destination_y = event.x - (CHARACTER_WIDTH // 2), KPU_HEIGHT - 1-  event.y + ( MOUSE_HEIGHT // 2 );
            state = 1;
            if destination_x < position_x : 
                dir = -1;
            elif destination_x > position_x : 
                dir = 1;
            else :
                dir = 0;
            

        #elif event.type == SDL_MOUSEWHEEL:
        #    pass;

# 
initialize();

while running:
    input();
    render();

finalize();