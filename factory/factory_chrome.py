from selenium import webdriver

from .factory_navegador import Navegador


class Chrome(Navegador):
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        
        self.navegador = webdriver.Chrome(chrome_options=options)
