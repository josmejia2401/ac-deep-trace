import cv2
from .dto.preference import Preference

class Camera:

  def __init__(self, preference: Preference, camera_id: int):
    self.preference = preference
    self.camera_id = camera_id
    self.cam = None
    self.fourcc = None
    self.out = None
    self.subtractor = None
    self.hog = None

  def init(self) -> None:
    print(f"starting camera {self.camera_id} with preferences {self.preference}")
    
    # Open the default camera
    self.cam = cv2.VideoCapture(self.camera_id)
    
    self.autosize_resolution()
    
    self.load_video_writer()

    # Initialize the motion detector
    
    # detectShadows=True : exclude shadow areas from the objects you detected
    self.subtractor = cv2.createBackgroundSubtractorKNN(detectShadows = True)
    # exclude shadow areas from the objects you detected
    #self.subtractor = cv2.createBackgroundSubtractorMOG2(detectShadows = True)

    # initialize the HOG descriptor/person detector
    self.hog = cv2.HOGDescriptor()
    self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


  def autosize_resolution(self):
    # Get the default frame width and height
    frame_width = int(self.cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(self.cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    if self.preference.video.resolution.width < frame_width:
      frame_width = self.preference.video.resolution.width  
    if self.preference.video.resolution.heigth < frame_height:
      frame_height = self.preference.video.resolution.heigth
    
    # set default frame width and height
    self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

  def load_video_writer(self):
    
    # Get the default frame width and height
    frame_width = int(self.cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(self.cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    if self.preference.video.resolution.width < frame_width:
      frame_width = self.preference.video.resolution.width  
    if self.preference.video.resolution.heigth < frame_height:
      frame_height = self.preference.video.resolution.heigth
      
    # Define the codec and create VideoWriter object
    # XVID > output.avi | MJPG > output.avi | mp4v > output.mp4
    self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    self.out = cv2.VideoWriter(
      'output.mp4',
      self.fourcc,
      self.preference.video.frame_rate,
      (frame_width, frame_height),
      isColor=self.preference.video.is_color
    )
    
  def release(self) -> None:
    print(f"relasing camera {self.camera_id}")
    if self.cam:
      print("camera released")
      self.cam.release()
    if self.out:
      print("out released")
      self.out.release()
  
  def read(self) -> tuple[bool, cv2.typing.MatLike]:
    if self.cam is None or self.cam.isOpened == False:
      return False, None
    ret, frame = self.cam.read()
    return (ret, frame)
  
  def write_video(self, ret, frame, mirror):
    if ret == True:
      if mirror == True:
        frame = cv2.flip(frame, 1)
      self.out.write(frame)