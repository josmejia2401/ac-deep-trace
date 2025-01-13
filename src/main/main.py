from src.main.camera.layers.layer import Layer
from .camera.camera import Camera
import threading
from .camera.dto.preference import Preference

#class CameraAsync(threading.Thread):
class CameraAsync:
    
    def __init__(self, preference: Preference):
        #threading.Thread.__init__(self)
        self.preference = preference
        self.camera = Camera(preference=preference)
        self.running = True
        self.lock = threading.Lock()
        self.camera.init()
    
    def stop(self):
        with self.lock:
            print(f"Thread {threading.current_thread().name} acquired lock for .stop()")
            self.running = False
        self.camera.release()
    
    def run(self):
        while self.running == True:
            (ret, frame) = self.camera.read()
            if ret == False:
                continue
            # con el fin de no efectar el rendimiento de lectura de la camara, se debe pasar los frame a una cola y ser procesados en otro espacio
            if self.preference.video.detect_face or self.preference.video.detect_people:
                is_detected, hg_mask = Layer.detect_people(hog=self.camera.hog,frame=frame)
                is_detected, fc_mask = Layer.detect_faces(frame=frame)
                
            if self.preference.video.detect_motion:
                is_detected, fg_mask = Layer.background_subtraction(bg_subtractor=self.camera.KNN_subtractor, frame=frame)
                
            self.camera.write_video(ret=ret, frame=hg_mask, mirror=False)