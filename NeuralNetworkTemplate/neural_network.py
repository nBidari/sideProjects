import numpy as np


class NeuralNetwork():
    
    def __init__(self):
        np.random.seed(1) # Optional Seed
        
        self.ilSize = 3
        self.hlSize = 2
        self.olSize = 1

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
    def cost(self, output, label):
        return output - label #Output of program - correct output
    
    #Train
    def train(self, data, iters):
        for i in range(iters):
            l0 = data["layer0"] #IL
            l1 = self.sigmoid(np.dot(l0, self.synIL))
            l2 = self.sigmoid(np.dot(l1, self.synHL0))

            # Backpropogation
            # The derivative is always positive, and calculates the slope of a point on the cost function
            # The error can be positive or negative, allowing us to determine the "direction" that the weights need to go in order to reduce error
            l2Error = data["label"] - l2 #Calculate error
            l2Delta = self.sigmoid_deriv(l2) * l2Error #Calculate adjustement required to reduce error
            l1Error = np.dot(l2Delta, self.synHL0.T)
            l1Delta = self.sigmoid_deriv(l1) * l1Error

            #Adjusting synaptic weights
            self.synIL += np.dot(l0.T, l1Delta)
            self.synHL0 += np.dot(l1.T, l2Delta)

    def hypothesis(self, inputs): #Runs through program using an input, and the current synaptic weights
        l1 = self.sigmoid(np.dot(inputs["layer0"], self.synIL))
        l2 = self.sigmoid(np.dot(l1, self.synHL0))
        return l2



#Troubleshooting
if __name__ == "__main__": #Only runs when this specific file runs, not when other files refer to it
    neural_network = NeuralNetwork()

    print(f"sigmoid(0): {neural_network.sigmoid(0)}") #Testing sigmoid function (should output 0.5)
    print(f"Random synaptic weights: syn0 {neural_network.synIL} synHL0 {neural_network.synHL0}") #Outputting the generating synaptic weights

    data = {
        "layer0" : np.array([[0,0,1], #Training Data
                             [1,1,1],
                             [1,0,1],
                             [0,1,1]]),

        "label" : np.array([[0,1,1,0]]).T #Labels for the data
    }

    neural_network.train(data, 1000) #Training the neural network

    #User input
    A = int(input("A: "))
    B = int(input("B: "))
    C = int(input("C: "))

    #formatting the user input
    testInput = {
        "layer0" : np.array([A,B,C])
    }

    #Predicting outcome using trained synaptic weights
    prediction = neural_network.hypothesis(testInput)
    print(f"The prediction for [{A},{B},{C}] is {prediction}")
