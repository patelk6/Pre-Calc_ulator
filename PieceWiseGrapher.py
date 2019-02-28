import numpy as np  
import matplotlib.pyplot as plt  
from sympy import *

numberOfPieces = input ("Enter number of pieces ")

listOfFunctions = []
bounds = []
def cleanInput(formula):
	outFormula = ''
	
	for i in range(len(formula)):

		if(formula[i] == '^'):
			outFormula = outFormula + '**'
		else:
			outFormula = outFormula + formula[i]

	
	return outFormula

def parseBounds(formula):
	for i in range(len(formula)):
		
	
for i in range(int(numberOfPieces)):
	function = input("Enter " + str(i+1) + " function ")
	listOfFunctions.append(cleanInput(function))
	
print(listOfFunctions)
	
	
