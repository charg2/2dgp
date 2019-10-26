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
        Timer.delta_time   = Timer.current_time-Timer.prev_time;
        Timer.prev_time    = Timer.current_time;
        Timer.game_time    += Timer.delta_time;
        return;

    def returnelapsedtime():
        return Timer.delta_time;

    @staticmethod
    def returnGameTime():
        return Timer.game_time;

    Initialize          = staticmethod(init);
    Update              = staticmethod(update);
    ReturnElapsedTime   = staticmethod(returnelapsedtime);
   

if __name__ == "__main__":
    Timer.Initialize();
    fTimer = 0.0;
    while(True):
        Timer.Update();
        fTimer += Timer.ReturnElapsedTime();
        if fTimer > 1.0:
            print("delta = {0} , fTimer{1}".format(Timer.ReturnElapsedTime(),fTimer));
            fTimer = 0.0;
