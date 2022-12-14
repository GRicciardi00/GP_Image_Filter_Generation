#UTILIZZO DI OPENCV PER PARAGONARE RISULTATI OTTENUTI DALLA GP CON METODI COMUNI DI EDGE DETECTION E DENOISING

import numpy as np 
import sys,cv2,os, glob
from os import listdir,makedirs
from os.path import isfile,join

#DENOISE
def denoise():
    img = cv2.imread('dataset/train/train_denoise/noise/11046.jpg',0) #insert your image to process here
    img = cv2.resize(img, (128,128))
    blur = cv2.GaussianBlur(img,(5,5),0) #(3,3)= dimensione kernel
    noiseless_image_bw = cv2.fastNlMeansDenoising(img, None, 20, 5, 21)
    cv2.imwrite("blur.jpg", blur)
    cv2.imwrite("Nlmeans.jpg", noiseless_image_bw)

#EDGE DETECTION
# loading image
def edge_detection(): 
    img0 = cv2.imread('dataset/train/train_edge_detection/163014.tiff',) #insert your image to process here
    img = cv2.resize(img0, (128,128))
    laplacian = cv2.Laplacian(img,cv2.CV_64F,ksize=5)
    sobel = cv2.Sobel(img,cv2.CV_64F,1,1,ksize=5)
    ret,sobel = cv2.threshold(sobel,29,255,cv2.THRESH_BINARY)
    ret,laplacian = cv2.threshold(laplacian,20,255,cv2.THRESH_BINARY)
    cv2.imwrite("laplacian.jpg", laplacian)
    cv2.imwrite("sobel.jpg", sobel)

def test_set():
    path_input_image = 'dataset/test/noise/'
    files_input_image = list(filter(lambda f: isfile(join(path_input_image,f)), listdir(path_input_image)))
    for image in files_input_image:
        if ".jpg" in format(image):
            img = cv2.imread((path_input_image+image)) #insert your image to process here
            img = cv2.resize(img, (128,128))
            blur = cv2.GaussianBlur(img,(3,3),0) #(3,3)= dimensione kernel
            laplacian = cv2.Laplacian(blur,cv2.CV_64F,ksize=3)
            sobel = cv2.Sobel(blur,cv2.CV_64F,1,1,ksize=3)  # x #
            destination = "dataset/test/image_processing/"
            ret,sobel = cv2.threshold(sobel,20,255,cv2.THRESH_BINARY)
            ret,laplacian = cv2.threshold(laplacian,20,255,cv2.THRESH_BINARY)
            cv2.imwrite( destination + "sobel_3x3_" + format(image), sobel)
            cv2.imwrite( destination + "laplacian_3x3_" + format(image), laplacian )
    print("denoise image processing on test set finished")

test_set()
#denoise()
#edge_detection()
