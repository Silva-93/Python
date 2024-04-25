import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# herança TestCase, informa ao python que esse código é um caso de teste
class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.drive = webdriver.Chrome()  # criando a instância do chrome

    def test_search_in_python_org(self):
        drive = self.drive
        drive.get('http://www.python.org')
        self.assertIn('Python', drive.title)
        elem = drive.find_element(By.NAME, 'q')
        elem.send_keys('pycon')
        elem.send_keys(Keys.RETURN)
        self.assertNotIn('No results found', drive.page_source)

    def tearDown(self):
        self.drive.close()


if __name__ == '__main__':
    unittest.main()
