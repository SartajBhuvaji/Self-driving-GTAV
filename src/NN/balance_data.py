import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle 
import pickle

train_data_pickle = open("training_data.pickle", "rb")
training_data = pd.read_pickle("training_data.pickle")

df = pd.DataFrame(training_data)

lefts = pd.DataFrame()
forwards = pd.DataFrame()
rights = pd.DataFrame()

for index, row in training_data.iterrows():
    img = row[0].flatten()  # Flatten the image array
    choice = row[1]
    
    if choice == [1, 0, 0]:
        #lefts.append([img, choice])
        lefts._append(pd.DataFrame([[img, choice]]), ignore_index=True)
    elif choice == [0, 1, 0]:
        #forwards.append([img, choice])
        forwards._append(pd.DataFrame([[img, choice]]), ignore_index=True)
    elif choice == [0, 0, 1]:
        #rights.append([img, choice])
        rights._append(pd.DataFrame([[img, choice]]), ignore_index=True)
    else:
        print('no matches')

# forwards = forwards[:len(lefts)][:len(rights)]
# lefts = lefts[:len(forwards)]
# rights = rights[:len(forwards)]

# Convert the image arrays to a consistent shape

forwards = np.array([i[0] for i in forwards]).reshape(-1, 120, 160, 1)
lefts = np.array([i[0] for i in lefts]).reshape(-1, 120, 160, 1)
rights = np.array([i[0] for i in rights]).reshape(-1, 120, 160, 1)
# forwards = np.array([item for item in forwards])
# lefts = np.array([item for item in lefts])
# rights = np.array([item for item in rights])

final_data = np.concatenate((forwards, lefts, rights), axis=0)

# final_data = np.concatenate((forwards, lefts, rights), axis=0)
# shuffle(final_data)

# print(final_data[0])
np.save('training_data.npy', np.array(final_data, dtype=object))