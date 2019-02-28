from sympy import *

x = symbols('x')
y = symbols('y')

myTerm = (x**2 + 1) - y

#yTerm.subs(x,y)

print(solve(myTerm,y))

#have him put in an equation, and append a -y, so we can do the inverse