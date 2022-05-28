# IMPORTS
import sys
from sympy import exp, log, pprint
from sympy.abc import x
# IMPORTS DIRETORIOS
import calculos

# Pegar o tipo de equacao que o usuario quer fazer
print("SELECIONE ALGUM TIPO DE INTEGRAL PARA RESOLVER: \n\n")
print("Opcao letra A: ")
pprint((3 * x) / ((x + 1) * (x + 2)))
print("\n\nOpcao letra B: ")
pprint((2 * x) / (x ** 2 - 5 * x + 6))
print("\n\nOpcao letra C: ")
pprint((2 * x) / ((x - 1) * (x - 2) * (x - 4)))
opcao = input("\nSelecione a sua opcao: ")

print("NAO COLOQUE OS PARENTESIS: \n\n")
if opcao == 'A' or opcao == 'a':
    # PEGAR DADOS DO USUARIO, SOBRE A INTEGRAL
    limite_superior = int(input("\nInsira o limite superior: "))
    limite_inferior = int(input("\nInsira o limite inferior: "))
    numerador = int(input("\nNUMERADOR: Insira o valor que substitui ?: (? * x) -> "))
    denominador1 = int(input("\nInsira o denominador referente a posicao do ?: (x ?) -> "))
    denominador2 = int(input("\nInsira o denominador referente a posicao do ?: (x ?) -> "))
    # _______________________________________________________________________________________________________#
    # Resolucao dos calculos para resolver
    calculos.integralA(numerador, denominador1, denominador2, limite_superior, limite_inferior)
elif opcao == 'B' or opcao == 'b':
    # PEGAR DADOS DO USUARIO, SOBRE A INTEGRAL
    numerador = int(input("\nNUMERADOR: Insira o valor que substitui ?: (? * x) -> "))
    print("\nInsira uma equacao do segundo grau no estilo de (x ** 2 - 5 * x + 6): ")
    a = int(input("Coeficiente A: "))
    b = int(input("Coeficiente B: "))
    c = int(input("Coeficiente C: "))
    # _______________________________________________________________________________________________________#
    # Resolucao dos calculos para resolver
    calculos.integralB(a, b, c, numerador)
elif opcao == 'C' or opcao == 'c':
    # PEGAR DADOS DO USUARIO, SOBRE A INTEGRAL
    numerador = int(input("\nNUMERADOR: Insira o valor que substitui ?: (? * x) -> "))
    denominador1 = int(input("\nInsira o denominador referente a posicao do ?: (x ?) -> "))
    denominador2 = int(input("\nInsira o denominador referente a posicao do ?: (x ?) -> "))
    denominador3 = int(input("\nInsira o denominador referente a posicao do ?: (x ?) -> "))
    # _______________________________________________________________________________________________________#
    # Resolucao dos calculos para resolver
    calculos.integralC(numerador, denominador1, denominador2, denominador3)
else:
    print("Voce selecionou uma opcao invalida, utilize [A, B, C] ou [a, b, c]")
    sys.sleep(5)
    exit()
