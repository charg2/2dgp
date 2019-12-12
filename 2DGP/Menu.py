from GameObject     import *;
from Const          import *;
from KeyIO          import KeyInput;
from CollisionRect  import *;
from random         import randint;

def add_hp():
    print("add_hp");
    from Player import Player;
    player = Player.MyPlayer;
    player.current_hp += 10;
    if  player.max_hp < player.current_hp :
        player.current_hp = player.max_hp;

def add_max_hp():
    print("add_max_hp");
    from Player import Player;
    player = Player.MyPlayer;
    player.max_hp += 10;

def increase_dash_count():
    print("i_d_c");
    from Player import Player;
    if 5 > Player.MyPlayer.max_dash_count:
        Player.MyPlayer.max_dash_count += 1;

def increase_attack_speed():
    print("i_a_s");
    from Player import Player;
    player = Player.MyPlayer;
    player.attack_speed_offset += 1;
    if player.max_attack_speed_offset < player.attack_speed_offset:
        player.attack_speed_offset = player.max_attack_speed_offset;


#MAX = 12;
MAX = 10;
MENT_LIST  = [ "스테이크", "빵", "달걀 후라이", "버섯 구이", "마라 스프", "버섯 스프", "떡볶이", "초코 쿠키", "쿠기", "핫 스윙 치킨 오믈렛", "버거킹", "백숙"  ];
PRICE_LIST = [ 50, 5, 3, 4, 30, 20, 10, 3, 2, 50, 40, 50 ];
EFFECT_LIST = [  add_max_hp, increase_dash_count, increase_attack_speed
               , add_max_hp, increase_dash_count, increase_attack_speed
               , add_max_hp, increase_dash_count, increase_attack_speed
               , add_max_hp, increase_dash_count, increase_attack_speed ];

class Menu(GameObject):
    IMGS        = [];
    TEXT_LIST   = [];
    FONT        = None;
    SMALL_FONT  = None;
    SOUND       = None;
    BG          = None;

    def __init__(self, x, y, angle, sx, sy, state):
        super(Menu, self).__init__(x, y, angle, sx, sy, state);
        if 0 >= len(Menu.IMGS) :
            Menu.FONT       = pico2d.load_font("assets/Font/font.ttf", 30);
            Menu.SMALL_FONT = pico2d.load_font("assets/Font/font.ttf", 19);
            Menu.SOUND      = load_wav('assets/foodEat2.wav');
            Menu.BG         = pico2d.load_image( 'assets/UI/menu_bg.png' );

            for idx in range(1, 12 + 1):
                img = pico2d.load_image( 'assets/Food/FOOD ({0}).png'.format( idx ) );
                img.opacify(50);
                Menu.IMGS.append( img );

            #불러오기.
        self.name               = "Menu";
        self.state              = True;
        self.has_image          = True;
        self.type               = randint(0, MAX);
        self.img                = Menu.IMGS[self.type];
        self.ment               = MENT_LIST[self.type];
        self.price              = PRICE_LIST[self.type];
        self.effect             = EFFECT_LIST[self.type];
        self.collider:Collision = CollisionRect(x, y, 190, 60);# self.img.w // 2, self.img.h // 2);
        
        print("selftype - {0}".format(self.type))
        print("{0}-{1}".format(self.img.w, self.img.h));

        self.tag                = Const.TAG_UI;
        self.is_overapped       = False;
        self.is_sold            = False;

        self.food_info          = "[{0}] 가격 :{1}".format(self.ment, self.price);
        self.food_info_detail   = "[{0}] 가격 :{1}".format(self.ment, self.price);

    def update(self, time):
        if self.is_overapped:
            if False == self.is_sold:
                if KeyInput.g_mouse_rdown:
                    from Player import Player;
                    if Player.MyPlayer.current_coin >= self.price:
                        self.is_sold = True;
                        Menu.SOUND.play(1);
                        self.effect();
                        add_hp();
                        Player.MyPlayer.current_coin -= self.price;

        self.is_overapped = False;
        pass;

    def render(self):
        if False == self.is_sold :
            if self.is_overapped:
                self.img.draw_to_origin(660, 300);
            #draw_rectangle(*self.collider.get_area());
            Menu.BG.draw_to_origin(self.transform.tx - 180, self.transform.ty - 50, 360, 110);

            Menu.SMALL_FONT.draw(self.transform.tx - 150, self.transform.ty, self.food_info, (255, 255, 255));
        #else :
        #    Menu.FONT.draw(self.transform.tx- 150, self.transform.ty, "매진", (50, 50, 50));
        pass;

    def on_collision(self, obj):
        if Const.TAG_MOUSE == obj.tag:
            #print("마우스와 충돌");
            self.is_overapped = True;
        pass;

