from PIL import Image
import numpy as np
import os, sys, numpy
from os import listdir,makedirs
from os.path import isfile,join
from datetime import datetime

PATH_FILTER_DENOISE_3X3 = 'denoise3x3/Denoise_Execution_20221122_121623/67079_best.pkl'
PATH_FILTER_EDGE_DETECTION_3X3 = '3x3-random/Edge_detection_Execution_2022121_02044/135069_best.pkl'
PATH_FILTER_DENOISE_5X5 = 'denoise5x5/Denoise_Execution_20221122_12834/65074_best.pkl'
PATH_FILTER_EDGE_DETECTION_5X5 = '5x5-random/Edge_detection_Execution_2022121_24138/157055_best.pkl'


def apply_filter_denoise(size, folder_name):
	
	path_input_denoise_image = 'dataset/test/noise' 
	files_input_denoise_image = list(filter(lambda f: isfile(join(path_input_denoise_image,f)), listdir(path_input_denoise_image)))
	for txt in files_input_denoise_image:
		if ".txt" in format(txt):
			file_name = 'dataset/test/denoise' + "/" + format(txt)
			file_name = file_name.split('.',1)[0]
			datainputname = os.path.join(path_input_denoise_image,format(txt))
			if size == "1":
				print("running 3x3 denoise of: " + format(txt))
				os.system("python3 test_img_from_gp_3x3_denoise.py "+ PATH_FILTER_DENOISE_3X3 + " " + 'dataset/test/denoise' + " " + datainputname + " " + file_name)
			if size == "2":
					print("running 5x5 denoise of: " + format(txt))
					os.system("python3 test_img_from_gp_5x5_denoise.py "+ PATH_FILTER_DENOISE_3X3 + " " + 'dataset/test/denoise' + " " + datainputname + " " + file_name)

def convert_denoised_image():
	path_input_denoise_image = 'dataset/test/denoise/'
	files_input_denoise_image = list(filter(lambda f: isfile(join(path_input_denoise_image,f)), listdir(path_input_denoise_image)))
	for image in files_input_denoise_image:
		if ".bmp" in format(image):
			try:
				img = Image.open(os.path.join(path_input_denoise_image,image)).convert('L')
				img_resized = img.resize((128,128))
				dstPath = join(path_input_denoise_image,image)
				bnarray = np.array(img_resized)
				filename_noise = path_input_denoise_image + format(image)
				filename_noise = os.path.splitext(filename_noise)[0]
				filename_noise =  filename_noise + ".txt"
				np.savetxt(filename_noise,np.uint8(bnarray), fmt="%d")
			except:
				print ("{} is not converted".format(image))
	print("txt noise images conversion finished")

def apply_filter_edge_detection(size, folder_name):
	print("Saving results....")
	path_input_edge_image = 'dataset/test/denoise'  
	files_input_edge_image = list(filter(lambda f: isfile(join(path_input_edge_image,f)), listdir(path_input_edge_image)))
	for txt in files_input_edge_image:
		if ".txt" in format(txt):
			file_name= folder_name + "/" + format(txt)
			datainputname = os.path.join(path_input_edge_image,format(txt))
			if size == "1":
				print("running 3x3 edge detection of: " + format(txt))
				os.system("python3 test_img_from_gp_3x3_edge.py "+ PATH_FILTER_EDGE_DETECTION_3X3 + " " + 'dataset/test/denoise' + " " + datainputname + " " + file_name)
			if size == "2":
					print("running 5x5 edge detection of: " + format(txt))
					os.system("python3 test_img_from_gp_5x5_edge.py "+ PATH_FILTER_EDGE_DETECTION_5X5 + " " + 'dataset/test/denoise' + " " + datainputname + " " + file_name)
			
#MAIN		
folder_name =input("Insert folder name...")
try:
	os.makedirs(folder_name)
except:
	print("folder with that name already exists, still continue with execution...")
size = input("Insert 1: 3x3 filter matrix size, 2: 5x5 filter matrix size")
start_time = datetime.now()
apply_filter_denoise(size,folder_name)
convert_denoised_image()
apply_filter_edge_detection(size,folder_name)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

