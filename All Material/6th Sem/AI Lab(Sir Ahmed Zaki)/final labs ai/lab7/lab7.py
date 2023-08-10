from __future__ import division
import cv2
import os
import shutil

def haarImagesHandler(folder, face_cascade, eye_cascade):
    global lock
    folder = os.path.dirname(folder)
    os.chdir(folder)
    
    # If the folder already exists
    # if lock == False and "HaarResults" in os.listdir(folder):
    #     # Deleting the folder
    #     shutil.rmtree("HaarResults")
    
    if lock == False:
        os.makedirs("HaarResults")
        HaarOutput = os.path.join(folder, "HaarResults")
        lock = True
        Total = 0
        Found = 0
        notFound = 0
        for filename in os.listdir(folder):
            # Check if the file has an image extension
            if filename.endswith((".jpg", ".png", ".bmp",".jpeg")):
                image = cv2.imread(os.path.join(folder, filename))
                if haarImages(image, face_cascade, eye_cascade, filename, HaarOutput) == False:
                    notFound += 1
                    Total += 1
                if haarImages(image, face_cascade, eye_cascade, filename, HaarOutput) == True:
                    Found += 1
                    Total += 1
        
        percentage(Found, Total)
        percentage(notFound, Total, found=False)

def percentage(obtain, total, found=True):
    try:
        if found == True:
            print('Found', (obtain / total) * 100, '%')
        if found == False:
            print('Not Found', (obtain / total) * 100, '%')
    except ZeroDivisionError:
        print('Please Check Your Path, No File Found')

    # Deleting the HaarResults folder
    # shutil.rmtree('HaarResults')
    exit()

def haarImages(frame, face_cascade, eye_cascade, filename, HaarOutput):
    faces = face_cascade.detectMultiScale(frame, 1.1, 2)
    for (x, y, w, h) in faces:
        # Draw rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        eyes = eye_cascade.detectMultiScale(frame)
        
        # If no eyes detected
        if len(eyes) == 0:
            cv2.imwrite(os.path.join(HaarOutput, filename), frame)
            return False
        
        # If eyes detected
        if len(eyes) != 0:
            for (ex, ey, ew, eh) in eyes:
                # Draw rectangle around the detected eyes
                cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                cv2.imwrite(os.path.join(HaarOutput, filename), frame)
                print(os.path.join(HaarOutput, filename))
                return True

if __name__ == '__main__':
    global lock
    root = os.getcwd()
    face_cascade = cv2.CascadeClassifier(os.path.join(root, 'haarcascade_frontalface_default.xml'))
    eye_cascade = cv2.CascadeClassifier(os.path.join(root, 'haarcascade_eye.xml'))
    lock = False
    haarImagesHandler(r"lab7\male.jpg", face_cascade, eye_cascade)