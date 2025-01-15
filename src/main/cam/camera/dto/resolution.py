class Resolution:
    """
    160.0 x 120.0
    176.0 x 144.0
    320.0 x 240.0
    352.0 x 288.0
    640.0 x 480.0
    1024.0 x 768.0
    1280.0 x 1024.0
    """
    def __init__(self, width: int, heigth: int) -> None:
        self.width = width
        self.heigth = heigth

    def __repr__(self) -> str:
        return f"Resolution(width={self.width},heigth={self.heigth})"