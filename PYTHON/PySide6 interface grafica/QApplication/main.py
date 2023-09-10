""" 
    O QApplication é uma aplicação que não mostra nada na tela, um dos widget que é assim. Ele gerencia um loop de eventos da plicação.

    Widget é tudo que está na tela 
"""
import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

botao = QPushButton('Botão')
botao.setStyleSheet('font-size: 40px; color: red')

botao.show()  # Adiciona o widget na hierarquia e exibe a janela


app.exec()  # Executa o loop da aplicação