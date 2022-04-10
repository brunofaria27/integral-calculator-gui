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
    [sg.Text('Equação'), sg.Input(key='equacao', size=(50, 50))],
    [sg.Button('Calcular'), sg.Button('Informações')],
    [sg.Text('Resultado:'), sg.Text('', key='_OUTPUT_')]
]

# Janela que irá ser aberta pelo usuário
janela = sg.Window('Calculadora de Integral', layout)

# Ler os eventos - enquanto o evento for verdadeiro a janela continuará aparecendo para o usuário
while True:
    eventos, valores = janela.read() # Guardar valores e eventos dentro de duas variaveis, para consulta futura
    if eventos == sg.WINDOW_CLOSED:
        break # Sai do looping fechando a janela (Encerra o programa)
    if eventos == 'Calcular': # Caso o botão de calcular seja apertado
        try: # Irá tentar resolver a integral e mostrar para o usuário
            calc = calculadora(valores['equacao'])
            janela.Element('_OUTPUT_').Update(calc)
        except: # Senão irá mostrar uma mensagem de erro para o usuário
            error_string = 'Error, escreva a equação novamente.'
            janela.Element('_OUTPUT_').Update(error_string)
    elif eventos == 'Informações':  # Caso o botão de informações seja apertado, irá mostrar informações sobre símbolos
        sg.PopupOKCancel('Elevado: ** ', 'Dividido: / ', 'Vezes: * ', 'Menos: - ', 'Soma: + ')
