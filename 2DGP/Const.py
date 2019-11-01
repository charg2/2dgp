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
    #enum
    del parser;


    def clamp(minimum, x, maximum) : 
        return max(minimum, min(x, maximum));
    def cordinate_window_position(pico2d_height) -> int :
        return poco2d_height + 1;

if __name__ == "__main__":
    print("const 실행되나");