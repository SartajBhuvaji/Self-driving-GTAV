# balance_data.py

import numpy as np
print(np.__version__) # Use 1.21.6
import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split
from random import shuffle

train_data = np.load(r'C:\Local Disk D\gtav\self-driving_GTAV\mini\training_data-mini.npy', allow_pickle=True)  
WIDTH = 270
HEIGHT = 480

df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))

w = []
s =[]
a = []
d = []
wa = []
wd = []
sa = []
sd = []
nk = []


for data in train_data:
    img = data[0]
    choice = data[1]

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
    elif choice == [0, 0, 0, 0, 0, 0, 0, 0, 0]:
        pass    
    else:
        print('no matches')    

print(len(w), len(s), len(a), len(d), len(wa), len(wd), len(sa), len(sd), len(nk))

# balance the data
w = w[:len(a)*2] # Balance W as per need

# convert to numpy array
w = np.array(w)
s = np.array(s)
a = np.array(a)
d = np.array(d)
wa = np.array(wa)
wd = np.array(wd)
sa = np.array(sa)
sd = np.array(sd)
nk = np.array(nk)

train_data = np.concatenate((w, s, a, d, wa, wd, sa, sd, nk), axis=0)
shuffle(train_data)

# change shape to (480, 270, 3)
for i in range(len(train_data)):
    train_data[i][0] = train_data[i][0].reshape(WIDTH, HEIGHT, 3)

X = np.array([i[0] for i in train_data]).reshape(-1, WIDTH, HEIGHT, 3)
y = np.array([i[1] for i in train_data])

# Split data into train and test

X_train, X_test, y_train, y_test = train_test_split(X, y , test_size=0.1, random_state=42)

# Save the data
# np.save(r'X_train.npy', X_train)
# np.save(r'X_test.npy', X_test)
# np.save(r'y_train.npy', y_train)
# np.save(r'y_test.npy', y_test)
print('done')
