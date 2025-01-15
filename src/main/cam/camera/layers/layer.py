import cv2
import numpy as np

class Layer:
    
    @staticmethod
    def detect_people(hog, frame) -> tuple[bool, any]:
        # resizing for faster detection
        frame_out = cv2.resize(frame, (640, 480))
        # using a greyscale picture, also for faster detection
        gray = cv2.cvtColor(frame_out, cv2.COLOR_RGB2GRAY)

        # detect people in the image
        # returns the bounding boxes for the detected objects
        boxes, weights = hog.detectMultiScale(gray, winStride=(8,8))

        boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

        is_detected = False

        for (xA, yA, xB, yB) in boxes:
            # display the detected boxes in the colour picture
            cv2.rectangle(frame_out, (xA, yA), (xB, yB), (0, 255, 0), 2)
            is_detected = True
        
        return is_detected, frame_out
    
    
    @staticmethod
    def detect_faces(frame) -> tuple[bool, any]:
        frame_out = frame.copy()
        # Load the cascade
        # https://github.com/opencv/opencv/tree/master/data/haarcascades
        cascade = cv2.CascadeClassifier('./src/resources/data/haarcascades/haarcascade_frontalface_default.xml')
        # Convert to grayscale
        gray = cv2.cvtColor(frame_out, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        #faces = cascade.detectMultiScale(gray, 1.1, 4)
        #faces = cascade.detectMultiScale(gray, 1.3, 5)
        faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
        
        is_detected = False
        
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame_out, (x, y), (x+w, y+h), (255, 0, 0), 2)
            is_detected = True


        return is_detected, frame_out
            
    @staticmethod
    def background_subtraction(bg_subtractor, frame) -> tuple[bool, any]:
        # Every frame is used both for calculating the foreground mask and for updating the background. 
        foreground_mask = bg_subtractor.apply(frame)
        # threshold if it is bigger than 240 pixel is equal to 255 if smaller pixel is equal to 0
        # create binary image , it contains only white and black pixels
        ret , treshold = cv2.threshold(foreground_mask.copy(), 120, 255,cv2.THRESH_BINARY)
        #  dilation expands or thickens regions of interest in an image.
        dilated = cv2.dilate(treshold, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3)),iterations = 2)
        
        # Apply erosion
        #mask_eroded = cv2.morphologyEx(frame, cv2.MORPH_OPEN, dilated)
        
        # find contours 
        contours, hier = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
         # print(contours)
        #frame_ct = cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
        
        # check every contour if are exceed certain value draw bounding boxes
        large_contours = Layer.filtering_contours(contours=contours)
        frame = Layer.draw_bounding_boxes(frame=frame, large_contours=large_contours)
        
        is_detected = False
        if len(large_contours) > 0:
            is_detected = True
        
        #cv2.imshow("Subtractor", foreground_mask)
        #cv2.imshow("threshold", treshold)
        #cv2.imshow("detection", frame)
    
        return is_detected, frame


    @staticmethod
    def filtering_contours(contours) -> None:
        min_contour_area = 500  # Define your minimum area threshold
        large_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]
        return large_contours

    @staticmethod
    def draw_bounding_boxes(frame, large_contours) -> None:
        frame_out = frame.copy()
        for cnt in large_contours:
            x, y, w, h = cv2.boundingRect(cnt)
            frame = cv2.rectangle(frame_out, (x, y), (x+w, y+h), (0, 0, 200), 3)
            #frame_out = cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 255, 0), 2)
        # Display the resulting frame
        #cv2.imshow('Frame_final', frame_out)
        return frame_out
