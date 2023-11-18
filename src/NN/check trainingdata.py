import cv2
import pandas as pd

training_data = pd.read_pickle("training_data.pickle")

for index, row in training_data.iterrows():
    img = row[0]
    choice = row[1]

    cv2.imshow('test', img)
    print(choice)
    print(img.shape)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
