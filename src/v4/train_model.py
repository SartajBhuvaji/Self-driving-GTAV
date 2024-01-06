# train_model.py

import numpy as np
from models import alexnet_sartaj
import tensorboard
WIDTH = 480
HEIGHT = 270
LR = 1e-3
EPOCHS = 5

MODEL_NAME = 'alexnet_color_4096dense'
model = alexnet_sartaj(WIDTH, HEIGHT, LR, input=3, output=9, model_name=MODEL_NAME)

X_train = np.load(r'C:\Local Disk D\gtav\self-driving_GTAV\mini\X_train.npy', allow_pickle=True)
Y_train = np.load(r'C:\Local Disk D\gtav\self-driving_GTAV\mini\y_train.npy', allow_pickle=True)
X_test = np.load(r'C:\Local Disk D\gtav\self-driving_GTAV\mini\X_test.npy', allow_pickle=True)
Y_test = np.load(r'C:\Local Disk D\gtav\self-driving_GTAV\mini\y_test.npy', allow_pickle=True)

#model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit({'input': X_train}, {'targets': Y_train}, n_epoch=1, validation_set=({'input': X_test}, {'targets': Y_test}),run_id=MODEL_NAME, show_metric=True)

model.save("model.h5")

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
