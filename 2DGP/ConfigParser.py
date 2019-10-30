class ConfigParser:
    Dict = {};
    def __init__(self):
        pass;
    # for test
    #def print(self):
    #    f = ConfigParser.file.readline();
    #    print(f);

    def parse(self, config_name:str):
        file = open(config_name, "r", encoding = "UTF8");
        string = file.read();
        buffer = string.splitlines();
        # 공백 라인 처리는 안했다.
        for line in buffer: 
            str_list = line.split();
            print(str_list);
            if not str_list : # 공백인지 체크.
                print(str_list)
                continue;
            if str_list[0][0] == '#' : #주석 처리만 일단.
                continue;
            else:
                if str_list[-1][-1] == ';': # ; 제거.
                    str_list[-1] = str_list[-1].replace(';', "");
                ConfigParser.Dict[ str_list[0] ] = str_list[2]; #

    def get_int(self, value_name:str):
        #print(ConfigParser.Dict.get(value_name));
        return int(ConfigParser.Dict.get(value_name));

    def get_float(self, value_name:str):
        return float(ConfigParser.Dict.get(value_name));

    def get_string(self, value_name:str):
        return ConfigParser.Dict.get(value_name);

    def get_bool(self, value_name:str):
        return ConfigParser.Dict.get(value_name) == "true" or ConfigParser.Dict.get(value_name) == "True";

    ##Parse = staticmethod(parse);
    #GetInt = staticmethod(get_int);
    #GetBool = staticmethod(get_bool);
    #GetFloat = staticmethod(get_float);
    #GetString = staticmethod(get_string);

class GameConfig:
    StartX, StartY = 0, 0; # 시작 지점.
    pass;

class Stage1Tile:
    pass;

class Stage2Tile:
    pass;


if __name__ == "__main__":
    parser = ConfigParser();
    parser.parse("config.ini");
    
    print(parser.get_int("speed"));
    print(parser.get_int("x"));
    print(parser.get_int("y"));
    print(parser.get_string("poetry"));
    print(parser.get_bool("can_move"));




