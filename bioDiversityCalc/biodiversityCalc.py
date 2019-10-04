import json

fileName = input("Input file name: ") #Dataset
outputFileName = input("Output file name: ") #Summary Table

#Loading JSON
with open(fileName) as json_file:
	data = json.load(json_file)

#Var
outputData = {}
commonNames = []
numberOfSpecies = 0


for i in range(0,len(data)):
	if i != 0: #Edge cases
		if data[i]['Scientific'] == data[i-1]['Scientific']: #Listing number of each species
			outputData[data[i]['Scientific']] += 1 #Counting number of species
		else:
			outputData[data[i]['Scientific']] = 1 #Starting new species
			commonNames.append(data[i]['Common'])

			numberOfSpecies += 1
	else: #Edge Case
		outputData[data[i]['Scientific']] = 1 #Starting the algorithm
		numberOfSpecies += 1
		commonNames.append(data[i]['Common'])

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
relBioDiversity = srd/numberOfSpecies


#Output for Simpsons reciprocal diversity index
print(outputData)
print("\n######################################\n")
print("The number of different species were: " + str(numberOfSpecies))
print("\nThe Simpson Reciprocal Index of the dataset was " + str(srd))
print("\nThe relative biodiversity of " + fileName + " is " + str(round(relBioDiversity * 100, 1000)) + "%.")


######Summary Table#########

#Altering File name
outputFileName = "SummaryDataTable-" + outputFileName + ".txt"

sumTab = open(outputFileName, 'w+') #Create file

dataList = list(outputData) #gets a list of all species names

sumTab.write('Scientific,Common,SpeciesVal \n')

for i in range(0, len(outputData)):
	sumTab.write(dataList[i] + "," + commonNames[i] + "," + str(speciesIndividualVal[i]) + "\n") #Adds data to txt file
#User can convert to csv by renaming






