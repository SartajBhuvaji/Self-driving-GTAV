# train_model.py

import numpy as np
from models import alexnet_sartaj
import tensorboard
WIDTH = 480
HEIGHT = 270
LR = 1e-3
EPOCHS = 1
#MODEL_NAME = 'pygta5-car-fast-{}-{}-{}-epochs-300K-data.model'.format(LR, 'alexnetv2',EPOCHS)
MODEL_NAME = 'alexnet_color_30_2'


##def alexnet(width, height, lr, input= 1, output=9, model_name = 'alexnet_color_30'):
model = alexnet_sartaj(WIDTH, HEIGHT, LR, input=3, output=9, model_name=MODEL_NAME)
# data = np.load(r'training_data_raw.npy', allow_pickle=True)

# X = np.array([i[0] for i in data]).reshape(-1, WIDTH, HEIGHT, 1)
# Y = np.array([np.array(i[1]) for i in data])  # Convert Y to a numpy array

# print("X shape: ", X.shape)
# print("Y shape: ", Y.shape)

# print("Data shape: ", data.shape)

# X = np.array([i[0] for i in data]).reshape(-1, WIDTH, HEIGHT, 1)
# Y = np.array([np.array(i[1]) for i in data])  # Convert Y to a numpy array

# print("X[0] ", X[0])
# print("Y[0] ", Y[0])

# # Split X and Y into training and testing data
# from sklearn.model_selection import train_test_split
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

# print("X_train shape: ", X_train.shape)
# print("Y_train shape: ", Y_train.shape)
# print("X_test shape: ", X_test.shape)
# print("Y_test shape: ", Y_test.shape)


# del data
# del X
# del Y


X_train = np.load(r'C:\Local Disk D\gtav\self-driving_GTAV\mini\X_train.npy', allow_pickle=True)
Y_train = np.load(r'C:\Local Disk D\gtav\self-driving_GTAV\mini\y_train.npy', allow_pickle=True)
X_test = np.load(r'C:\Local Disk D\gtav\self-driving_GTAV\mini\X_test.npy', allow_pickle=True)
Y_test = np.load(r'C:\Local Disk D\gtav\self-driving_GTAV\mini\y_test.npy', allow_pickle=True)

#model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit({'input': X_train}, {'targets': Y_train}, n_epoch=1, validation_set=({'input': X_test}, {'targets': Y_test}),run_id=MODEL_NAME, show_metric=True)

#model.save("model.h5")

# hm_data = 1
# for i in range(EPOCHS):
#     for i in range(1,hm_data+1):
#         # train_data = np.load('training_data_balanced.npy'.format(i), allow_pickle=True)

#         # train = train_data[:-100]
#         # test = train_data[-100:]

#         # X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
#         # Y = [i[1] for i in train]

#         # test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
#         # test_y = [i[1] for i in test]

#         model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}), 
#             snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

#         #model.save(MODEL_NAME)

# model.save("model.h5")


# tensorboard --logdir=foo:C:/path/to/log

































































# import os, cv2
# import pandas as pd
# import numpy as np
# from grabscreen import grab_screen
# from tqdm import tqdm
# from collections import deque
# from models import sartajnet_with_attention
# from random import shuffle
# from alexnet import alexnet
# import tensorboard

# FILE_I_END = 1860

# WIDTH = 480
# HEIGHT = 270
# LR = 1e-3
# EPOCHS = 1

# MODEL_NAME = ''
# PREV_MODEL = ''
# LOAD_MODEL = True

# #model = googlenet(WIDTH, HEIGHT, 3, LR, output=9, model_name=MODEL_NAME)
# model = sartajnet_with_attention(WIDTH, HEIGHT, 3, LR, output=9, model_name=MODEL_NAME)

# train_data = np.load('../mini/training_data-mini.npy', allow_pickle=True)
# train = train_data[:-50]
# test = train_data[-50:]

# X = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 3)
# Y = [i[1] for i in train]

# test_x = np.array([i[0] for i in test]).reshape(-1, WIDTH, HEIGHT, 3)
# test_y = [i[1] for i in test]

# model.fit({'input': X}, {'targets': Y}, n_epoch = 1, validation_set = ({'input': test_x}, {'targets': test_y}),
# snapshot_step = 2, show_metric = True, run_id = MODEL_NAME)

# # if LOAD_MODEL:
# #     model.load(PREV_MODEL)
# #     print('We have loaded a previous model!!!!')

# # iterates through the training files
# for e in range(EPOCHS):
# ##    data_order = [i for i in range(1,FILE_I_END+1)]
#     data_order = [i for i in range(1, FILE_I_END + 1)]
#     shuffle(data_order)
#     for count, i in enumerate(data_order):
#         try:
#             file_name = 'J:/phase10-random-padded/training_data-{0}.npy'.format(i)
#             # full file info
#             train_data = np.load(file_name)
#             print('training_data-{0}.npy'.format(i), len(train_data))

# ##            # [   [    [FRAMES], CHOICE   ]    ]
# ##            train_data = []
# ##            current_frames = deque(maxlen=HM_FRAMES)
# ##
# ##            for ds in data:
# ##                screen, choice = ds
# ##                gray_screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
# ##
# ##
# ##                current_frames.append(gray_screen)
# ##                if len(current_frames) == HM_FRAMES:
# ##                    train_data.append([list(current_frames),choice])

#             # always validating unique data:
# ##            shuffle(train_data)
#             train = train_data[:-50]
#             test = train_data[-50:]

#             X = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 3)
#             Y = [i[1] for i in train]

#             test_x = np.array([i[0] for i in test]).reshape(-1, WIDTH, HEIGHT, 3)
#             test_y = [i[1] for i in test]

#             model.fit({'input': X}, {'targets': Y}, n_epoch = 1, validation_set = ({'input': test_x}, {'targets': test_y}),
#                 snapshot_step = 2500, show_metric = True, run_id = MODEL_NAME)

#             if count % 10 == 0:
#                 print('SAVING MODEL!')
#                 model.save(MODEL_NAME)

#         except Exception as e:
#             print(e)


# # #tensorboard --logdir=foo:J:/phase10-code/log