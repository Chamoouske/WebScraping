from tkinter import *

janela = Tk()
janela.title('Pesquisar produto')

texto_principal = Label(janela, text='Pesquisar produto:')
texto_principal.grid(row=0, column=1, padx=10, pady=10)

texto_produto = Label(janela, text='Produto:')
texto_produto.grid(row=1, column=0, padx=10, pady=10)
produto = Entry(janela)
produto.grid(row=1, column=1, padx=10, pady=10)

texto_tabela = Label(janela, text='Nome da tabela:')
texto_tabela.grid(row=2, column=0, padx=10, pady=10)
tabela = Entry(janela)
tabela.grid(row=2, column=1, padx=10, pady=10)

botao_chrome = Button(janela, text='Pesquisar usando o Chrome')
botao_chrome.grid(row=3, column=0, padx=10, pady=10)

botao_firefox = Button(janela, text='Pesquisar usando o Firefox')
botao_firefox.grid(row=3, column=2, padx=10, pady=10)

botao_edge = Button(janela, text='Pesquisar usando o Edge')
botao_edge.grid(row=3, column=1, padx=10, pady=10)

mensagens = Label(janela, text='')
mensagens.grid(row=4, column=1, padx=10, pady=10)