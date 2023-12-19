import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle 
import pickle

#train_data_pickle = open("training_data_1.pickle", "rb")
training_data = pd.read_pickle("training_data_1.pickle")

df = pd.DataFrame(training_data)
#print(df.head())
#print(Counter(df[1].apply(str)))

w = []
s =[]
a = []
d = []
wa = []
wd = []
sa = []
sd = []
nk = []


for index, row in training_data.iterrows():
    img = row[0].flatten()  # Flatten the image array
    choice = row[1]

    if choice == [1, 0, 0, 0, 0, 0, 0, 0, 0]:
        w.append([img, choice])
    elif choice == [0, 1, 0, 0, 0, 0, 0, 0, 0]:
        s.append([img, choice])
    elif choice == [0, 0, 1, 0, 0, 0, 0, 0, 0]:
        a.append([img, choice])
    elif choice == [0, 0, 0, 1, 0, 0, 0, 0, 0]:
        d.append([img, choice])
    elif choice == [0, 0, 0, 0, 1, 0, 0, 0, 0]:
        wa.append([img, choice])
    elif choice == [0, 0, 0, 0, 0, 1, 0, 0, 0]:
        wd.append([img, choice])
    elif choice == [0, 0, 0, 0, 0, 0, 1, 0, 0]:
        sa.append([img, choice])
    elif choice == [0, 0, 0, 0, 0, 0, 0, 1, 0]:
        sd.append([img, choice])
    elif choice == [0, 0, 0, 0, 0, 0, 0, 0, 1]:
        nk.append([img, choice])
    else:
        print('no matches')    

print(len(w), len(s), len(a), len(d), len(wa), len(wd), len(sa), len(sd), len(nk))

# Balance the lists

# w = w[:len(a)][:len(d)][:len(s)][:len(wa)][:len(wd)][:len(sa)][:len(sd)][:len(nk)]
# a = a[:len(w)][:len(d)][:len(s)][:len(wa)][:len(wd)][:len(sa)][:len(sd)][:len(nk)]
# d = d[:len(w)][:len(a)][:len(s)][:len(wa)][:len(wd)][:len(sa)][:len(sd)][:len(nk)]
# s = s[:len(w)][:len(a)][:len(d)][:len(wa)][:len(wd)][:len(sa)][:len(sd)][:len(nk)]
# wa = wa[:len(w)][:len(a)][:len(d)][:len(s)][:len(wd)][:len(sa)][:len(sd)][:len(nk)]
# wd = wd[:len(w)][:len(a)][:len(d)][:len(s)][:len(wa)][:len(sa)][:len(sd)][:len(nk)]
# sa = sa[:len(w)][:len(a)][:len(d)][:len(s)][:len(wa)][:len(wd)][:len(sd)][:len(nk)]
# sd = sd[:len(w)][:len(a)][:len(d)][:len(s)][:len(wa)][:len(wd)][:len(sa)][:len(nk)]
# nk = nk[:len(w)][:len(a)][:len(d)][:len(s)][:len(wa)][:len(wd)][:len(sa)][:len(sd)]

# print(len(w)==len(a)==len(d)==len(s)==len(wa)==len(wd)==len(sa)==len(sd)==len(nk))
# print(len(w))

# forwards = forwards[:len(lefts)][:len(rights)]
# lefts = lefts[:len(forwards)]
# rights = rights[:len(forwards)]

# print(len(forwards)==len(lefts)==len(rights))
# # Convert the image arrays to a consistent shape


# # Define a structured data type for the NumPy array
dtype = np.dtype([('0', np.ndarray), ('1', np.int32, (9,))])

# # Create the structured NumPy arrays

w = np.array([(np.array(item[0]).flatten(), np.array(item[1], dtype=np.int32)) for item in w if len(np.array(item[0]).flatten()) == len(np.array(w[0][0]).flatten())], dtype=dtype)
a = np.array([(np.array(item[0]).flatten(), np.array(item[1], dtype=np.int32)) for item in a if len(np.array(item[0]).flatten()) == len(np.array(a[0][0]).flatten())], dtype=dtype)
d = np.array([(np.array(item[0]).flatten(), np.array(item[1], dtype=np.int32)) for item in d if len(np.array(item[0]).flatten()) == len(np.array(d[0][0]).flatten())], dtype=dtype)
s = np.array([(np.array(item[0]).flatten(), np.array(item[1], dtype=np.int32)) for item in s if len(np.array(item[0]).flatten()) == len(np.array(s[0][0]).flatten())], dtype=dtype)
wa = np.array([(np.array(item[0]).flatten(), np.array(item[1], dtype=np.int32)) for item in wa if len(np.array(item[0]).flatten()) == len(np.array(wa[0][0]).flatten())], dtype=dtype)
wd = np.array([(np.array(item[0]).flatten(), np.array(item[1], dtype=np.int32)) for item in wd if len(np.array(item[0]).flatten()) == len(np.array(wd[0][0]).flatten())], dtype=dtype)
sa = np.array([(np.array(item[0]).flatten(), np.array(item[1], dtype=np.int32)) for item in sa if len(np.array(item[0]).flatten()) == len(np.array(sa[0][0]).flatten())], dtype=dtype)
sd = np.array([(np.array(item[0]).flatten(), np.array(item[1], dtype=np.int32)) for item in sd if len(np.array(item[0]).flatten()) == len(np.array(sd[0][0]).flatten())], dtype=dtype)
nk = np.array([(np.array(item[0]).flatten(), np.array(item[1], dtype=np.int32)) for item in nk if len(np.array(item[0]).flatten()) == len(np.array(nk[0][0]).flatten())], dtype=dtype)


# forwards = np.array([(np.array(item[0]).flatten(), np.array(item[1], dtype=np.int32)) for item in forwards if len(np.array(item[0]).flatten()) == len(np.array(forwards[0][0]).flatten())], dtype=dtype)
# lefts = np.array([(np.array(item[0]).flatten(), np.array(item[1], dtype=np.int32)) for item in lefts if len(np.array(item[0]).flatten()) == len(np.array(lefts[0][0]).flatten())], dtype=dtype)
# rights = np.array([(np.array(item[0]).flatten(), np.array(item[1], dtype=np.int32)) for item in rights if len(np.array(item[0]).flatten()) == len(np.array(rights[0][0]).flatten())], dtype=dtype)


# final_data = np.concatenate((forwards, lefts, rights), axis=0)

final_data = np.concatenate((w, a, d, s, wa, wd, sa, sd, nk), axis=0)
shuffle(final_data)

print(final_data[0])
np.save('training_data_balanced.npy', np.array(final_data, dtype=object))

# # # final_data = np.concatenate((forwards, lefts, rights), axis=0)
# shuffle(final_data)

# # # print(final_data[0])
# np.save('training_data_balanced.npy', np.array(final_data, dtype=object))
# # print(final_data.shape)