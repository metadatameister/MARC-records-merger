import shutil
import glob

with open('output_file.mrc', 'wb') as outfile:
    for i in glob.glob(r'c:/files/*.mrc'):
    #this line takes every file with .mrc extension in c:/files/ folder and iterates them through a loop
        with open(i, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)
