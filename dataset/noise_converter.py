import cv2
import os,glob
from os import listdir,makedirs
from os.path import isfile,join
import numpy as np
from random import choice
from random import uniform
#noise_types = ["gauss","s&p","poisson"]
MEAN = round(uniform(1.5,30), 4)
VAR = round(uniform(1.5,30), 4)
SIGMA = round(uniform(1.5,30), 4)
print("mean: " + str(MEAN) + "; VAR: " + str(VAR) + "; SIGMA: " + str(SIGMA))
def noisy(image):
    #if noise_typ == "gauss":
    row,col,ch= image.shape
    mean = MEAN
    var = VAR
    sigma = SIGMA
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    return noisy
    """
    elif noise_typ == "s&p":
        print("s&p")
        row,col,ch = image.shape
        s_vs_p = 0.4
        amount = round(uniform(0.0005,0.008), 8)
        out = np.copy(image)
        # Salt mode
        num_salt = np.ceil(amount * image.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt))
                  for i in image.shape]
        out[tuple(coords)] = 255
        # Pepper mode
        num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper))
                  for i in image.shape]
        out[tuple(coords)] = 0
        return out
    elif noise_typ == "poisson":
        print("poisson")
        vals = len(np.unique(image))
        vals = round(uniform(1,25), 4)
        noisy = np.random.poisson(image * vals) / float(vals)
        return noisy
    """

##ADD_NOISE
path = 'train/train_denoise/'
dstpath = 'train/train_denoise/noise' # Destination Folder
try:
    makedirs(dstpath)
except:
    print ("Directory already exist, images will be written in same folder")
files = list(filter(lambda f: isfile(join(path,f)), listdir(path)))
for image in files:
    try:
        print("{}".format(image))
        img = cv2.imread(os.path.join(path,image))
        noise_img = noisy(img)
        dstPath = join(dstpath,image)
        cv2.imwrite(dstPath,noise_img)
    except:
        print ("{} is not converted".format(image))
for fil in glob.glob("*.jpg"):
    try:
        image = cv2.imread(fil) 
        gray_image = noisy(image) # add noise 
        cv2.imwrite(os.path.join(path,fil),noise_image)
    except:
        print('{} is not converted')

print("noise added")


