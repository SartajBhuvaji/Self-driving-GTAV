# Check Training Data
import cv2
import numpy as np
import time
from collections import Counter

def get_count_choices():
    total_count_choices = Counter()

    for i in range(1,101):
        training_data = np.load(f'training_data-{i}.npy', allow_pickle=True)
        choices = [str(data[1]) for data in training_data]

        total_count_choices.update(choices)
    count_choices_dict = dict(total_count_choices)
    print(count_choices_dict)

def roi(img, vertices):
    # Applies ROI Mask to Image
    mask = np.zeros_like(img)   
    cv2.fillPoly(mask, vertices, color=[255,255,255])
    masked = cv2.bitwise_and(img, mask)
    return masked

def display_training_data():
    '''
    Displays training data
    '''
    training_data = np.load(r'training_data-74.npy', allow_pickle=True)
    mask = False #True

    if mask:
        # Masking Region of Interest
        vertices = np.array([[0,25],[0,270],[100,270],[100,200],[430,200],[430,270],[480,270],[480,25],], np.int32)

    for data in training_data:
        img = data[0]
        choice = data[1]

        if mask:
            img = roi(img, [vertices])

        cv2.imshow('screen', img)
        print(choice)
        print(img.shape)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    start_time = time.time()
    get_count_choices()
    #display_training_data()
    print(f'Elapsed time: {time.time() - start_time} seconds')

# Output:
'''
 Image Resolution : (270, 480, 3)
 'W':  [1, 0, 0, 0, 0, 0, 0, 0, 0] : 353725
 'S':  [0, 1, 0, 0, 0, 0, 0, 0, 0] : 2243
 'A':  [0, 0, 1, 0, 0, 0, 0, 0, 0] : 14303
 'D':  [0, 0, 0, 1, 0, 0, 0, 0, 0] : 13114
 'WA': [0, 0, 0, 0, 1, 0, 0, 0, 0] : 30877
 'WD': [0, 0, 0, 0, 0, 1, 0, 0, 0] : 29837
 'SA': [0, 0, 0, 0, 0, 0, 1, 0, 0] : 1952
 'SD': [0, 0, 0, 0, 0, 0, 0, 1, 0] : 1451
 'NK': [0, 0, 0, 0, 0, 0, 0, 0, 1] : 52256
  NONE : 242 
  '''
# Elapsed time: 181.86165976524353 seconds