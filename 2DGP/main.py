from FrameWork import FrameWork;
from KeyIO import *;
from MyTimer import *;
from Const import *;


FrameWork.Initialize();
KeyInput.Initialize();

while FrameWork.GameState :
    FrameWork.Update();
    KeyInput.Update();

FrameWork.Exit()

