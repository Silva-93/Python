# """ 
#     Slot é um método que é executado quando um signal é disparado
# """

# import sys
# from PySide6.QtCore import Slot
# from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QGridLayout, QMainWindow

# app = QApplication(sys.argv)
# window = QMainWindow()
# central_widget = QWidget()  # widget(principal) onde terá outros widgets dentro dele. Ele sozinho não recebe outros widgets, é necessário criar um layout para receber outros widgets como mostra abaixo ↓
# window.setCentralWidget(central_widget)
# window.setWindowTitle('Minha Janela')

# layout = QGridLayout()
# central_widget.setLayout(layout)

# botao1 = QPushButton('Botão1')
# botao2 = QPushButton('Botão2')
# botao3 = QPushButton('Botão3')

# # Linha coluna row_span col_span
# layout.addWidget(botao1, 1, 1, 1, 1)
# layout.addWidget(botao2, 1, 2, 1, 1)
# layout.addWidget(botao3, 3, 1, 1, 2)

# botao1.setStyleSheet('font-size: 40px; color: red')

# @Slot
# def first_slot(status_bar):
#     def inner():
#         status_bar.showMessage('Slot executado!')
#     return inner

# @Slot
# def second_slot(checked):
#     print('Está marcado?', checked)

# @Slot
# def third_slot(action):
#     def inner():
#         second_slot(action.isChecked())
#     return inner

# # MSG de status da barra
# status_bar = window.statusBar()
# status_bar.showMessage('Mensagem da barra de status')

# # Menu da barra
# menu = window.menuBar()
# first_menu = menu.addMenu('Menu principal')
# first_action = first_menu.addAction('Primeira ação')
# first_action.triggered.connect(first_slot(status_bar))

# second_action = first_menu.addAction('Segunda ação')
# second_action.setCheckable(True)  # Opção de marcar e desmarcar 
# second_action.toggled.connect(second_slot)  # uma função conectada a um signal é chamada de slot
# second_action.hovered.connect(third_slot(second_action)) 

# botao1.clicked.connect(third_slot(second_action))  # Ao clicar no botão 1, ativa o third_slot()


# menu.triggered.connect(first_slot)

# window.show()
# app.exec()  # Executa o loop da aplicação

# O básico sobre Signal e Slots (eventos e documentação)
import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget)

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha janela bonita')

botao1 = QPushButton('Texto do botão')
botao1.setStyleSheet('font-size: 80px;')

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px;')

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px;')

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)


@Slot()
def slot_example(status_bar):
    def inner():
        status_bar.showMessage('O meu slot foi executado')
    return inner


@Slot()
def outro_slot(checked):
    print('Está marcado?', checked)


@Slot()
def terceiro_slot(action):
    def inner():
        outro_slot(action.isChecked())
    return inner


# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

# menuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro menu')
primeira_acao = primeiro_menu.addAction('Primeira ação')
primeira_acao.triggered.connect(slot_example(status_bar))  # type:ignore

segunda_action = primeiro_menu.addAction('Segunda ação')
segunda_action.setCheckable(True)
segunda_action.toggled.connect(outro_slot)  # type:ignore
segunda_action.hovered.connect(terceiro_slot(segunda_action))  # type:ignore

botao1.clicked.connect(terceiro_slot(segunda_action))  # type:ignore

window.show()
app.exec()  # O loop da aplicação