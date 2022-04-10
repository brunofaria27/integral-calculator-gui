# TASKS:
# - Criar um executável -> pyinstaller --onefile --noconsole .\gui.py
# - Tratamento da integral
# - Tratamento de limite superior e inferior
# - Comentários no código

from PySimpleGUI import PySimpleGUI as sg
from sympy import *

import os

# Função que recebe a equação de dentro da integral e calcula a soma infinita da área (integral)
# @param -> equacao a ser calculada
# @return -> resultado da integral
def calculadora(equacao):
    init_printing()
    var('x')
    result = integrate(equacao, x)
    return result

# Layout da página mostrada para o usuário
sg.theme('Reddit')
layout = [
    [sg.Button('Integral com limite')],
    [sg.Button('Integral equação segundo grau')],
    [sg.Button('Integral produto notável')]
]

layout2 = [
    [sg.Text('Insira a Equação:')],
    [sg.Text('Insira o limite superior:'), sg.Input(key='lim_superior', size=(4, 4))],
    [sg.Text('Insira o limite inferior:'), sg.Input(key='lim_inf', size=(4, 4))],
    [sg.Input(key='superior', size=(10, 10))],
    [sg.Text('------------------')],
    [sg.Input(key='denominador', size=(10, 10))],
    [sg.Button('Calcular'), sg.Button('Voltar')],
    [sg.Text('Resultado:'), sg.Text('', key='_OUTPUT_')]
]

# Janela que irá ser aberta pelo usuário
janelaSelecion = sg.Window('Selecione o tipo de Integral', layout)

# Ler os eventos - enquanto o evento for verdadeiro a janela continuará aparecendo para o usuário
while True:
    eventos, valores = janelaSelecion.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Integral com limite':
        janelaSelecion.hide()
        janelaLimite = sg.Window('Limite', layout2)

        eventos, valores = janelaLimite.read()
        if eventos == 'Calcular':
            try:
                calc = calculadora(valores['equacao'])
                janelaLimite.Element('_OUTPUT_').Update(calc)
            except:
                error_string = 'Error, escreva a equação novamente.'
                janelaLimite.Element('_OUTPUT_').Update(error_string)
        elif eventos == 'Voltar':
            janelaLimite.hide()
            janelaSelecion.un_hide()
    elif eventos == 'Integral equação segundo grau':
        janelaSelecion.hide()
    elif eventos == 'Integral produto notável':
        janelaSelecion.hide()

