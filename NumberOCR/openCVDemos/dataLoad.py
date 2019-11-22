import cv2 as cv
import csv
import numpy as np



testArr = np.array([[0,0,1],
					[1,1,1],
					[1,0,1],
					[0,1,1]], dtype='float')

np.savetxt("data.csv", testArr, delimiter=',')
loadArr = np.loadtxt("data.csv", delimiter=',')

print(loadArr)