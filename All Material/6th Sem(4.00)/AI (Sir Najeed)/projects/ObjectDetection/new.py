import cv2
import numpy as np

cap = cv2.VideoCapture("E:\\University\\6 sem\\ai\\ObjectDetection\\traffic_highway.webm")

# Object detection from stable camera
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=80)

# Initialize object count and font for displaying count
object_count = 0
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame = cap.read()
    
    height, width, _ = frame.shape
    print(height, width)
    
    # Extract region of interest
    roi = frame[50: 770,100: 1800]
    
    # Object Detection
    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    
    # Apply morphological closing to fill small gaps and smooth edges
    kernel = np.ones((6, 6), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        # Calculate area and small elements
        area = cv2.contourArea(cnt)
        if area > 100:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Increment object count

    
    cv2.imshow('Frame', frame)  
    cv2.imshow('Mask', mask)
    cv2.imshow('Roi', roi)
      
     
    key = cv2.waitKey(30)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()





