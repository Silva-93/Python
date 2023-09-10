""" 
    Janela com mais de um widget (Janela principal)
"""

import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QGridLayout, QMainWindow

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()  # widget(principal) onde terá outros widgets dentro dele. Ele sozinho não recebe outros widgets, é necessário criar um layout para receber outros widgets como mostra abaixo ↓
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha Janela')

layout = QGridLayout()
central_widget.setLayout(layout)

botao1 = QPushButton('Botão1')
botao2 = QPushButton('Botão2')
botao3 = QPushButton('Botão3')

# Linha coluna row_span col_span
layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

botao1.setStyleSheet('font-size: 40px; color: red')

def slot_exemple(status_bar):
    status_bar.showMessage('Slot executado!')

# MSG de status da barra
status_bar = window.statusBar()
status_bar.showMessage('Mensagem da barra de status')

# Menu da barra
menu = window.menuBar()
first_menu = menu.addMenu('Menu principal')
first_action = first_menu.addAction('Primeira ação')
first_action.triggered.connect(lambda: slot_exemple(status_bar))

menu.triggered.connect(slot_exemple)

window.show()
app.exec()  # Executa o loop da aplicação