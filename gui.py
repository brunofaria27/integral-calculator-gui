# TASKS:
# - Criar um executável
# - Tratamento da integral
# - Tratamento de limite superior e inferior

from PySimpleGUI import PySimpleGUI as sg
from sympy import *

import os

def calculadora(equacao):
    init_printing()
    var('x')
    result = integrate(equacao, x)
    return result

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Equação'), sg.Input(key='equacao', size=(50, 50))],
    [sg.Button('Calcular'), sg.Button('Informações')],
    [sg.Text('Resultado:'), sg.Text('', key='_OUTPUT_')]
]

# Janela
janela = sg.Window('Calculadora de Integral', layout)

# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Calcular':
        try:
            calc = calculadora(valores['equacao'])
            janela.Element('_OUTPUT_').Update(calc)
        except:
            error_string = 'Error, escreva a equação novamente.'
            janela.Element('_OUTPUT_').Update(error_string)
    elif eventos == 'Informações':
        sg.PopupOKCancel('Elevado: ** ', 'Dividido: / ', 'Vezes: * ', 'Menos: - ', 'Soma: + ')
