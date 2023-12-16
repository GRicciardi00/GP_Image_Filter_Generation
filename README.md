# GENERAZIONE DI FILTRI OTTIMI PER IMMAGINI TRAMITE PROGRAMMAZIONE GENETICA

## LIBRARIES
The implementation is compatible only with Linux OS.
- Opencv
- DEAP
- Numpy
- PIL
- Matplotlib
- Graphviz
## ABOUT IT
The project aim to generate filters for denoising and edge detection using Genetic Programming (GP).
The algorithm for generating noise reduction filters has 30x30 size samples input of the images with noise and as a label the same samples without noise, the objective of the algorithm is to minimise the value of the fitness function defined as the MSE (average quadratic error) between the image processed by the filter and the reference image. To evolve programs, the algorithm needs a set of terminal nodes T and a set of functions F: the mathematical operations of sum, subtraction, multiplication, division and arithmetic mean represent the set F. The results of these operations are limited between 0 and 255 because a pixel can only take these values and also the division by 0 has been protected. The terminal nodes are represented by the elements of the window whose filter is being generated; the evolution for the denoise algorithm lasts 40 generations of a population of 400 individuals. <br />
A very similar approach to that seen for the denoise task was used for the creation of filters for the edge detection task, the training starts from 30x30 samples of the training images and their references (represented by the images in which only the edges are visible). The set of functions F differs from that used for dennoising for the addition of square root, absolute value and elevation to square operations; the domain of these operations has been enlarged to values ranging from -255 to 255 as the filter must detect negative as well as positive discontinuities. Compared to the task of denoise, the evolution is longer, being planned 300 generations of 400 individuals. <br />
In the test phase, some denoise filters and some edge detection filters generated on the training set on the images of the test set were applied in series to evaluate how generalizable the results obtained were. The results show that the filters obtained are applicable with similar results even on images on which they have not been trained.
## HOW TO USE
The dataset folder contains all the images used for training and testing and the various algorithms used for preliminary operations on them.
For the training run the file 'GP_training.py' and follow the guide on the terminal, then you can run the test with the filters obtained by modifying the file 'GP_test.py' by setting the paths of the necessary _best.pkl files.
The ''image_processing.py'' file uses openCV to edit images with common methods of edge detection and denoise.
The 'results' folder has the algorithm used to evaluate the results obtained.









