from Const import *;
from GameObject import *;
from Player import *;
from KeyIO import *;


class MessageBox(GameObject):
    BG      = None;
    SOUND   = None;
    Font    = None;
    def __init__(self, x, y, string, lambda_func = None, lambda_argument = None):
        super(MessageBox, self).__init__(x, y, 1, 1, 1, True);
        if None  == MessageBox.BG:
            MessageBox.BG = pico2d.load_image('assets/UI/MessageBox.png');
            MessageBox.SOUND = pico2d.load_wav("assets/UI/대사 시작시.wav");
            MessageBox.SOUND.set_volume(30);
            MessageBox.Font= pico2d.load_font('assets/Font/font.TTF', 30);

        self.string = string;
        self.buffer = "";
        self.name = "MSG_BOX";
        self.idx = 0;
        self.max_idx = len(string);
        self.timer = 0;
        self.time = 0.4;
        self.is_complete = False;
        self.has_image = True;
        self.lambda_func = lambda_func;
        self.lambda_argument = lambda_argument;

    def update(self, time):
        if False == self.is_complete :
            self.timer += time;

            if self.time <= self.timer and self.buffer != self.string :
                self.buffer += self.string[self.idx];
                self.idx += 1;
                MessageBox.SOUND.play(1);
                if self.idx >= self.max_idx:
                    self.is_complete = True;
                    self.state  = False;
                    self.lambda_func(self.lambda_argument);
                
    def render(self):
        MessageBox.BG.draw_to_origin(0,0,
                    Const.WIN_WIDTH,
                    180,
                    );
        MessageBox.Font.draw( 50, 100, self.buffer, (255,255,255));

    def is_end(self) -> bool:
        return self.is_complete;
