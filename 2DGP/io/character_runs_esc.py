
from pico2d import *;
import os;

def handle_events():
    global running;
    events = pico2d.get_events();
    for event in events:
        if event.type == SDL_QUIT:
            running = False;
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False;

os.chdir("C:\\_Git\\2dgp\\2DGP\\assets");

pico2d.open_canvas();

image:Image = pico2d.load_image('character.png');
running = True;
while running:
    image.draw(400, 300);
    image.draw(100, 100, 200, 100);

    pico2d.clear_canvas();
    pico2d.update_canvas();
    handle_events();


