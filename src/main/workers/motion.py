from .dto.q_item import QItem
import threading
import queue
import time

class MotionWorker(threading.Thread):
    
    q_item: QItem
    q: queue.Queue
    socket_client: tuple[any, any]
    
    def __init__(self, q: queue.Queue):
        threading.Thread.__init__(self)
        self.q = q
        self.socket_client = None
        self.running = True
        self.lock = threading.Lock()
    
    def update_socket_client(self, socket_client: tuple[any, any]):
        self.socket_client = socket_client
    
    def stop(self):
        with self.lock:
            print(f"Thread {threading.current_thread().name} acquired lock for stop()")
            self.running = False
    
    def run(self):
        while self.running == True:
            try:
                self.q_item = self.q.get(timeout=3) # 3s timeout
                if self.q_item:
                    #is_detected, _ = Layer.detect_people(hog=self.camera.hog,frame=self.q_item.frame)
                    #is_detected, _ = Layer.detect_faces(frame=self.q_item.frame)
                    #is_detected, _ = Layer.background_subtraction(bg_subtractor=self.camera.KNN_subtractor, frame=self.q_item.frame)
                    # send frame to socket
                    if self.socket_client:
                        self.socket_client.sendall(self.q_item.frame)
                    print("it's have data")
                    self.q.task_done()
            except queue.Empty:
                time.sleep(1)    # 1s sleep         