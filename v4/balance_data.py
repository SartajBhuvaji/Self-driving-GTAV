# balance_data.py

import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

train_data = np.load('training_data-1.npy', allow_pickle=True)  

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

# 'W': [1, 0, 0, 0, 0, 0, 0, 0, 0],
# 'S': [0, 1, 0, 0, 0, 0, 0, 0, 0],
# 'A': [0, 0, 1, 0, 0, 0, 0, 0, 0],
# 'D': [0, 0, 0, 1, 0, 0, 0, 0, 0],
# 'WA': [0, 0, 0, 0, 1, 0, 0, 0, 0],
# 'WD': [0, 0, 0, 0, 0, 1, 0, 0, 0],
# 'SA': [0, 0, 0, 0, 0, 0, 1, 0, 0],
# 'SD': [0, 0, 0, 0, 0, 0, 0, 1, 0],
# 'NK': [0, 0, 0, 0, 0, 0, 0, 0, 1],
# 'default': [0, 0, 0, 0, 0, 0, 0, 0, 0],

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

final_data = w + a + d
shuffle(final_data)
print(len(final_data))

np.save('training_data_raw.npy', final_data)


# forwards = forwards[:len(lefts)][:len(rights)]
# lefts = lefts[:len(forwards)]
# rights = rights[:len(forwards)]

# final_data = forwards + lefts + rights
# shuffle(final_data)

# np.save('training_data.npy', final_data)



