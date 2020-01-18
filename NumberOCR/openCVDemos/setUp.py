import cv2 as cv
import numpy as np
from os import listdir
from os.path import isfile, join


trainingImages = list(listdir('0'))
imLen = len(trainingImages)

trainingData = np.array([[0]], dtype='float')
trainingData = np.expand_dims(trainingData, axis=2)

print(trainingData.shape)


np.savetxt('data.csv', trainingData, delimiter=',', fmt='%s')
