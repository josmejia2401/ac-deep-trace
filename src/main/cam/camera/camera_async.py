import threading
import queue

from ...workers.dto.q_item import QItem
from .camera import Camera
from .dto.preference import Preference

class CameraAsync(threading.Thread):
    
    def __init__(self, preference: Preference, camera_id: int):
        threading.Thread.__init__(self)
        self.preference = preference
        self.running = True
        self.lock = threading.Lock()
        self._q = queue.Queue()
        self.camera = Camera(preference=preference, camera_id=camera_id)
        self.camera.init()

    def stop(self):
        with self.lock:
            print(f"Thread {threading.current_thread().name} acquired lock for stop()")
            self.running = False
        self.camera.release()
        with self.q.mutex:
            self.q.queue.clear()
            self.q.all_tasks_done.notify_all()
            self.q.unfinished_tasks = 0  
    
    def run(self):
        print(f"rinning camera with id {self.camera.camera_id}")
        while self.running == True:
            (ret, frame) = self.camera.read()
            if ret == False:
                continue
            self.camera.write_video(ret=ret, frame=frame, mirror=False)
            self.q.put(QItem(camera_id=self.camera.camera_id, frame=frame))

    @property
    def q(self):
        return self._q

    @q.setter
    def q(self, q):
        self._q = q
        
    @q.deleter
    def q(self):
        del self._q