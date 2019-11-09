import tkinter as tk

from neural_network import NeuralNetwork
# from dataSave import DataSave

#GUI Constants
padx = 15
pady = 5
lightGray = '#b8b6b6'
darkGray = '#333333'
whiteGray = '#e0e0e0'


#GUI Start
root = tk.Tk()
root.title("Neural Network")
root.configure(background=darkGray)

#Inputs
inputFrame = tk.LabelFrame(root, text='Training Data File Path')
inputFrame.config(background=darkGray, fg=whiteGray, relief='sunken')
inputFrame.grid(row=0, column=0, sticky='W', padx=padx, pady=pady)

inputEnt = tk.Text(inputFrame, background=lightGray, height=1, width=40)
inputEnt.config(highlightbackground=whiteGray, font=("Courier", 18))
inputEnt.grid(row=0, column=0, padx=padx, pady=pady)

inputSubmit = tk.Button(inputFrame, text="Train Neural Network", width=40, height=2)
inputSubmit.grid(row=0, column=1, padx=padx, pady=pady)

#Synaptic Weights
weightFrame = tk.LabelFrame(root, text="Synaptic Weights")
weightFrame.config(background=darkGray, fg=whiteGray, relief='sunken')
weightFrame.grid(row=1, column=0, padx=padx, pady=pady)

weightEnt = tk.Text(weightFrame, background=lightGray, width=60, height=1)
weightEnt.config(highlightbackground=whiteGray, font=("Courier", 18))
weightEnt.grid(row=0, column=0, columnspan=2, padx=padx, pady=pady)

saveWeight = tk.Button(weightFrame, text="Save Synaptic\nWeights", width=40, height=2)
saveWeight.grid(row=1, column=0, padx=padx, pady=pady)
loadWeight = tk.Button(weightFrame, text="Load Synaptic\nWeights", width=40, height=2)
loadWeight.grid(row=1, column=1, padx=padx, pady=pady)

#Predict Data
outputFrame = tk.LabelFrame(root, text="Synaptic Weights")
outputFrame.config(background=darkGray, fg=whiteGray, relief='sunken')
outputFrame.grid(row=2, column=0, padx=padx, pady=pady)



root.mainloop()