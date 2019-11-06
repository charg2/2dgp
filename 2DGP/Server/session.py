from socket import socket;

class Session:
    def __init__(self):
        self.sock:socket = None;
        self.ip:str = "";
        self.port:int = 0;
        self.send_buffer:bytearray = bytearray(65536);
        self.recv_buffer:bytearray = bytearray(65536);
        pass;

    def update(self):
        slef.recv_buffer
        pass;

e = [ 10, 200, 254,255]
v = bytearray(e);


print(e);
print("---------------");
print(v);


