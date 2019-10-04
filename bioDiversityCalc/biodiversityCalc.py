import json

fileName = input("Input file name: ")

#Loading JSON
with open(fileName) as json_file:
	data = json.load(json_file)

#Var
outputData = {}
numberOfSpecies = 0


for i in range(0,len(data)):
	if i != 0: #Edge cases
		if data[i]['Scientific'] == data[i-1]['Scientific']: #Listing number of each species
			outputData[data[i]['Scientific']] += 1 #Counting number of species
		else:
			outputData[data[i]['Scientific']] = 1
			numberOfSpecies += 1
	else: #Edge Case
		outputData[data[i]['Scientific']] = 1 #Starting the algorithm
		numberOfSpecies += 1

#Simpson's reciprocal diversity Index
speciesIndividualVal = list(outputData.values())
denom = 0
num = 0

#Calculating denominator
for i in range(0,len(speciesIndividualVal)):
	denom += speciesIndividualVal[i]*(speciesIndividualVal[i]+1)

#Calculating numerator
num = numberOfSpecies*(numberOfSpecies+1)

print(num)
print(denom)

srd = num/denom


print(outputData)
print("The number of different species were: " + str(numberOfSpecies))
print("The Simpson Reciprocal Index of the dataset was " + str(srd))