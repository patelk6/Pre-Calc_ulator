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
		
for i in range(int(numberOfPieces)):
	function = input("Enter " + str(i+1) + " function ")
	listOfFunctions.append(cleanInput(function))

def cleanBounds(bounds):
		
	for bound in bounds:
		if(bound.find('<') + 1 or bound.find('>') + 1):
			
def generateBounds(bounds):
	numbered_bounds = []
	
	for i in range(len(bounds)-1):
		print("In function")
		#print(np.arange(bounds[i],bounds[i+1],1))
		#print(np.arange(int(bounds[i]),int(bounds[i+1],1)))
		
		numbered_bounds.append(np.arange(bounds[i],bounds[i+1]))
	
	return numbered_bounds
	
#bounds = getBounds(listOfFunctions)
output_bounds = generateBounds(cleanBounds(bounds))
print(output_bounds)

#print(listOfFunctions)

