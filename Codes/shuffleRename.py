import random
import os

path = os.chdir(
    r'C:\Users\Karma Wangchuk\Desktop\Thesis\CaptureImage\Number\9Nine')
lst = os.listdir(path)
random.shuffle(lst)
print(lst)

for j in range(50):
    i = 0
    for file in os.listdir(path):
        Newfile_name = 'alpha{}-{}.jpg'.format(j, i)
        os.rename(file, Newfile_name)
        i = i + 1
    print('Shuffle Number ', j)

k = 1
for file in os.listdir(path):
    Newfile_name = 'Nine{}.jpg'.format(k)
    os.rename(file, Newfile_name)
    k = k + 1
