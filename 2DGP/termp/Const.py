from ConfigParser import ConfigParser as Parser;

class Const:
    parser = Parser();
    parser.parse("config.ini");
    WIN_WIDTH, WIN_HEIGHT = parser.get_int('WIN_WIDTH'), parser.get_int('WIN_HEIGHT');
    frameForPlayer = parser.get_int('frameForPlayer');
    
    title, game, start, ending, pause  = range(5);
    #enum

    del parser;


if __name__ == "__main__":
    print("const 실행되나");