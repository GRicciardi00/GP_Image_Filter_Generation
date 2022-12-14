import os, sys, numpy
from os import listdir,makedirs
from os.path import isfile,join
from datetime import datetime



#TRAINING EDGE DETECTION
def edge_detection(size):
	path_original_edge_detection = 'dataset/train/train_edge_detection' #Full images folder
	path_expected_edge_detection = 'dataset/train/train_edge_detection/expected/nero' #Expected images folder 
	files_original_edge_detection = list(filter(lambda f: isfile(join(path_original_edge_detection,f)), listdir(path_original_edge_detection)))
	files_expected_edge_detection = list(filter(lambda f: isfile(join(path_expected_edge_detection,f)), listdir(path_expected_edge_detection)))
	for txt in files_original_edge_detection:
		if ".txt" in format(txt):
			datainputname = os.path.join(path_original_edge_detection,format(txt))
			dataresultname = os.path.join(path_expected_edge_detection,format(txt))
			os.system("python3 GP_edge_detection_3x3_random.py " + datainputname + " " + dataresultname + " " + folder_name)
			os.system("python3 GP_edge_detection_5x5_random.py " + datainputname + " " + dataresultname + " " + folder_name)

#TRAINING DENOISE
def denoise(size):
	path_original_noise = 'dataset/train/train_denoise/noise' #Full images folder
	path_expected_denoise = 'dataset/train/train_denoise' #Expected images folder 
	files_original_noise = list(filter(lambda f: isfile(join(path_original_noise,f)), listdir(path_original_noise)))
	files_expected_denoise = list(filter(lambda f: isfile(join(path_expected_denoise,f)), listdir(path_expected_denoise)))
	for txt in files_original_noise:
		if ".txt" in format(txt):
		    datainputname = os.path.join(path_original_noise,format(txt))
		    dataresultname = os.path.join(path_expected_denoise,format(txt))
		    if size == "1":
		        print("running 3x3 denoise of: " + format(txt))
		        os.system("python3 GP_denoise_3x3.py "+ datainputname + " " + dataresultname + " " + folder_name)
		    if size == "2":
		        print("running 5x5 denoise of: " + format(txt))
		        os.system("python3 GP_denoise_5x5.py "+ datainputname + " " + dataresultname + " " + folder_name)             

#SAVE RESULTS	
def save_results(size,task):
	print("Saving results....")
	directories = [x[0] for x in os.walk(folder_name)]
	for folder in directories:
		files = list(filter(lambda f: isfile(join(folder,f)),listdir(folder)))
		for txt in files:
			if "_best.pkl" in format(txt) or "_best2.pkl" in format(txt) or "_best3.pkl" in format(txt) :
				if size == "1": 
					if task == "1":
						os.system("python3 create_img_from_gp_3x3_denoise.py " + folder + "/" + txt + " " + folder_name)
					if task == "2":
						os.system("python3 create_img_from_gp_3x3_edge.py " + folder + "/" + txt + " " + folder_name)
				if size == "2":
					if task == "1":
						os.system("python3 create_img_from_gp_5x5_denoise.py " + folder + "/" + txt + " " + folder_name)
					if task == "2":
						os.system("python3 create_img_from_gp_5x5_edge.py " + folder + "/" + txt + " " + folder_name)
			if "_logbook.pkl" in format(txt):
				os.system("python3 load_logbook.py " + folder + "/" + txt + " " + folder_name)
#MAIN		
folder_name =input("Insert folder name...")
try:
	os.makedirs(folder_name)
	os.makedirs(os.path.join(folder_name, 'results'))
except:
	print("folder with that name already exists, still continue with execution...")
size = input("Insert 1: 3x3 filter matrix size, 2: 5x5 filter matrix size")
mode = input("Insert 1: denoise, 2: edge detection, 3: only extract results")
if mode == "1":
	start_time = datetime.now()
	denoise(size);
	save_results(size,"1")
	end_time = datetime.now()
	print('Duration: {}'.format(end_time - start_time))
if mode == "2":
	start_time = datetime.now()
	edge_detection(size)
	save_results(size,"2")
	end_time = datetime.now()
	print('Duration: {}'.format(end_time - start_time))
if mode == "3":
	task=input("press 1 for denoise, 2 for edge detection...")
	start_time = datetime.now()
	save_results(size,task)
	end_time = datetime.now()
	print('Duration: {}'.format(end_time - start_time))


