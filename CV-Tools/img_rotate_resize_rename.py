import os
from PIL import Image

os.getcwd()

dir_folder = "C:/Users/Karthik/Desktop/dk"
dir_folder_path = "C:/Users/Karthik/Desktop/dk/"

size = (640, 320)  # (l, b)
degree = 180

for i, filename in enumerate(os.listdir(dir_folder)):
    im = Image.open(dir_folder_path + filename)  # open file
    im = im.resize(size)  # resize the file
    #  im = im.rotate(degree)  # degrees counter-clockwise
    im.save(dir_folder_path + filename)  # save the file
# os.rename(coll + filename, coll + f"mini_green_{i}_dg_90.jpg")  # os.rename(old_name, new_name)
