# train_model.py

import numpy as np
import os
from models import alexnet_sartaj
from sklearn.model_selection import train_test_split
from random import shuffle
import tensorboard

EPOCHS = 2
WIDTH = 480
HEIGHT = 270
LR = 1e-3
COLORS = 3
MODEL_NAME = 'alexnet_color_4096dense'

for ep in range(EPOCHS): # For all epochs 
    for v in range(1,6): # Load all 5 versions of the data
        train_data = np.load(f'cleaned_data/balanced_data-{v}.npy', allow_pickle=True)

        # change shape to (480, 270, 3)
        for i in range(len(train_data)):
            train_data[i][0] = train_data[i][0].reshape(WIDTH, HEIGHT, COLORS)

        # Split into X and y
        shuffle(train_data)    
        X = np.array([i[0] for i in train_data]).reshape(-1, WIDTH, HEIGHT, COLORS)
        y = np.array([i[1] for i in train_data])

        print(X.shape)
        print(y.shape)

        #Split data into train and test
        X_train, X_test, y_train, y_test = train_test_split(X, y , test_size=0.25, random_state=42)

        # Clear the memory
        del train_data
        del X
        del y

        ## TRAINING THE MODEL
        model = alexnet_sartaj(WIDTH, HEIGHT, LR, input=COLORS, output=9, model_name=MODEL_NAME)

        # Check if model is already trained, if so lead if before training
        if os.path.exists(f'{MODEL_NAME}.meta'):
            model.load(MODEL_NAME)
            print('Model loaded!')
        else:
            print('Model not found!')
            print('Training new model...')    

        model.fit({'input': X_train}, {'targets': y_train}, n_epoch=1, 
                  validation_set=({'input': X_test}, {'targets': y_test}),
                  run_id=MODEL_NAME, show_metric=True, batch_size=128)
        model.save(MODEL_NAME)
        del model

        # W tensorflow/core/common_runtime/bfc_allocator.cc:290] Allocator (GPU_0_bfc) ran out of memory trying to allocate 1.42GiB with freed_by_count=0. The caller indicates that this is not a failure, but this may mean that there could be performance gains if more memory were available.