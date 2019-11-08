import numpy as np

class NeuralNetwork():
    
    def __init__(self):
        #np.random.seed(##)  Optional Seed
        
        self.ilSize = 10
        self.hlSize = 3
        self.olSize = 4
        
        #2 * x - 1 makes it so that the random number is between -1 and 1
        self.synIL = 2 * np.random.random((self.ilSize,self.hlSize)) - 1  #Connects layer input layer to HL1
        self.synHL1 = 2 * np.random.random((self.hlSize,self.olSize)) - 1 #Connects HL1 to output layer

        
        