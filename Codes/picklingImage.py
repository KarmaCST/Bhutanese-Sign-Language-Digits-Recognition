import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm
import random
import pickle

#directory path
DATADIR = "./Number"

#Reading images from folder named Ozero, 1One, etc
CATEGORIES = ["0Zero", "1One", "2Two", "3Three",
              "4Four", "5Five", "6Six", "7Seven", "8Eight", "9Nine"]

IMG_SIZE = 64
training_data = []

def create_training_data():
    for category in CATEGORIES:  # from numbers 0-9

        path = os.path.join(DATADIR, category)  # create path for numbers
        # get the classification  (0 or a 1). 0=0Zero, 1=1One,..., 9=9Nine
        class_num = CATEGORIES.index(category)

        for img in tqdm(os.listdir(path)):  # iterate over each image per class
            try:
                img_array = cv2.imread(os.path.join(
                    path, img))  # convert to array
                img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
                # resize to normalize data size
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                # add this to our training_data
                training_data.append([new_array, class_num])
            except Exception as e:
                pass

create_training_data()
print(len(training_data))

random.shuffle(training_data)

X = []
y = []

for features, label in training_data:
    X.append(features)
    y.append(label)

print(X[0].reshape(-1, IMG_SIZE, IMG_SIZE, 3))

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 3)

pickle_out = open("X.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()
