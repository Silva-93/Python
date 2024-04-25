from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://www.python.org')

# a maneira mais comum de iniciar uma página web para navegação
driver.get("http://www.google.com")

# INTERAÇÃO COM A PÁGINA WEB

#     element = driver.find_element(By.ID, "passwd-id") -> Busca o elemento pelo ID
#     element = driver.find_element(By.NAME, "passwd") -> Busca o elemento pelo NOME
#     element = driver.find_element(By.XPATH, "//input[@id='passwd-id']") -> Busca o elemento pelo XPATH
#     element = driver.find_element(By.CSS_SELECTOR, "input#passwd-id") -> Busca o elemento pelo SELETOR CSS

