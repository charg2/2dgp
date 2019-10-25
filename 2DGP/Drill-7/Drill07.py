
from pico2d import *;
import os;
import random;

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png');

    def draw(self):
        self.image.draw(400, 30);

class Boy:
    image = None;
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90;
        self.frame = random.randint(0, 7);
        if Boy.image == None :
            Boy.image = load_image('run_animation.png');
    def update(self):
        self.frame = (self.frame + 1) % 8;
        self.x += 5;
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball:
    SMALL_BALL_GRASS_HEIGT = 60;
    BIG_BALL_GRASS_HEIGT = 70;

    def __init__(self):
        self.gravity = random.randint(5, 10);
        self.x, self.y = random.randint(100, 700), 599;

        self.big = bool(random.randint(0,1));

        if not self.big :
            self.image = load_image('ball21x21.png');
        else :
            self.image = load_image('ball41x41.png');

    def update(self):
        if not self.big:
            if self.y > Ball.SMALL_BALL_GRASS_HEIGT:
                self.y -= self.gravity;
                if self.y < Ball.SMALL_BALL_GRASS_HEIGT: 
                    self.y = Ball.SMALL_BALL_GRASS_HEIGT;
        else:
            if self.y > Ball.BIG_BALL_GRASS_HEIGT:
                self.y -= self.gravity;
                if self.y < Ball.BIG_BALL_GRASS_HEIGT : 
                    self.y = Ball.BIG_BALL_GRASS_HEIGT;

    def draw(self):
        self.image.draw(self.x, self.y);

def input():
    global running;
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False;
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False;


team:list;
balls:list;
grass:Grass;
running = True;

def initialize():
    global team, balls, grass, running;
    os.chdir("assets");
    open_canvas();
    team = [Boy() for x in range(1000)];
    grass = Grass();
    balls = [Ball() for x in range(20)];
    running = True;

def finalize():
    pico2d.close_canvas();

def update():
    global team, balls;
    for boy in team:
        boy.update();
    for ball in balls:
        ball.update();
def draw():
    global team, balls;
    global i;
    clear_canvas();
    grass.draw();
    for boy in team:
        boy.draw();
    for ball in balls:
        ball.draw();
    #i = 0;
    update_canvas();



initialize();

while running:
    input();
    update();
    draw();
    delay(0.025);

finalize();