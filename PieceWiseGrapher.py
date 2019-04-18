import numpy as np  
import matplotlib.pyplot as plt  
from sympy import *

numberOfPieces = input ("Enter number of pieces ")

listOfFunctions = []
bounds = []
bounds.append("x>5")
bounds.append("x<5")

output_bounds = []
def cleanInput(formula):
	outFormula = ''
	
	for i in range(len(formula)):

		if(formula[i] == '^'):
			outFormula = outFormula + '**'
		else:
			outFormula = outFormula + formula[i]

	return outFormula

def getBounds(listOfFunctions):
	bounds = []
	for i in range(len(listOfFunctions)):
		bounds.append((input("Enter " + str(i) + " bound ")))
	return bounds	
		
def getFunctions(numberOfPieces):
	for i in range(int(numberOfPieces)):
		function = input("Enter " + str(i+1) + " function ")
		listOfFunctions.append(cleanInput(function))

def cleanBounds(bounds):
	outBounds = []
	left_bound = -10
	right_bound = 10
	outBounds.append(left_bound)
	for bound in bounds:
		
		if(bound.find('<') + 1 or bound.find('>') + 1):
			if(bound.find('<') + 1 and bound.find('>')+1):
				break
			else:
				if(int(bound[2:])<-10):
					outBounds.append(left_bound)
					
				elif(int(bound[2:])>10):
					outBounds.append(right_bound)
					
				else:
					outBounds.append(int(bound[2:]))
	outBounds.append(right_bound)
			
	return outBounds			
def generateBounds(bounds):
	numbered_bounds = []
	
	for i in range(len(bounds)-1):
		
		#print(np.arange(bounds[i],bounds[i+1],1))
		#print(np.arange(int(bounds[i]),int(bounds[i+1],1)))
		
		numbered_bounds.append(np.arange(int(bounds[i]),int(bounds[i+1])))
		print(np.arange(int(bounds[i]),int(bounds[i+1])))
	return numbered_bounds

def plotFunctions(functions,bounds):
	print(len(functions))
	print(len(bounds))
	for i in range(len(functions)):
		
		x = bounds[i]
		y = eval(functions(i))
		
		plt.plot(x,y)
		plt.show()
	
#bounds = getBounds(listOfFunctions)
listOfFunctions = getFunctions(numberOfPieces)
output_bounds = generateBounds(cleanBounds(bounds))
#print((output_bounds))
plotFunctions(listOfFunctions,output_bounds)




#print(listOfFunctions)

