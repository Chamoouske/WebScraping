from selenium import webdriver
from .factory_navegador_webdriver import Navegador


class Firefox(Navegador):
    def __init__(self):
        self.navegador = webdriver.Firefox()
