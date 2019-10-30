import time

class Timer:
    prev_time       = time.time();
    current_time    = 0.0;
    delta_time      = 0.0;

    game_time       = 0;

    def init():
        Timer.current_time  = 0.0;
        Timer.prev_time     = time.time();
        Timer.delta_time    = 0.0;
        return;
    
    def update():
        Timer.current_time = time.time();
        Timer.delta_time   = Timer.current_time - Timer.prev_time;
        Timer.prev_time    = Timer.current_time;
        Timer.game_time    += Timer.delta_time;
        return;

    def get_elapsed_time():
        return Timer.delta_time;

    @staticmethod
    def get_game_time():
        return Timer.game_time;

    Initialize          = staticmethod(init);
    Update              = staticmethod(update);
    GetElapsedTime      = staticmethod(get_elapsed_time);
   

#if __name__ == "__main__":
#    Timer.Initialize();
#    fTimer = 0.0;
#    while True :
#        Timer.Update();
#        fTimer += Timer.GetElapsedTime();
#        if fTimer > 1.0:
#            print("delta = {0} , fTimer{1}".format(Timer.GetElapsedTime(),fTimer));
#            fTimer = 0.0;
