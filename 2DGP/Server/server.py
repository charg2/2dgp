
from socket import socket;
import sys;
import select;
import fcntl, os;
import errno;
from typing import List;

from Protocol import *;
from Session import *;





timeout_val:int = 10;
BUFFER_SIZE:int = 1024;
class Server:
    def __init__(self):
        self.sessions:List[socket] = [];
        self.listen_ip:str = "";
        self.port:int = 0;
        self.listen_socket:socket = None;
        self.is_angle:bool = False;
        return;

    def init(self):

        server_addr = (self.listen_ip, self.listen_port);
        
        self.listen_socket = socket(socket.AF_INET, socket.SOCK_STREAM);
        self.listen_socket.bind(server_addr);

        if self.is_nagle :
            fcntl.fcntl(self.listen_socket, fcntl.F_SETFL, os.O_NONBLOCK);

        return;

    def start(self):
        self.listen_socket.listen();
        pass;


    def stop(self):
        self.listen_socket.close();
        pass;

    def io(self):
        import copy;
        read_check_list:List[socket] = copy.deepcopy(sessions);
        read_check_list.append(slef.listen_socket);

        read_set, write_set, except_set = select.select(read_check_list, [], [], timeout_val);

        for read_sock in read_set:
            if read_sock == self.listen_socket:
                self.handle_accept();                
            else : # recv 
                self.handle_recv(read_sock, BUFFER_SIZE);
         
        # send check
        for session in self.session:
            #sesson 의 send 버퍼의 내용물이 있다면 보냄.
            pass;

    def update(self):
        for sesson in self.sessions:
            session.update();

        pass;

    # 커넥션이 여러개가 들어 오다면 여러번 확인해야 하나
    def handle_accept(self):

        client_sock = self.listen_socket.accept();
        self.sessions.append(client_sock);

        pass;

    # 
    def handle_disconnection(self, disconnected_sock:socket):
        self.sessions.remove(disconnected_sock);
        disconnected_sock.close();
        pass;

    def handle_recv(self, recv_sock:socket, buf_size:int):
        data = read_sock.recv(buf_size);
        if not data:
            self.handle_disconnection();

    def handle_send(self, session:Session):
        data = read_sock.recv(buf_size);
        if not data:
            self.handle_disconnection();


