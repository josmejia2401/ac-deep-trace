from .video import Video

class Preference:

    video: Video
    
    def __init__(self, **kwargs) -> None:
        self.video = kwargs["video"]
        self.image = kwargs["image"]
        self.description = kwargs.get("description", "")
        self.channel = kwargs.get("channel", "Canal 0")

    def __repr__(self) -> str:
        return f"Preference(video={self.video})"