import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle 
import pickle

train_data_pickle = open("training_data.pickle", "rb")
training_data = pd.read_pickle("training_data.pickle")

df = pd.DataFrame(training_data)
print(df.head())
print(Counter(df[1].apply(str)))

lefts = []
forwards =[]
rights = []

for index, row in training_data.iterrows():
    img = row[0].flatten()  # Flatten the image array
    choice = row[1]
    
    if choice == [1, 0, 0]:
        lefts.append([img, choice])
        #lefts._append(pd.DataFrame([[img, choice]]), ignore_index=True)
    elif choice == [0, 1, 0]:
        forwards.append([img, choice])
        #forwards._append(pd.DataFrame([[img, choice]]), ignore_index=True)
    elif choice == [0, 0, 1]:
        rights.append([img, choice])
        #rights._append(pd.DataFrame([[img, choice]]), ignore_index=True)
    else:
        print('no matches')

#print(lefts[:10])

forwards = forwards[:len(lefts)][:len(rights)]
lefts = lefts[:len(forwards)]
rights = rights[:len(forwards)]

print(len(forwards)==len(lefts)==len(rights))
# Convert the image arrays to a consistent shape


# Define a structured data type for the NumPy array
dtype = np.dtype([('0', np.ndarray), ('1', np.int32, (3,))])

# Create the structured NumPy arrays
forwards = np.array([(np.array(item[0]).flatten(), np.array(item[1], dtype=np.int32)) for item in forwards if len(np.array(item[0]).flatten()) == len(np.array(forwards[0][0]).flatten())], dtype=dtype)
lefts = np.array([(np.array(item[0]).flatten(), np.array(item[1], dtype=np.int32)) for item in lefts if len(np.array(item[0]).flatten()) == len(np.array(lefts[0][0]).flatten())], dtype=dtype)
rights = np.array([(np.array(item[0]).flatten(), np.array(item[1], dtype=np.int32)) for item in rights if len(np.array(item[0]).flatten()) == len(np.array(rights[0][0]).flatten())], dtype=dtype)



final_data = np.concatenate((forwards, lefts, rights), axis=0)

# # final_data = np.concatenate((forwards, lefts, rights), axis=0)
shuffle(final_data)

# # print(final_data[0])
np.save('training_data_balanced.npy', np.array(final_data, dtype=object))
# print(final_data.shape)