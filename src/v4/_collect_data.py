## Use the Jupyter Notebook instead

print("Use the Jupyter Notebook instead")


# import os
# import time
# import cv2
# import numpy as np
# from grabscreen import grab_screen
# from getkeys import key_check

# key_map = {
#     'W': [1, 0, 0, 0, 0, 0, 0, 0, 0],
#     'S': [0, 1, 0, 0, 0, 0, 0, 0, 0],
#     'A': [0, 0, 1, 0, 0, 0, 0, 0, 0],
#     'D': [0, 0, 0, 1, 0, 0, 0, 0, 0],
#     'WS': [0, 0, 0, 0, 1, 0, 0, 0, 0],
#     'WD': [0, 0, 0, 0, 0, 1, 0, 0, 0],
#     'SA': [0, 0, 0, 0, 0, 0, 1, 0, 0],
#     'SD': [0, 0, 0, 0, 0, 0, 0, 1, 0],
#     'NK': [0, 0, 0, 0, 0, 0, 0, 0, 1],
#     'default': [0, 0, 0, 0, 0, 0, 0, 0, 0],
# }

# starting_value = 1

# while True:
#     file_name = 'training_data-{0}.npy'.format(starting_value)
#     if os.path.isfile(file_name):
#         print('File exists, moving along', starting_value)
#         starting_value += 1
#     else:
#         print('File does not exist, starting fresh!', starting_value)
#         break


# def keys_to_output(keys):
#     if ''.join(keys) in key_map:
#         return key_map[''.join(keys)]
#     return key_map['default']


# def main(file_name, starting_value):
#     training_data = []
#     for i in list(range(4))[::-1]:
#         print(i + 1)
#         time.sleep(1)

#     last_time = time.time()
#     paused = False
#     print('STARTING!!!')
#     while True:
#         if not paused:
#             screen = grab_screen(region=(0, 40, 1920, 1120))
#             last_time = time.time()
#             screen = cv2.resize(screen, (480, 270))
#             screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
#             keys = key_check()
#             output = keys_to_output(keys)
#             training_data.append([screen, output])

#             if len(training_data) % 100 == 0:
#                 print(len(training_data))
#                 if len(training_data) == 100:
#                     np.save(file_name, np.array(training_data))
#                     print('SAVED')
#                     training_data = []
#                     starting_value += 1
#                     file_name = 'training_data-{0}.npy'.format(starting_value)

#         keys = key_check()
#         if 'T' in keys:
#             if paused:
#                 paused = False
#                 print('Unpaused!')
#                 time.sleep(1)
#             else:
#                 print('Pausing!')
#                 paused = True
#                 time.sleep(1)


# if __name__ == "__main__":
#     main(file_name, starting_value)
