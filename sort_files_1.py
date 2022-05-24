import shutil
import os

# originals
file_source = "FilesToSort"
file_list = os.listdir(file_source)

for file in file_list:
    # check file list
    if os.path.isdir(file):
        pass
    # get extension in list
    file_extension = file.split(".")[-1]
    # file name/file extension(normal format)
    if os.path.exists(file_source + "/" + file_extension):
        # move to new folder, change the path to get new folder
        shutil.move(file_source + "/" + file, file_source + "/" + file_extension + "/" + file)
    else:
        # create a new folder
        os.mkdir(file_source + "/" + file_extension)
        shutil.move(file_source + "/" + file, file_source + "/" + file_extension + "/" + file)
