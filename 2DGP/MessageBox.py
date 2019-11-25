from Const import *;
from GameObject import *;
from Player import *;
from KeyIO import *;


class MessageBox(GameObject):
    BG = None;
    SOUND = None;
    def __init__(self, x, y, angle, sx, sy, state, string):
        super(MessageBox, self).__init__(x, y, angle, sx, sy, state);
        if None  == MessageBox.BG:
            MessageBox.BG = pico2d.load_image('assets/UI/MessageBox.png');
            MessageBox.SOUND = pico2d.load_wav("assets/UI/대사 시작시.wav");
            MessageBox.SOUND.set_volume(50);

        self.string = string;
        self.buffer = "";

        self.idx = 0;
        self.max_idx = len(string);
        self.timer = 0;
        self.time = 0.3;
        self.is_complete = False;
        self.has_image = True;

    def update(self, time):
        if False == self.is_complete :
            self.timer += time;

            if self.time <= self.timer and self.buffer != self.string :
                self.buffer += self.string[self.idx];
                self.idx += 1;
                MessageBox.SOUND.play(1);
                if self.idx > self.max_idx:
                    self.is_complete = True;
                
    def render(self):
        MessageBox.BG.draw_to_origin(0,0,
                    Const.WIN_WIDTH,
                    180,
                    );
        GameObject.Font.draw( 10, 100, self.buffer, (255,255,255));
