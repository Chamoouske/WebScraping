import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from log.main import *
from utils.vars_utils import *


class Navegador:
    create_logger('factory_navegador.log')
    site_atual = None

    produto = None

    lista_sites_produtos = []
    lista_nomes_produtos = []
    lista_valores_produtos = []
    lista_links_produtos = []

    tabela_produtos = None

    sites_usados = lista_sites


    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        return super(Navegador, cls).__new__(cls, *args, **kwargs)


    def get(self, ir_para):
        self.navegador.get(ir_para)


    def quit(self):
        info('Saindo do navegador')
        self.navegador.quit()


    def pesquisar_produto(self, produto = False):
        if produto:
            self.salvar_produto_pesquisado(produto)
            self.proximo_site()
                
        info('Pesquisando produto')
        elemento = self.navegador.find_element(By.XPATH, xpaths_e_links[self.site_atual]['input_search'])
        elemento.send_keys(self.produto, Keys.ENTER)
        self.pegar_valores_dos_resultados_da_pesquisa()


    def salvar_produto_pesquisado(self, produto):
        self.produto = produto


    def proximo_site(self):
        if len(self.sites_usados) > 0:
            proximo_site = self.sites_usados.pop(0)
            self.site_atual = proximo_site
            self.get(xpaths_e_links[self.site_atual]['site'])

            info('Vai para o próximo site: {}'.format(proximo_site))
            self.verificar_popups_cookies()
            self.pesquisar_produto()
        else:
            info('Não há mais sites para pesquisar')
            self.salvar_tabela_produtos()

    
    def verificar_popups_cookies(self):
        try:
            info('Verificando popups e cookies')
            elemento = self.navegador.find_element(By.XPATH, xpaths_e_links[self.site_atual]['verificar_popups'])
            if elemento:
                elemento.click()
            self.fechar_popups_cookies()
        except:
            info('Não há popups ou cookies')


    def fechar_popups_cookies(self):
        try:
            info('Fechando popups e cookies')
            elemento = self.navegador.find_element(By.XPATH, xpaths_e_links[self.site_atual]['fechar_popups'])
            if elemento:
                elemento.click()
        except:
            info('Não há popups ou cookies')


    def pegar_valores_dos_resultados_da_pesquisa(self):
        try:
            time.sleep(3)
            valores_produtos = []
            nomes_resultados = []
            links_resultados = []
            if self.conta_as_listas_do_resultado_da_pesquisa() > 1:
                valores_produtos = self.navegador.find_elements(By.XPATH,
                                                                xpaths_e_links[self.site_atual]
                                                                ['valores_resultados_layout_2'])
                nomes_resultados = self.navegador.find_elements(By.XPATH,
                                                                xpaths_e_links[self.site_atual]
                                                                ['nomes_resultados_layout_2'])
                links_resultados = self.navegador.find_elements(By.XPATH, 
                                                                xpaths_e_links[self.site_atual]
                                                                ['links_resultados_layout_2'])
            else:
                valores_produtos = self.navegador.find_elements(By.XPATH,
                                                                xpaths_e_links[self.site_atual]
                                                                ['valores_resultados_layout_1'])
                nomes_resultados = self.navegador.find_elements(By.XPATH,
                                                                xpaths_e_links[self.site_atual]
                                                                ['nomes_resultados_layout_1'])
                links_resultados = self.navegador.find_elements(By.XPATH, 
                                                                xpaths_e_links[self.site_atual]
                                                                ['links_resultados_layout_1'])

            info('Pegando valores dos resultados da pesquisa')
        except:
            error('Erro ao pegar os valores na página')
    
        self.salvar_resultados_da_pesquisa_da_pagina_atual(valores_produtos, nomes_resultados, links_resultados)


    def conta_as_listas_do_resultado_da_pesquisa(self):
        return len(self.navegador.find_elements(By.XPATH, xpaths_e_links[self.site_atual]['verificar_layout']))


    def salvar_resultados_da_pesquisa_da_pagina_atual(self,valores_produtos, nomes_resultados,links_resultados):
        try:
            info('Salvando resultados da pesquisa da página atual em listas')
            for i in range(0, len(valores_produtos)):
                self.lista_sites_produtos.append(self.site_atual)
                self.lista_nomes_produtos.append(nomes_resultados[i].text)
                self.lista_valores_produtos.append(valores_produtos[i].text)
                self.lista_links_produtos.append(links_resultados[i].get_attribute('href'))

        except:
            error('Erro ao salvar os resultados da pesquisa')
        self.ir_para_a_pagina_seguinte()


    def ir_para_a_pagina_seguinte(self):
        try:
            elemento = self.navegador.find_element(By.XPATH, f'{xpaths_e_links[self.site_atual]["proxima_pagina"]}')
            if elemento:
                elemento.click()
                info('Indo para a próxima página')
                self.pegar_valores_dos_resultados_da_pesquisa()
        except:
            info('Não há mais páginas')
            self.proximo_site()


    def salvar_tabela_produtos(self):
        try:
            self.tabela_produtos = None
            self.tabela_produtos = pd.DataFrame({
                'site': self.lista_sites_produtos,
                'produto': self.lista_nomes_produtos,
                'valor': self.lista_valores_produtos,
                'link': self.lista_links_produtos
            })

            self.tabela_produtos.to_excel('tabela_produtos.xlsx', index=False)

            info('Tabela de produtos salva com sucesso')
        except:
            error('Erro ao salvar a tabela de produtos')
