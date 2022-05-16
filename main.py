from factory.factory_chrome import Chrome
from factory.factory_firefox import Firefox
from log.main import *


def main():
    create_logger('main.log')


def definir_navegador(navegador_usado = 'CHROME'):
    if navegador_usado.upper() == 'CHROME':
        navegador = Chrome()
    elif navegador_usado.upper() == 'FIREFOX':
        navegador = Firefox()
    return navegador


if __name__ == '__main__':
    main()
    navegador = definir_navegador('CHROME')
    navegador.pesquisar_produto('redmi note 8 pro')

