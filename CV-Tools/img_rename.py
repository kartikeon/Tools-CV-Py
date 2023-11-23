import os

os.getcwd()
dir_folder = "C:/Users/Karthik/Desktop/dk"
dir_folder_path = "C:/Users/Karthik/Desktop/dk/"

for i, filename in enumerate(os.listdir(dir_folder)):
    os.rename(dir_folder_path + filename, dir_folder_path + f"red_tld_mini_{i}.jpg")  # os.rename(old_name, new_name)
# os.rename(coll + filename, coll + str(i) + ".jpg")

# "C:/Xtream Drive/Projects/Pycharm Projects/tld_1/Red_TDL_mini"
