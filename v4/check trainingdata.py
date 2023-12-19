import cv2
import numpy as np
import time

training_data = np.load('training_data-1.npy', allow_pickle=True)

for data in training_data:
    img = data[0]
    choice = data[1]

    cv2.imshow('test', img)
    print(choice)
    print(img.shape)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

