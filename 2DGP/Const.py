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
    TAG_DEFAULT,TAG_TERRAIN, TAG_PLAYER, TAG_MONSTER = range(4);
    CURSOR_ARROW, CURSOR_TARGET = range(2);
    DASH, JUMP, RUN, IDLE = range(4);
    DASH_CHARGE_TIME = parser.get_int('dash_charge_time');
    MAX_DASH_COUNT = parser.get_int('max_dash_count');
    BANSHEE_FIELD_OF_VIEW = parser.get_float('banshee_filed_of_view');

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



if __name__ == "__main__":
    print("const 실행되나");

    print(Const.distance(-2, -3, 4 ,5));
    print(Const.distance(1, 3, 4 ,5));
