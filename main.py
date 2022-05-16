from factory.factory_chrome import Chrome
from factory.factory_firefox import Firefox
from log.main import *


from tkinter import *
from utils.window import *


def main():
    create_logger('main.log')
    global mensagens
    global navegador

def pesquisar_produto(produto = '', browser = 'chrome', nome_tabela = 'tabela_produtos'):
    if produto != '':
        navegador = definir_navegador(browser, nome_tabela)
        navegador.pesquisar_produto(produto)
    else:
        mensagens.config(text='Digite um produto', fg='red')
        

def definir_navegador(browser = 'chrome', nome_tabela = 'tabela_produtos'):
    if browser == 'firefox':
        navegador = Firefox()
    else:
        navegador = Chrome()
    navegador.nome_tabela = nome_tabela
    return navegador

    
def pegar_nome_tabela():
    return tabela.get() if tabela.get() != '' else 'tabela_produtos'

def set_command_botoes():
    botao_chrome.config(width=25, command=lambda: pesquisar_produto(produto.get(), 'chrome', pegar_nome_tabela()))
    botao_firefox.config(width=25, command=lambda: pesquisar_produto(produto.get(), 'firefox', pegar_nome_tabela()))


if __name__ == '__main__':
    main()
    set_command_botoes()
    mensagens.config(text='Informe um produto para iniciar o sistema\nDepois clique no botão do navegador usado', fg='blue')
    janela.mainloop()


