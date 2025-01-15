import socket

from src.main.workers.motion import MotionWorker

from ..cam.main import CameraMain

class SocketMain:
    
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 65432
        self.max_listen = 5
        self.connections = []
        self.camera_main = CameraMain()
        self.motions = []
        
    def init(self):
        self.camera_main = CameraMain()
        self.camera_main.init()
        for camera in self.camera_main.cameras:
            motion = MotionWorker(q=camera.q)
            motion.start()
            self.motions.append(motion)
    
    def stop(self):
        for camera in self.camera_main.cameras:
            camera.stop()
        for motion in self.motions:
            motion.stop()
    
    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind((self.host, self.port))
                s.listen(self.max_listen)    
                while True:
                    c, addr = s.accept()
                    self.connections.append((c,addr))
            except Exception as ex:
                raise ex