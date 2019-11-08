import numpy as np

class NeuralNetwork():
    
    def __init__(self):
        #np.random.seed(##)  Optional Seed
        
        self.ilSize = 10
        self.hlSize = 3
        self.olSize = 4

        self.input = {}
        
        #2 * x - 1 makes it so that the random number is between -1 and 1
        self.synIL = 2 * np.random.random((self.ilSize,self.hlSize)) - 1  #Connects layer input layer to HL1
        self.synHL0 = 2 * np.random.random((self.hlSize,self.olSize)) - 1 #Connects HL1 to output layer

    #Normalizing Functions
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    def sigmoid_deriv(self, x):
        return 1 * (1 - x)

    #Cost
    def costFnc(self, arr):
        return 
    
    #Train
    def train(self, data, syns, iters):
        for i in range(iters):
            l0 = data["layer0"] #IL
            l1 = self.sigmoid(np.dot(l0, syns[0]))
            l2 = self.sigmoid(np.dot(l1, syns[1]))

            print(i)


