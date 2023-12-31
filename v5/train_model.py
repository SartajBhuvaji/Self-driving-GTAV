# train_model.py

import numpy as np
import os
from models import lstm_alexnet
from sklearn.model_selection import train_test_split
from random import shuffle
import tensorboard
import gc

def foo():
    EPOCHS = 5
    WIDTH = 480
    HEIGHT = 270
    LR = 1e-3
    COLORS = 3
    MODEL_NAME = 'lstm_alexnet_color_4096_v1'
    LOG_DIR = 'log'

    train_data = np.load(f'cleaned_data/balanced_data_lstm-1.npy', allow_pickle=True)
    # for i in range(2,6):
    #     train_data_part = np.load(f'cleaned_data/balanced_data_lstm-{i}.npy', allow_pickle=True)
    #     train_data = np.concatenate((train_data, train_data_part), axis=0)

    # change shape to (480, 270, 3)
    for i in range(len(train_data)):
        train_data[i][0] = train_data[i][0].reshape(WIDTH, HEIGHT, COLORS)

    # Split into X and y
    #shuffle(train_data)    
    X = np.array([i[0] for i in train_data]).reshape(-1, WIDTH, HEIGHT, COLORS)
    y = np.array([i[1] for i in train_data])

    print(X.shape)
    print(y.shape)

    #Split data into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, shuffle=False)

    # Clear the memory
    del train_data
    del X
    del y

    ## TRAINING THE MODEL
    model = lstm_alexnet(WIDTH, HEIGHT, LR, input=COLORS, output=9, model_name=MODEL_NAME)

    # Check if model is already trained, if so lead if before training
    if os.path.exists(f'{MODEL_NAME}.meta'):
        model.load(MODEL_NAME)
        print('Model loaded!')
    else:
        print('Model not found!')
        print('Training new model...')    

    model.fit({'input': X_train}, {'targets': y_train}, n_epoch=EPOCHS, 
            validation_set=({'input': X_test}, {'targets': y_test}),
            run_id=MODEL_NAME, show_metric=True)
    model.save(MODEL_NAME)
    del model
    gc.collect

#foo()
# a = 4
# b = 5
# for _ in range(3):
#     try:
#         foo(a,b)
#         a = a+1
#         b = b+1
#     except:
#         print("Out of memory")    

#     if a == 5:
#         a = 1
#         b = 2

# W tensorflow/core/common_runtime/bfc_allocator.cc:290] Allocator (GPU_0_bfc) ran out of memory trying to allocate 1.42GiB with freed_by_count=0. The caller indicates that this is not a failure, but this may mean that there could be performance gains if more memory were available.
    
def bax():
    EPOCHS = 5
    WIDTH = 480
    HEIGHT = 270
    LR = 1e-3
    COLORS = 3
    MODEL_NAME = 'lstm_alexnet_color_4096_v1'
    LOG_DIR = 'log'

    #train_data = np.load(f'cleaned_data/balanced_data_lstm-1.npy', allow_pickle=True)
    model = lstm_alexnet(WIDTH, HEIGHT, LR, input=COLORS, output=9, model_name=MODEL_NAME)

    print(model.summary())


bax()    