from src.main.camera.dto.resolution import Resolution
from src.main.camera.dto.video import Video
from src.main.main import CameraAsync
from src.main.camera.dto.preference import Preference

camera = None
try:
    resolution = Resolution(width=640, heigth=480)
    video = Video(resolution=resolution, frame_rate=20, is_color=True)
    pref = Preference(video=video,image=None,camera_id=0)
    camera = CameraAsync(preference=pref)
    camera.run()
except KeyboardInterrupt as ex:
    print(ex)
    camera.stop()