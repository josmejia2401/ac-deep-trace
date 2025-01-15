from .utils.helpers import Helpers
from .camera.dto.resolution import Resolution
from .camera.dto.video import Video
from .camera.camera_async import CameraAsync
from .camera.dto.preference import Preference

class CameraMain:
    
    cameras: list[CameraAsync]
    
    def __init__(self):
        self.preference = None
        self.cameras = []
        
    def load_preferences(self):
        resolution = Resolution(width=640, heigth=480)
        video = Video(resolution=resolution, frame_rate=20, is_color=True)
        self.preference = Preference(video=video, image=None)
    
    def init(self):
        self.load_preferences()
        cameras_ids = Helpers.list_cameras()
        for cam_id in cameras_ids:
            camera_async = CameraAsync(preference=self.preference, camera_id=cam_id)
            camera_async.start()
            self.cameras.append(camera_async)
    
    def stop(self):
        for cam in self.cameras:
            cam.stop()