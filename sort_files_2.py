import shutil
import os

# originals
file_source = "FilesToSort"
file_list = os.listdir(file_source)
type_file = {}

for file in file_list:
    # check file list
    if os.path.isdir(file):
        pass
    # get extension in list
    file_extension = file.split(".")[-1]
    # user part
    folder = input("what category would you like to sort {} files into?".format(file_extension))
    type_file[file_extension] = folder

    # file name/file extension(normal format)
    if os.path.exists(file_source + "/" + file_extension):
        # move to new folder, change the path to get new folder
        shutil.move(file_source + "/" + file, file_source + "/" + file_extension + "/" + file)
    else:
        # create a new folder
        os.mkdir(file_source + "/" + file_extension)
        shutil.move(file_source + "/" + file, file_source + "/" + file_extension + "/" + file)