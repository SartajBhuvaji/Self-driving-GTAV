# Check Training Data
import cv2
import numpy as np
import time
from collections import Counter
import pandas as pd

def get_count_choices(a,b):
    total_count_choices = Counter()
    for i in range(a,b):
        training_data = np.load(f'training_data-{i}.npy', allow_pickle=True)
        choices = [str(data[1]) for data in training_data]

        total_count_choices.update(choices)
    count_choices_dict = dict(total_count_choices)
    print(count_choices_dict)

def get_count_choices_per_file(a,b):
    df = pd.DataFrame(columns=['File','W','S','A','D','WA','WD','SA','SD','NK','NONE'])
    choice_to_column = {'[1, 0, 0, 0, 0, 0, 0, 0, 0]':'W',
                        '[0, 1, 0, 0, 0, 0, 0, 0, 0]':'S',
                        '[0, 0, 1, 0, 0, 0, 0, 0, 0]':'A',
                        '[0, 0, 0, 1, 0, 0, 0, 0, 0]':'D',
                        '[0, 0, 0, 0, 1, 0, 0, 0, 0]':'WA',
                        '[0, 0, 0, 0, 0, 1, 0, 0, 0]':'WD',
                        '[0, 0, 0, 0, 0, 0, 1, 0, 0]':'SA',
                        '[0, 0, 0, 0, 0, 0, 0, 1, 0]':'SD',
                        '[0, 0, 0, 0, 0, 0, 0, 0, 1]':'NK',        
                        'None':'NONE'}
    for i in range(a,b):
        training_data = np.load(f'training_data-{i}.npy', allow_pickle=True)
        choice = [str(data[1]) for data in training_data]
        count_choices = Counter(choice)
        count_choices_dict = dict(count_choices)
        df = df.append({'File': f'training_data-{i}.npy'}, ignore_index=True)
        for key in count_choices_dict:
            #print(key,':',count_choices_dict[key])
            if key == None:
                df.loc[i-a,'NONE'] = count_choices_dict['NONE']
            else:
                df.loc[i-a,choice_to_column[key]] = count_choices_dict[key]
    #print(df)
    df.replace(np.nan, 0, inplace=True)
    df.to_csv('training_data_count_001-100.csv', index=False)

def roi(img, vertices):
    # Applies ROI Mask to Image
    mask = np.zeros_like(img)   
    cv2.fillPoly(mask, vertices, color=[255,255,255])
    masked = cv2.bitwise_and(img, mask)
    return masked

def display_training_data(n):
    '''
    Displays training data
    '''
    training_data = np.load(f'training_data-{n}.npy', allow_pickle=True)
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
    #get_count_choices(1,101)
    get_count_choices_per_file(1,101)    
    #display_training_data(74)
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