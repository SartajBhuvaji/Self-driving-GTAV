import cv2
import numpy as np
import time

training_data = np.load('training_data-1.npy', allow_pickle=True)
vertices = np.array([[0,25],[0,270],[100,270],[100,200],[430,200],[430,270],[480,270],[480,25],], np.int32)

def roi(img, vertices):
    mask = np.zeros_like(img)   
    cv2.fillPoly(mask, vertices, color=[255,255,255])
    masked = cv2.bitwise_and(img, mask)
    return masked


for data in training_data:
    img = data[0]
    choice = data[1]
    
    img = roi(img, [vertices])

    cv2.imshow('test', img)
    print(choice)
    print(img.shape)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

