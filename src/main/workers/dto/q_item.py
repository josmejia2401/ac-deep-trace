
class QItem:

    camera_id: int
    frame: any
    
    def __init__(self, camera_id, frame) -> None:
        self.camera_id = camera_id
        self.frame = frame