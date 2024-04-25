from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# instância do Firefox
driver = webdriver.Firefox()

# abre a URL passada, caso a página seja iniciado com AJAX, o webdriver pode não saber se foi totalmente iniciado
driver.get('http://www.python.org')

# "Verifica" se o título tem a palavra Python
assert 'Python' in driver.title

# By. fprocura elementos da página name, id, value, class...
elem = driver.find_element(By.NAME, 'q')

# limpa qualquer texto pré-escrito no campo
elem.clear()

# informa o que será escrito no campo pesquisa
elem.send_keys('pycon')

# Keys. aciona uma tecla do teclado, nesse caso, enter
elem.send_keys(Keys.RETURN)

# a mensagem será exibida se o elemento não for encontrato na página
assert 'no results found' not in driver.page_source

# fecha o navegador
driver.close()
