

## fill here

#from pico2d import *;
#import math;

#open_canvas();

#grass = load_image('grass.png');
#character = load_image('animation_sheet.png');

#x = 0;
#y = 0;
#frame_x = 0;
#frame_y = 1;

#is_forward = True;
#offset = 16;

#while True :
#    for i in range(0, 100+1):
#        if i == 0:
#            frame_y = 1;
#        elif i == 49:
#            frame_y = 0;

#        clear_canvas();
#        grass.draw(400, 30);
#        character.clip_draw(frame_x * 100, frame_y * 100, 100, 100 ,x ,90);
#        update_canvas();

#        frame_x = ( frame_x +1 ) % 8;
#        x = math.sin( i / 100  * math.pi) * 800;

#        delay(0.05);
#        get_events();



#close_canvas()


