import os, cv2
import pandas as pd
import numpy as np
from grabscreen import grab_screen
from tqdm import tqdm
from collections import deque
from models import inception_v3 as googlenet
from models import alexnet2
from random import shuffle

WIDTH = 480
HEIGHT = 270
LR = 1e-3
EPOCHS = 2

MODEL_NAME = 'test'
PREV_MODEL = ''
LOAD_MODEL = True

#model = googlenet(WIDTH, HEIGHT, 3, LR, output=9, model_name=MODEL_NAME)
model = alexnet2(WIDTH, HEIGHT, LR, output=9)
# alexnet2(width, height, lr, output=3):

file_name = 'training_data_balanced.npy'

train_data = np.load('training_data_balanced.npy', allow_pickle=True)

train = train_data[:-100]
test = train_data[-100:]

X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
Y = [i[1] for i in train]

test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
test_y = [i[1] for i in test]

print('X shape: ', X.shape)
print('Y shape: ', len(Y))
print('test_x shape: ', test_x.shape)
print('test_y shape: ', len(test_y))

# model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}))

#model.save("model.h5")