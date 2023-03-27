
import os
import shutil

directory = 'Data'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        #parent_dir = "Data"
        #path = os.path.join(parent_dir, f[:-5])
        os.mkdir(f[:-5])
        shutil.move(f, f[:-5])
