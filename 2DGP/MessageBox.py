from Const import *;
from GameObject import *;
from Player import *;
from KeyIO import *;


class MessageBox(GameObject):
    BG      = None;
    SOUND   = None;
    Font    = None;

    def __init__(self, x, y, script_list:list, lambda_func = None, lambda_argument = None):
        super(MessageBox, self).__init__(x, y, 1, 1, 1, True);
        if None  == MessageBox.BG:
            MessageBox.BG       = pico2d.load_image('assets/UI/MessageBox.png');
            MessageBox.SOUND    = pico2d.load_wav("assets/UI/대사 시작시.wav");
            MessageBox.Font     = pico2d.load_font('assets/Font/font.TTF', 30);
            MessageBox.SOUND.set_volume(30);

        self.has_image      = True;
        self.name           = "MSG_BOX";

        self.buffer_list        = []; #
        self.script_list        = script_list;

        self.vertical_max_idx   = len(script_list);
        self.horizon_max_idx    = 0;
        self.vertical_idx = 0;
        self.horizon_idx = 0;


        # 줄수를 미리 만들어 놓음.
        for i in range( self.vertical_max_idx ):
            self.buffer_list.append("");

        self.timer = 0;
        self.time = 0.1;
        
        
        self.is_complete = False;
        
        self.lambda_func     = lambda_func;
        self.lambda_argument = lambda_argument;
        

    def update(self, time):
        if False == self.is_complete :
            self.timer += time;
            if self.time <= self.timer :  
                self.timer = 0;
                for v in range(self.vertical_idx, self.vertical_max_idx):
                    self.horizon_max_idx = len(self.script_list[v]);
                    for h in range(self.horizon_idx, self.horizon_max_idx):
                        self.buffer_list[v] += self.script_list[v][h];
                        MessageBox.SOUND.play(1);
                        self.horizon_idx += 1;
                        return;
                    self.horizon_idx = 0;
                    self.vertical_idx += 1;

            if self.vertical_idx == self.vertical_max_idx:
                self.is_complete = True;
                #self.lambda_func(self.lambda_argument);

                self.state  = False;
                
    def render(self):
        MessageBox.BG.draw_to_origin(0,0,
                    Const.WIN_WIDTH,
                    180,
                    );


        i = 1;
        for buffer in self.buffer_list:
            if 0 < len(buffer) :
                MessageBox.Font.draw( 50, 100 * i, buffer , (255,255,255));
            i += 1;

    def is_end(self) -> bool:
        return self.is_complete;
