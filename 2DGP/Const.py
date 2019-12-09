from ConfigParser import ConfigParser as Parser;

class Const:
    parser = Parser();
    parser.parse("config.ini");
    WIN_WIDTH, WIN_HEIGHT = parser.get_int('WIN_WIDTH'), parser.get_int('WIN_HEIGHT');
    frameForPlayer = parser.get_int('frameForPlayer');
    
    title, game, start, ending, pause  = range(5);

    direction_L,direction_R = range(2);

    SWORD, BOW, GUN = range(3);
    RUN_L, RUN_R, IDLE_R, IDLE_L = range(4);
    COLLISION_RECT , COLLISION_CIRCLE, COLLISION_POINT, COLLISION_LINE = range(4); 
    TAG_DEFAULT, TAG_TERRAIN, TAG_PLAYER, TAG_MONSTER, TAG_OPSTACLE, TAG_UI, TAG_MONSTER_PROJECTILE, TAG_PLAYER_PROJECTILE, TAG_NPC, TAG_EFFECT, TAG_MOUSE = range(11);
    CURSOR_ARROW, CURSOR_TARGET = range(2);
    DASH, JUMP, RUN, IDLE = range(4);
    DASH_CHARGE_TIME = parser.get_int('dash_charge_time');
    MAX_DASH_COUNT = parser.get_int('max_dash_count');
    BANSHEE_FIELD_OF_VIEW = parser.get_float('banshee_filed_of_view');
    STATIC_ANIMATION, STATIC_SPRITE, DYNAMIC_ANIMATION, DYNAMIC_SPRITE = range(4);

    LEFT, TOP, RIGHT, BOTTOM = range(4);
    FPS:float = 1000.0 / 60.0;

    #enum
    del parser;

    def clamp(minimum, x, maximum) : 
        return max(minimum, min(x, maximum));
    def cordinate_window_position(pico2d_height) -> int :
        return poco2d_height + 1;

    def is_collided(aleft,abottom,aright,atop,  bleft,bbottom,bright,btop):
        if aleft<bright and  aright > bleft:
            if(abottom<btop and  atop > bbottom):
                return True;
            else : return False;
        else : return False;

    def distance( ax:float, ay:float, bx:float, by:float) -> float:
        import math;
        return math.sqrt(((bx - ax)**2 + (by - ay)**2));

    def calc_degree(from_tx, from_ty, to_tx, to_ty) -> float:
        import math;
        radian = math.atan2( to_tx - from_tx, to_ty - from_ty);
        degree = (radian * 180) / math.pi;
        return degree;
    
    def calc_radian(from_tx, from_ty, to_tx, to_ty) -> float: #45%
        import math;
        radian = math.atan2( to_tx - from_tx, to_ty - from_ty);
        return radian;


if __name__ == "__main__":
    print("const 실행되나");

    print(Const.distance(-2, -3, 4 ,5));
    print(Const.distance(1, 3, 4 ,5));
    print(Const.calc_degree(0, 0, 1,1));

    print(Const.calc_radian(0, 0, 1,1));
    print(Const.calc_radian(1, 1, 0,0));
    print(Const.calc_radian(0, 1, 0,-1));
    print(Const.calc_radian(300, 120, 551,392));


