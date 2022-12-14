'''
usage: set the correct folders path and run the programm

'''

from PIL import Image
import numpy as np
import sys,os, glob
from os import listdir,makedirs
from os.path import isfile,join

path_denoise = '3x3/' # denoise images Folder
path_noise = '5x5/' # noise images Folder
path_eq = 'closing/' #Equalized images folder
path_deq = 'closing/' #Equalized images folder
files_noise = list(filter(lambda f: isfile(join(path_noise,f)), listdir(path_noise)))
files_denoise = list(filter(lambda f: isfile(join(path_denoise,f)), listdir(path_denoise)))
files_eq = list(filter(lambda f: isfile(join(path_eq,f)), listdir(path_eq)))
files_deq = list(filter(lambda f: isfile(join(path_deq,f)), listdir(path_deq)))
"""
for image in files_noise:
	try:
		img = Image.open(os.path.join(path_noise,image)).convert('L')
		dstPath = join(path_noise,image)
		bnarray = np.array(img)
		filename_noise = path_noise + format(image)
		filename_noise = os.path.splitext(filename_noise)[0]
		filename_noise =  filename_noise + ".txt"
		np.savetxt(filename_noise,np.uint8(bnarray), fmt="%d")
	except:
		print ("{} is not converted".format(image))
print("txt noise images conversion finished")

for image in files_denoise:
	try:
		img = Image.open(os.path.join(path_denoise,image)).convert('L')
		dstPath = join(path_denoise,image)
		bnarray = np.array(img)
		filename_denoise = path_denoise + format(image)
		filename_denoise = os.path.splitext(filename_denoise)[0]
		filename_denoise =  filename_denoise + ".txt"
		np.savetxt(filename_denoise,np.uint8(bnarray), fmt="%d")
	except:
		print ("{} is not converted".format(image))
print("txt denoise images conversion finished")
"""
for image in files_eq:
	try:
		img = Image.open(os.path.join(path_eq,image)).convert('L')
		dstPath = join(path_eq,image)
		bnarray = np.array(img)
		bnarray = np.resize(bnarray,(128,128))
		bnarray[bnarray >= 20] = 255
		bnarray[bnarray < 20] = 0
		filename_eq = path_eq + format(image)
		filename_eq = os.path.splitext(filename_eq)[0]
		filename_eq =  filename_eq + ".txt"
		np.savetxt(filename_eq,np.uint8(bnarray), fmt="%d")
	except:
		print ("{} is not converted".format(image))
print("txt eq images conversion finished")
"""
for image in files_deq:
	try:
		img = Image.open(os.path.join(path_deq,image)).convert('L')
		dstPath = join(path_deq,image)
		bnarray = np.array(img)
		bnarray = np.resize(bnarray,(128,128))
		bnarray[bnarray >= 20] = 255
		bnarray[bnarray < 20] = 0
		filename_deq = path_deq + format(image)
		filename_deq = os.path.splitext(filename_deq)[0]
		filename_deq =  filename_deq + ".txt"
		np.savetxt(filename_deq,np.uint8(bnarray), fmt="%d")
	except:
		print ("{} is not converted".format(image))
print("txt deq images conversion finished")
"""

