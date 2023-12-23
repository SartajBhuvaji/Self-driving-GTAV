from collections import Counter
import numpy as np

total_count_choices = Counter()

for i in range(1,101):
    training_data = np.load(f'training_data-{i}.npy', allow_pickle=True)
    choices = [str(data[1]) for data in training_data]

    total_count_choices.update(choices)
count_choices_dict = dict(total_count_choices)

print(count_choices_dict)


# {'[0, 0, 0, 1, 0, 0, 0, 0, 0]': 13114,
# '[0, 0, 0, 0, 0, 0, 0, 0, 1]': 52256, 
# '[1, 0, 0, 0, 0, 0, 0, 0, 0]': 353725, 
# '[0, 0, 0, 0, 1, 0, 0, 0, 0]': 30877, 
# '[0, 0, 0, 0, 0, 1, 0, 0, 0]': 29837, 
# '[0, 0, 1, 0, 0, 0, 0, 0, 0]': 14303, 
# 'None': 242, 
# '[0, 1, 0, 0, 0, 0, 0, 0, 0]': 2243,
# '[0, 0, 0, 0, 0, 0, 1, 0, 0]': 1952,
# '[0, 0, 0, 0, 0, 0, 0, 1, 0]': 1451}
# Elapsed time: 181.86165976524353 seconds