'''
usage: set the correct folders path and run the programm

'''

from PIL import Image
import numpy as np
import sys,os, glob
from os import listdir,makedirs
from os.path import isfile,join

path_denoise = 'train/train_denoise/' # denoise images Folder
path_noise = 'train/train_denoise/noise/' # noise images Folder
path_eq = 'train/train_equalization/' #Equalized images folder
path_deq = 'train/train_equalization/modified/' #Equalized images folder
path_noborder = 'train/train_edge_detection/' #Full images folder
path_border = 'train/train_edge_detection/expected/' #Border images folder 
path_border_black = 'train/train_edge_detection/expected/nero/' #Border images folder
files_noise = list(filter(lambda f: isfile(join(path_noise,f)), listdir(path_noise)))
files_denoise = list(filter(lambda f: isfile(join(path_denoise,f)), listdir(path_denoise)))
files_eq = list(filter(lambda f: isfile(join(path_eq,f)), listdir(path_eq)))
files_deq = list(filter(lambda f: isfile(join(path_deq,f)), listdir(path_deq)))
files_noborder = list(filter(lambda f: isfile(join(path_noborder,f)), listdir(path_noborder)))
files_border = list(filter(lambda f: isfile(join(path_border,f)), listdir(path_border)))
files_border_black = list(filter(lambda f: isfile(join(path_border_black,f)), listdir(path_border_black)))
for image in files_border_black:
        try:
                img = Image.open(os.path.join(path_border_black,image)).convert('L')
                img_resized = img.resize((128,128))
                dstPath = join(path_border_black,image)
                bnarray = np.array(img_resized)
                bnarray_new= bnarray
                bnarray_new[bnarray_new>=50]=255 
                bnarray_new[bnarray_new<50]=0
                filename_border = path_border_black + format(image)
                filename_border = os.path.splitext(filename_border)[0]
                filename_border =  filename_border + ".txt"
                print(filename_border)
                im = Image.fromarray(np.uint8(bnarray_new))
                im.save(filename_border+"_modified.png", "PNG")
                np.savetxt(filename_border,np.uint8(bnarray), fmt="%d")
        except:
                print ("{} is not converted".format(image))
print("txt black border images conversion finished")



