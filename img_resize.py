from PIL import Image
import os, sys

path = os.path.dirname(os.path.realpath(__file__))
dirs = os.listdir(path+"/dataset/")

def resize():
    for item in dirs:
        file_path = path+"/dataset/"+item
        for filename in os.listdir(file_path):
            im = Image.open(file_path+"/"+filename)
            imResize = im.resize((150,150), Image.ANTIALIAS)
            imResize.save(path+"/dataset_resized/"+item+"/"+filename, 'JPEG', quality=90)
            # print(filename)
        # print(item)

resize()