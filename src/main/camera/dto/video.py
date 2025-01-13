from .resolution import Resolution

class Video:
    """
    160.0 x 120.0
    176.0 x 144.0
    320.0 x 240.0
    352.0 x 288.0
    640.0 x 480.0
    1024.0 x 768.0
    1280.0 x 1024.0
    """
    def __init__(self, 
                resolution: Resolution,
                frame_rate: float = 20.0,
                is_color: bool = False,
                detect_people: bool = False,
                detect_face: bool = False,
                detect_motion: bool = False) -> None:
        self.resolution = resolution
        self.frame_rate = frame_rate # fps
        self.is_color = is_color
        self.detect_people = detect_people
        self.detect_face = detect_face
        self.detect_motion = detect_motion

    def __repr__(self) -> str:
        return f"Video(resolution={self.resolution},frame_rate={self.frame_rate})"