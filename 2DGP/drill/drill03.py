from pico2d import *;
import math;
import os;

os.chdir("C:\\_Git\\2dgp\\2DGP\\assets");

open_canvas();

character   = load_image('character.png');
grass       = load_image('grass.png');

grass_height = 90;
y = 0;
x = 400;
r = 150;

while(True):
    for angle in range(-180, 180+1):
        clear_canvas_now();
        y = math.cos(angle/ (180 )* -math.pi ) * r;
        x = math.sin(angle/ (180 )* -math.pi ) * r;
        grass.draw_now(400, 30);
        character.draw_now(( x + 400 ), y + (grass_height + 150 ));
        delay(0.01);


    y = 0;

    for i in range(0, 100 + 1, 2):
        clear_canvas_now();
        x = i;
        grass.draw_now(400, 30);
        character.draw_now(x + 400, y + grass_height);
        delay(0.01);
    

    for j in range(0, 200 + 1, 2):
        clear_canvas_now();
        y = j;
        grass.draw_now(400, 30);
        character.draw_now(x + 400, y + grass_height);
        delay(0.01);

    for i in range(100, -100, -2):
        clear_canvas_now();
        x = i;
        grass.draw_now(400, 30);
        character.draw_now(x + 400, y + grass_height);
        delay(0.01);
    

    for j in range(200, 0, -2):
        clear_canvas_now();
        y = j;
        grass.draw_now(400, 30);
        character.draw_now(x + 400 , y + grass_height);
        delay(0.01); 

    for i in range(-100, 0 + 1, 2):
        clear_canvas_now();
        x = i;
        grass.draw_now(400, 30);
        character.draw_now(x + 400, y + grass_height);
        delay(0.01);


close_canvas();


# 교수님의 답안?

# while True:
#   move_rectangular();
#   move_circular();

