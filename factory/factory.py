from selenium import webdriver

from utils.paths import resource_path
from .factory_navegador import Navegador


def Factory(navegador='chrome'):
    navegadores = {
        "chrome": Chrome,
        "firefox": Firefox
    }

    return navegadores[navegador]


class Chrome(Navegador):
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        self.navegador = webdriver.Chrome(resource_path('./driver/chromedriver.exe'), chrome_options=options)


class Firefox(Navegador):
    def __init__(self):
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        self.navegador = webdriver.Firefox(resource_path('./drive/geckodriver.exe'),firefox_profile=profile)
