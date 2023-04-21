"""
    Locale para internacionalização
"""

import calendar
import locale 

locale.setlocale(locale.LC_ALL, '')  # Usando a localidade padrão do SO

print(calendar.calendar(2022))

