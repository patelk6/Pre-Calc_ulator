import numpy as np  
import matplotlib.pyplot as plt 
from sympy import *



x_int = [1,0]
y_int = [0,5]



def slope(x,y):
	return ((y[1]-y[0])/(x[1]-x[0]))

def eqOfLine(x_points,y_points):
	x = symbols('x')
	b_symbol = symbols('b')
	m = slope(x_points,y_points)
	myTerm = m * x_points[1] + b_symbol - y_points[1]
	b = (solve(myTerm,b_symbol))
	y = eval(m*x + b)
	plt.plot(np.array(10),y)

eqOfLine(x_int,y_int)