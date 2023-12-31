'''
This file is meant to collect data for the latest model.

*** DO NOT BALANCE THIS DATA ***
*** DO NOT BALANCE THIS DATA ***
*** DO NOT BALANCE THIS DATA ***

Leave the data in raw form. It must be raw so I can use it for recurrent layers/motion/optical flow...etc. 

The data should be first person view data with the *HOOD CAMERA* in an armored Karuma. 

Driving style should be at pace, drive as fast as reasonably possible while avoiding objects and staying on road to the best of
your ability. There may be times when you drive off road to avoid things, this is fine, just get back on! 

Press "T" to pause data gathering. When you're done, press T, alt-tab out, and close the script. 

I will check all data for fitment to AI (basically how close does my AI predict the data you submit) to validate 
against people trying to submit bad data. 

When you have some data files, host them to google docs or something of that sort and share with 
Harrison@pythonprogramming.net
'''
# create_training_data.py

import numpy as np
from grabscreen import grab_screen
import cv2
import time
from getkeys import key_check
import os
import pandas as pd

w = [1,0,0,0,0,0,0,0,0]
s = [0,1,0,0,0,0,0,0,0]
a = [0,0,1,0,0,0,0,0,0]
d = [0,0,0,1,0,0,0,0,0]
wa = [0,0,0,0,1,0,0,0,0]
wd = [0,0,0,0,0,1,0,0,0]
sa = [0,0,0,0,0,0,1,0,0]
sd = [0,0,0,0,0,0,0,1,0]
nk = [0,0,0,0,0,0,0,0,1]

starting_value = 1
CHUNK_SIZE = 1000

while True:
    #file_name = 'training_data-{}.npy'.format(starting_value)
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
        break


def keys_to_output(keys):
    '''
    Convert keys to a ...multi-hot... array
     0  1  2  3  4   5   6   7    8
    [W, S, A, D, WA, WD, SA, SD, NOKEY] boolean values.
    '''
    # [W, S, A, D, WA, WD, SA, SD, NOKEY] 
    output = [0,0,0,0,0,0,0,0,0]

    # Convert keys to a ...multi-hot... array
    if 'W' in keys and 'A' in keys:
        output = wa
    elif 'W' in keys and 'D' in keys:
        output = wd
    elif 'S' in keys and 'A' in keys:
        output = sa
    elif 'S' in keys and 'D' in keys:
        output = sd
    elif 'W' in keys:
        output = w
    elif 'S' in keys:
        output = s
    elif 'A' in keys:
        output = a
    elif 'D' in keys:
        output = d
    else:
        output = nk
    return output

def main(file_name, starting_value):
    file_name = file_name
    starting_value = starting_value
    training_data = []
    df = pd.DataFrame()
    for i in range(4)[::-1]:
        print(i+1)
        time.sleep(1)

    #last_time = time.time()
    paused = False
    print('STARTING!!!')

    while(True):    
        if not paused:
            
            # 800x600 windowed mode
            screen = grab_screen(region=(0, 40, 800, 640))
            #last_time = time.time()

            # resize to something a bit more acceptable for a CNN
            screen = cv2.resize(screen, (480,270))
            # run a color convert:
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
            
            # Get key input
            keys = key_check()

            output = keys_to_output(keys)

            #cv2.imshow('window',cv2.resize(screen,(640,360)))
            #print(output)
            
            #training_data.append([screen,output])
            df1 = pd.DataFrame([[screen, output]])
            df = df._append(df1, ignore_index=True)

            #print('loop took {} seconds'.format(time.time()-last_time))
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

            if len(df) % CHUNK_SIZE == 0:
                df.to_pickle(f"training_data_{starting_value}.pickle")
                print(f"iteration {starting_value} saved")
                starting_value += 1
                df.drop(df.index, inplace=True)
                print("Iteration ", starting_value)
                   
        keys = key_check()
        if 'T' in keys:
            if paused:
                paused = False
                print('Unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')
                paused = True
                time.sleep(1)

main(file_name, starting_value)