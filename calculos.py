import math
import numpy
from sympy import Matrix, log, solve, solve_linear_system_LU, symbols

def raizesSegundoGrau(a, b, c):
    # Achar as raizes da equacao do segundo grau
    delta = b ** 2 - (4 * a * c)
    x1 = (- b + math.sqrt(delta) ) / (2 * a)
    x2 = (- b - math.sqrt(delta) ) / (2 * a)
    return x1, x2

def integralB(a, b, c, numerador):
    raiz1, raiz2 = raizesSegundoGrau(a, b, c)
    subs1, subs2 = inverteParaZerar(raiz1, raiz2)
    valorA = (numerador * subs1) / (subs1 + raiz2)
    valorB = (numerador * subs2) / (subs2 + raiz1)
    print("RESULTADO = " + str(valorA) + f" * ln(x{subs1:+})" + f"{valorB:+}" + f" * ln(x{subs2:+})" + " + C")

def integralA(numerador, denominador1, denominador2, limiteSuperior, limiteInferior):
    subs1, subs2 = inverteParaZerar(denominador1, denominador2)
    valorA = (numerador * subs1) / (subs1 + denominador2)
    valorB = (numerador * subs2) / (subs2 + denominador1)
    solve_fun = float((valorA * log(limiteSuperior + denominador1)) + (valorB * log(limiteSuperior + denominador2)))
    solve_fun2 = float((valorA * log(limiteInferior + denominador1)) + (valorB * log(limiteInferior + denominador2))) 
    print("RESULTADO = %.2f" %(solve_fun - solve_fun2))

def integralC(numerador, denominador1, denominador2, denominador3):
    value_a1 = denominador2 * denominador3
    if denominador3 < 0:
        value_a2 = denominador2 + denominador3
    else:
        value_a2 = denominador2 - denominador3

    value_b1 = denominador1 * denominador3
    if denominador3 < 0:
        value_b2 = denominador1 + denominador3
    else:
        value_b2 = denominador1 - denominador3

    value_c1 = denominador1 * denominador2
    if denominador2 < 0:
        value_c2 = denominador1 + denominador2
    else:
        value_c2 = denominador1 - denominador2

    a, b, c = symbols('a b c')
    solve = solve_linear_system_LU(Matrix([[1, 1, 1, 0], [value_a2, value_c2, value_b2, numerador], [value_a1, value_c1, value_b1, 0]]), [a, b, c])

    concat1 = float(solve.get(a))
    concat2 = float(solve.get(b))
    concat3 = float(solve.get(c))
    
    if concat1 < 0:
        concat1 = f' %.2f' %concat1
    else:
        concat1 = f'+ %.2f' %concat1
    
    if concat2 < 0:
        concat2 = f' %.2f' %concat2
    else:
        concat2 = f'+ %.2f' %concat2

    if concat3 < 0:
        concat3 = f' %.2f' %concat3
    else:
        concat3 = f'+ %.2f' %concat3

    print("RESULTADO = " + str(concat2) + f"ln(x{denominador1:+})" + str(concat1) + f" * ln(x{denominador2:+})" + str(concat3) + f" * ln(x{denominador3:+})" + " + C")

def inverteParaZerar(valor1, valor2):
    novoValor = 0
    novoValor2 = 0

    if valor1 < 0:
        novoValor = abs(valor1)
    
    if valor2 < 0:
        novoValor2 = abs(valor2)
    
    if valor1 > 0:
        novoValor = valor1 * (-1)
    
    if valor2 > 0:
        novoValor2 = valor2 * (-1)

    return novoValor, novoValor2
