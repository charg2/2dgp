from pico2d import *;


class KeyInput:
    g_right_arrow:bool = False;
    g_left_arrow:bool = False;
    g_down_arrow:bool = False;
    g_up_arrow:bool = False;
    g_space:bool = False;
    
    g_p:bool = False;
    
    g_a:bool = False;
    g_w:bool = False;
    g_s:bool = False;
    g_d:bool = False;

    g_mouse_rdown:bool = False;
    g_mouse_ldown:bool = False;
    
    g_mouse_x = 0;
    g_mouse_y = 0;

    def init():
        KeyInput.g_right_arrow = False;
        KeyInput.g_left_arrow  = False;
        KeyInput.g_down_arrow = False;
        KeyInput.g_up_arrow = False;

        KeyInput.g_p = False;
        KeyInput.g_s = False;
        
        KeyInput.g_a = False;
        KeyInput.g_w = False;
        KeyInput.g_s = False;
        KeyInput.g_d = False;

        KeyInput.g_mouse_rdown = False;
        KeyInput.g_mouse_ldown = False;
        
        KeyInput.g_mouse_x = 0;
        KeyInput.g_mouse_y = 0;   
        
        KeyInput.g_previous_mouse_x = 0;
        KeyInput.g_previous_mouse_y = 0;   
        return;

    def update():
        KeyInput.polling();

    def polling():
        KeyInput.events = get_events();
        for event in KeyInput.events :
            if event.type in (SDL_QUIT, SDL_KEYDOWN, SDL_KEYUP, SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, SDL_MOUSEBUTTONUP):
                if event.type == SDL_KEYDOWN:#key down 처리
                    if event.key == SDLK_RIGHT:
                        KeyInput.g_right_arrow = True;
                    if event.key == SDLK_LEFT:
                        KeyInput.g_left_arrow = True;
                    if event.key == SDLK_DOWN:
                        KeyInput.g_down_arrow = True;
                    if event.key== SDLK_UP:#sdl_event.key  -> sdl 자체의 이벤트 키종류 인티져
                        KeyInput.g_up_arrow = True;
                    #	SDLK_SPACE
                    if event.key  == SDLK_SPACE:
                        KeyInput.g_space = True; 

                    if event.key  == SDLK_p:
                        KeyInput.g_p = True; 

                    if event.key  == SDLK_a:
                        KeyInput.g_a = True;
                    if event.key  == SDLK_w:
                        KeyInput.g_w = True;
                    if event.key  == SDLK_s:
                        KeyInput.g_s = True;
                    if event.key  == SDLK_d:
                        KeyInput.g_d = True;

                        

                    if event.key  == SDLK_ESCAPE:
                        from FrameWork import FrameWork; # referecne FrameWork
                        FrameWork.GameState = False;
                        
                if event.type == SDL_MOUSEBUTTONDOWN:#Mouse input
                    if event.button == SDL_BUTTON_RIGHT: #sdl_event.button.button -> 마우스의 이벤트는 이 항목을 통해 전달 된다.
                        KeyInput.g_mouse_rdown = True;
                    if event.button == SDL_BUTTON_LEFT:
                        KeyInput.g_mouse_ldown = True;


########    ################################################################################################################
                if event.type == SDL_KEYUP:#key up 처리
                    if event.key  == SDLK_RIGHT:
                        KeyInput.g_right_arrow = False;
                    if event.key  == SDLK_LEFT:
                        KeyInput.g_left_arrow = False;
                    if event.key  == SDLK_DOWN:
                        KeyInput.g_down_arrow = False;
                    if event.key  == SDLK_UP:
                        KeyInput.g_up_arrow = False;   
                    if event.key  == SDLK_SPACE:
                        KeyInput.g_space = False; 

                    if event.key  == SDLK_p:
                        KeyInput.g_p = False; 
                    if event.key  == SDLK_s:
                        KeyInput.g_s = False; 
                    if event.key  == SDLK_a:
                        KeyInput.g_a = False;
                    if event.key  == SDLK_w:
                        KeyInput.g_w = False;
                    if event.key  == SDLK_d:
                        KeyInput.g_d = False;

                if event.type == SDL_MOUSEBUTTONUP:
                    if event.button == SDL_BUTTON_RIGHT:
                        KeyInput.g_mouse_rdown = False;
                    if event.button == SDL_BUTTON_LEFT:
                        KeyInput.g_mouse_ldown = False;

                elif event.type == SDL_MOUSEMOTION:
                    #KeyInput.g_previous_mouse_x, KeyInput.g_previous_mouse_y = KeyInput.g_mouse_x, KeyInput.g_mouse_y;
                    KeyInput.g_mouse_x, KeyInput.g_mouse_y = event.x, event.y;

        return;        
    def display():
        print("g_right_arrow = {0} mx = {1} my = {2}".format(KeyInput.g_right_arrow, KeyInput.g_mouse_x, KeyInput.g_mouse_y));

    Initialize = staticmethod(init);
    Update = staticmethod(update);
    Display = staticmethod(display);

if __name__ == "__main__":
    pico2d.open_canvas();
    while(True):
        KeyInput.Update();
        KeyInput.Display();