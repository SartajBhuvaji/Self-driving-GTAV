# create_training_data.py

import numpy as np
from grabscreen import grab_screen
import cv2
import time
from getkeys import key_check
import os
import pickle
import pandas as pd


def keys_to_output(keys):
    '''
    Convert keys to a ...multi-hot... array

    [A,W,D] boolean values.
    '''
    output = [0,0,0]
    #np_array_output = np.array(output)

    if 'A' in keys:
        output[0] = 1
    elif 'D' in keys:
        output[2] = 1
    else:
        output[1] = 1
    return output


# file_name = 'training_data.npy'
file_name = 'training_data.pickle'
if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    try:
        df = pd.read_pickle("training_data.pickle")
    except Exception as e:
        print(f"Error loading DataFrame from pickle: {e}")
        df = pd.DataFrame()
else:
    print('File does not exist, starting fresh!')
    df = pd.DataFrame()


def main():

    global df
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    paused = False
    while True:

        if not paused:
            # 800x600 windowed mode
            screen = grab_screen(region=(0, 40, 800, 640))
            last_time = time.time()
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (160, 120))
            keys = key_check()
            output = keys_to_output(keys)
            df1 = pd.DataFrame([[screen, output]])
            df = df._append(df1, ignore_index=True)
            # print(df.head(2))
    

            if len(df) % 100 == 0:
                print(len(df))
                df.to_pickle("training_data.pickle")

        keys = key_check()
        if 'T' in keys:
            if paused:
                paused = False
                print('unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')
                paused = True
                time.sleep(1)

main()
