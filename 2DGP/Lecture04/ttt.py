

from pico2d import *;
import os;
import random;

KPU_WIDTH, KPU_HEIGHT = 1280, 1024;
MAX_RANDOM_INDEX = 10;
random_course = [( random.randint(0, KPU_WIDTH), random.randint(0, KPU_HEIGHT)) for i in range(MAX_RANDOM_INDEX)];


course_idx = 0;
position_x, position_y = 0 , 0; 
frame_x, frame_y = 0, 0;

running = True;

character:Image;
kpu_ground:Image;

def initialize():
    global character;
    global kpu_ground;
    global position_x, position_y;
    
    os.chdir("assets");
    
    pico2d.open_canvas(KPU_WIDTH, KPU_HEIGHT);
    pico2d.hide_cursor();

    character   = load_image('animation_sheet.png');
    kpu_ground  = load_image('KPU_GROUND.png');

    # 캐릭터 초기 위치;
    position_x, position_y = random_course[0];
    print(position_x);
    print(position_y);



def finalize():
    pico2d.close_canvas();

   
def render():
    global frame_x, frame_y;
    global position_x, position_y;

    pico2d.clear_canvas();
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2);

    character.clip_draw(frame_x * 100, frame_y ,100, 100, position_x, position_y);
    frame_x = (frame_x +1) % 8;

    update_canvas();

def input():
    events = pico2d.get_events();
    for event in events:
        if event.type == SDL_QUIT:
            running = False;
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False;

zz = 0;
def update():
    global position_x, position_y;
    global zz;
    global random_course;
    global course_idx, MAX_RANDOM_INDEX;

    #position_x, positioin_y, zz = draw_curve( zz ,random_course, course_idx, MAX_RANDOM_INDEX);

    for i in range(zz, 50):
        next_idx = (course_idx + 1) % MAX_RANDOM_INDEX;
        next_next_idx = (course_idx + 2) % MAX_RANDOM_INDEX;
        t = i / 100;
        position_x = (2*t**2-3*t+1) * random_course[course_idx][0] + (-4*t**2+4*t)* random_course[next_idx][0] + (2*t**2-t) * random_course[next_next_idx][0];
        position_y = (2*t**2-3*t+1) * random_course[course_idx][1] + (-4*t**2+4*t)* random_course[next_idx][1] + (2*t**2-t) * random_course[next_next_idx][1];
        zz += 5;
        if 50 == zz :
            course_idx = next_idx;
            zz = 0;
        return ;



initialize();

while running:
    input();
    update();
    render();
    delay(0.016);

finalize();