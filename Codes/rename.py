import os

path = os.chdir(
    'C:\\Users\\Karma Wangchuk\\Desktop\\Thesis\\CaptureImage\\Augment\\30.Aa')

i = 0
for file in os.listdir(path):
    new_file_name = 'Aa-{}.jpg'.format(i)
    os.rename(file, new_file_name)
    i = i + 1
