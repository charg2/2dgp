import Const;

class ConfigParser:
    map = {};
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
            test = line.split();
            ConfigParser.map[ test[0] ] = test[2];

    def get_int(self, value_name:str):
        return int(ConfigParser.map.get(value_name));

    def get_float(self, value_name:str):
        return float(ConfigParser.map.get(value_name));

    def get_string(self, value_name:str):
        return ConfigParser.map.get(value_name);

    def get_bool(self, value_name:str):
        return ConfigParser.map.get(value_name) == "true" or ConfigParser.map.get(value_name) == "True";

if __name__ == "__main__":
    parser = ConfigParser();
    #parser.print();
    parser.parse("config.ini");
    
    print(parser.get_int("speed"));
    print(parser.get_int("x"));
    print(parser.get_int("y"));
    print(parser.get_string("poetry"));
    print(parser.get_bool("can_move"));




