import game_framework
import pico2d
import os;

import main_state

os.chdir("assets");

pico2d.open_canvas()
game_framework.run(main_state)
pico2d.close_canvas()