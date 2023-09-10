""" 
pip install PySide6
pip install -U napari-deeplabcut

    QApplication 
        QMainWindow
            centralWidget
                Layout
                    widget
                    widget
                    widget
            show
    exec()

"""

import PySide6.QtCore

# Versão do PySide6
print(PySide6.__version__)

# Versão do QtCore compilado com o PySide6
print(PySide6.QtCore.__version__)

