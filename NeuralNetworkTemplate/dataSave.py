import json
import numpy as np

class DataSave():
    
    def __init__(self):
        self.outputData = {
            'input' : []
            # 'hl1' : []
            # 'hl2' : []
        }

    def formatData(self, input, hl):
        for i in range(hl):
            name = 'hl' + str(i+1)
            self.outputData[name] = []

    def read(self, fileName):
        with open(fileName, 'r') as raw:
            data = json.load(raw)
            print(data)

    def write(self, fileName, input):
        #NumPy Arrays
        if type(input['hl0']) == 'numpy.ndarray':
            for i in range(len(input)):
                name = 'hl' + i


        with open(fileName, 'w') as json_file:
            json.dump(input, json_file)



#Troubleshooting
if __name__ == "__main__":
    dataSave = DataSave()

    data = {
        "layer0" : np.array([[0,0,1], #Training Data
                             [-1,-1,1],
                             [1,0,-1],
                             [0,-1,1]])
    }
    print(type(data["layer0"]))
    print(dataSave.read('synaptic_weights.json'))