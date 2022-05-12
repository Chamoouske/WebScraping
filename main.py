from factory.factory_chrome import Chrome
from factory.factory_firefox import Firefox
import time


def definir_navegador(navegador_usado = 'CHROME'):
    if navegador_usado.upper() == 'CHROME':
        navegador = Chrome()
    elif navegador_usado.upper() == 'FIREFOX':
        navegador = Firefox()
    return navegador


if __name__ == '__main__':
    navegador = definir_navegador('CHROME')
    navegador.get('https://www.mercadolivre.com.br/')
    navegador.pesquisar_produto('ssd', 'mercadolivre')
    time.sleep(1)
    navegador.pegar_valores_dos_resultados_da_pesquisa()
    navegador.quit()

