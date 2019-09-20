import os
import shutil
from os import path

def single_file_rename():
    if path.exists("guru99.txt"):
        src = path.realpath("guru99.txt");
        os.rename("guru99.txt","guru.txt")

##### Rename multiple files #####
def multi_file_rename():
    i=0
    dir_path = "cwp"
    for filename in os.listdir(dir_path):
        dst = "Hostel" + str(i) + ".jpg"
        src = dir_path + dst
        os.rename(src,dst)

##### Start calling function  #####
if __name__ == "__main__"
    main()