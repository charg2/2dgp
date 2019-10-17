from FrameWork import FrameWork;
from KeyIO import *;


FrameWork.Initialize();
KeyInput.Initialize();

while FrameWork.GameState :
    FrameWork.Update();
    KeyInput.Update();
    
    delay(0.016);

FrameWork.Exit()