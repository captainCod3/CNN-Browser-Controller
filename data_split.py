import os
import sys
import shutil
path = os.path.dirname(os.path.realpath(__file__))
dirs = os.listdir(path+"/dataset/")
train_path = path+"/data/train/"
val_path = path+"/data/validation/"
def resize():
    for item in dirs:
        file_path = path+"/dataset/"+item
        x = len(os.listdir(file_path))
        train_x = int(0.8*x)
        validation_x = x-train_x
        tr = 0
        val = 0
        for filename in os.listdir(file_path):
            if tr <= train_x:
                newPath = shutil.copy(file_path+"/"+filename, train_path+item)
                tr=tr+1 
            elif val <= validation_x:
                newPath  = shutil.copy(file_path+"/"+filename, val_path+item)
                val=val+1


resize()






            
            
