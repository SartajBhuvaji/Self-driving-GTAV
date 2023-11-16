import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
from directkeys import PressKey, ReleaseKey, W, A, S, D

def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def draw_lines(img, lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(img, (coords[0],coords[1]), (coords[2],coords[3]), [255,255,255], 3)
    except:
        pass

def process_img(original_image):
<<<<<<< HEAD
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY) #convert to gray
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300) #edge detection
    #processed_img = cv2.GaussianBlur(processed_img, (3,3), 0) #smoothing
    vertices = np.array([[10,500],[10,300],[300,200],[500,200],[800,300],[800,500],], np.int32) #region of interest
    processed_img = roi(processed_img, [vertices])

    #lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180, np.array([]), 100, 5) # hough lines -> big lines
    #draw_lines(processed_img,lines) #draw lines
=======
    # convert to gray
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    processed_img = cv2.GaussianBlur(processed_img, (3,3), 0)
    vertices = np.array([[10,500],[10,300],[300,200],[500,200],[800,300],[800,500],], np.int32)
    processed_img = roi(processed_img, [vertices])

    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180, np.array([]), 100, 5)
    draw_lines(processed_img,lines)
>>>>>>> 0aaa0977766ad2db7361b22745f603ddd8b5834e

    return processed_img



for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

PressKey(W)
time.sleep(5)
ReleaseKey(W)

last_time = time.time()
while(True):
    screen = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
    new_screen = process_img(screen)
    print('Loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    cv2.imshow('window',new_screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break