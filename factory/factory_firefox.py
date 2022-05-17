from selenium import webdriver

from utils.paths import resource_path
from .factory_navegador import Navegador


class Firefox(Navegador):
    def __init__(self):
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        self.navegador = webdriver.Firefox(resource_path('./drive/geckodriver.exe'),firefox_profile=profile)
