from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from .navegador import Navegador


def Factory(navegador='chrome'):
    navegadores = {
        "chrome": Chrome,
        "firefox": Firefox,
    }

    return navegadores[navegador]()


class Chrome(Navegador):
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--headless')
        service = ChromeService(ChromeDriverManager().install())
        self.navegador = webdriver.Chrome(service=service, chrome_options=options)


class Firefox(Navegador):
    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
        service = FirefoxService(GeckoDriverManager().install())
        self.navegador = webdriver.Firefox(service=service,firefox_profile=options)
