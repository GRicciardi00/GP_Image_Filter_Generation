from PIL import Image
import numpy as np
from sklearn import metrics 
from os import listdir,makedirs
from os.path import isfile,join
import matplotlib.pyplot as plt
import operator, random, pickle,sys, os, time, math,glob
import seaborn as sns

truth_labels = np.loadtxt("label/157036.txt").astype(int)
y_prediction = np.loadtxt("closing/sobel_3x3.txt").astype(int)
negative = 0.0
positive = 255.0
tp = np.sum(np.logical_and(y_prediction == positive, truth_labels == positive))
tn = np.sum(np.logical_and(y_prediction == negative, truth_labels == negative))
fp = np.sum(np.logical_and(y_prediction == positive, truth_labels == negative))
fn = np.sum(np.logical_and(y_prediction == negative, truth_labels == positive))
precision = tp/(tp + fp)
recall = tp/(tp + fn)
F1 = 2*((precision*recall)/(precision+recall))
print("true positive: " + str(tp))
print("true negative: " + str(tn))
print("false positive: " + str(fp))
print("false negative: " + str(fn))
print("recall: " + str(recall))
print("precision: " + str(precision))
accuracy = (tp+tn)/(tp+tn+fp+fn)
cm_data = [[(tn/(tn+fp)),(fp/(tn+fp))], [(fn/(tp+fn)),(tp/(tp+fn)) ]]
sns.heatmap(cm_data, annot=True, cmap='Blues')
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()
print("F1 score: " + str(accuracy))
