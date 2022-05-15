from selenium import webdriver

from .factory_navegador import Navegador


class Firefox(Navegador):
    def __init__(self):
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        self.navegador = webdriver.Firefox(firefox_profile=profile)
