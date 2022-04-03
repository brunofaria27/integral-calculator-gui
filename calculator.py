from sympy import *

init_printing()
var('x')
result = integrate(1/(x**2-4), x)
print(result)