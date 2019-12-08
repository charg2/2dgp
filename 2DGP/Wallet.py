from GameObject import *;
from Const import *;
from Player import *;


offset_x, offset_y = 20, 20;
class Wallet(GameObject):
    Instance:GameObject = None;
    MyPlayer:GameObject = None;
    IMG     :Image      = None;
    Font    :Font       = None;

    def __init__(self, owner, x, y, angle, sx, sy, state):
        super(Wallet, self).__init__(x, y, angle, sx, sy, state);
        
        if None == Wallet.IMG :
            Wallet.IMG           = pico2d.load_image('assets/Monster/Coin/IMG-0.png');
            Wallet.IMG.opacify(50); 
            Wallet.Instance      = self;
            Wallet.Font          = pico2d.load_font("assets/Font/font.ttf", 30);
            Wallet.MyPlayer = owner;
            
        self.name = "Wallet";
        self.state = True;
        self.has_image = True;

        self.coin:int = Wallet.MyPlayer.current_coin;
        pass;

    def update(self, time):
        pass;

    def render(self):
        coin_str = str(Wallet.MyPlayer.current_coin);
        Wallet.IMG.draw_to_origin( 5 , 100 );
        Wallet.Font.draw( 100, 100 + (Wallet.IMG.h // 2), coin_str,(255,255,255));
        pass;
        
    def get_instance():
        if None == Wallet.Instance:
            from Player import Player;
            Wallet.Instance = Wallet(Player.MyPlayer, 0,0,0,1,1,True);

        return Wallet.Instance;


class WalletR(GameObject):
    Instance:GameObject = None;
    MyPlayer:GameObject = None;
    IMG     :Image      = None;
    Font    :Font       = None;

    def __init__(self, owner, x, y, angle, sx, sy, state):
        super(WalletR, self).__init__(x, y, angle, sx, sy, state);
        
        if None == WalletR.IMG :
            WalletR.IMG           = pico2d.load_image('assets/Monster/Coin/IMG-0.png');
            WalletR.Instance      = self;
            WalletR.Font          = pico2d.load_font("assets/Font/font.ttf", 30);
            WalletR.MyPlayer      = owner;
            
        self.name = "WalletR";
        self.state = True;
        self.has_image = True;

        self.coin:int = WalletR.MyPlayer.current_coin;
        pass;

    def update(self, time):
        pass;

    def render(self):
        coin_str = str(WalletR.MyPlayer.current_coin);
        #WalletR.IMG.draw_to_origin( 1130 , 35, WalletR.IMG.w, WalletR.IMG.h + 10 );
        
        WalletR.Font.draw( 1140, 40 + (WalletR.IMG.h // 2), coin_str,(255,255,255));
        pass;
        
    def get_instance():
        if None == WalletR.Instance:
            from Player import Player;
            WalletR.Instance = WalletR(Player.MyPlayer, 0,0,0,1,1,True);

        return WalletR.Instance;
