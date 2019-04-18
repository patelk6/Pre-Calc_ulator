import numpy as np  
import matplotlib.pyplot as plt  
from sympy import *
def graph(formula, x_range):  
	x = np.array(x_range)  
	print(x)
	#y = eval(formula)	
	y = np.piecewise('x', [('x < 0, x >= 0 , x>5')], [lambda 'x': 'x**2',lambda 'x':'2' , lambda 'x':'x**3'])
	plt.plot(x, y)

	
def cleanInput(formula):
	outFormula = ''
	
	for i in range(len(formula)):

		if(formula[i] == '^'):
			outFormula = outFormula + '**'
		else:
			outFormula = outFormula + formula[i]

	
	return outFormula
#function = input('Enter function')
function = "x**2+x+1"
cleaned = cleanInput(function)

left = input('Left bound')
right = input('right bound')

#graph(function, range(int(left),int(right)))

#function = input('Enter function')
cleaned = cleanInput(function)
graph(cleaned, list(range(int(left),int(right))))

plt.show()

#print(cleaned)

#graph(cleaned, range(-10, 11))