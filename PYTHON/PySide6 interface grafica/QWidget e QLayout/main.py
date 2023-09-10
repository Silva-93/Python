""" 
    Janela com mais de um widget (Janela principal)
"""

import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QGridLayout

app = QApplication(sys.argv)

central_widget = QWidget()  # widget(principal) onde terá outros widgets dentro dele. Ele sozinho não recebe outros widgets, é necessário criar um layout para receber outros widgets como mostra abaixo ↓

layout = QGridLayout()
central_widget.setLayout(layout)

botao = QPushButton('Botão')
botao2 = QPushButton('Botão2')
botao3 = QPushButton('Botão3')

# Linha coluna row_span col_span
layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1,)

botao.setStyleSheet('font-size: 40px; color: red')

central_widget.show()  # Adiciona o widget na hierarquia e exibe a janela


app.exec()  # Executa o loop da aplicação