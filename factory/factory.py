from selenium import webdriver

from utils.paths import resource_path
from .navegador import Navegador


def Factory(navegador='chrome'):
    navegadores = {
        "chrome": Chrome,
        "firefox": Firefox,
        "edge": Edge
    }

    return navegadores[navegador]()


class Chrome(Navegador):
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--headless')
        self.navegador = webdriver.Chrome(resource_path('.driver/chromedriver.exe'), chrome_options=options)


class Firefox(Navegador):
    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
        self.navegador = webdriver.Firefox(resource_path('.driver/geckodriver.exe'),firefox_profile=options)


class Edge(Navegador):
    def __init__(self):
        options = webdriver.EdgeOptions()
        options.headless = True
        self.navegador = webdriver.Edge(resource_path('.driver/msedgedriver.exe'), options=options)
