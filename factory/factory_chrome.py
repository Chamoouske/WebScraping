from selenium import webdriver

from utils.paths import resource_path
from .factory_navegador import Navegador


class Chrome(Navegador):
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        self.navegador = webdriver.Chrome(resource_path('./driver/chromedriver.exe'), chrome_options=options)
