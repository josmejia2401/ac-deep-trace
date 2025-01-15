from .socket.main import SocketMain

class Main:
    
    socket_main: SocketMain
    
    def run(self):
        self.socket_main = SocketMain()
        self.socket_main.init()
        self.socket_main.run()
    
    def stop(self):
        self.socket_main.stop()