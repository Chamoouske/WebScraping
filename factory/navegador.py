import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from log.main import *
from utils.vars_utils import *
from utils.window import *


class Navegador:
    create_logger('factory_navegador.log')
    site_atual = None

    produto = None

    lista_sites_produtos = []
    lista_nomes_produtos = []
    lista_valores_produtos = []
    lista_links_produtos = []

    nome_tabela = ''
    tabela_produtos = None

    sites_usados = lista_sites


    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Navegador, cls).__new__(cls, *args, **kwargs)
        return cls._instance


    def get(self, ir_para):
        self.navegador.get(ir_para)


    def quit(self):
        info('Saindo do navegador')
        self.navegador.quit()


    def sleep(self, tempo = 2):
        time.sleep(tempo)


    def pesquisar_produto(self, produto = False):
        if produto != False:
            self.salvar_produto_pesquisado(produto)
            self.proximo_site(True)
                
        mensagens.config(text='Pesquisando produto', fg='blue')
        info(f'Pesquisando produto: {self.produto}')
        elemento = self.navegador.find_element(By.XPATH, xpaths_e_links[self.site_atual]['input_search'])
        elemento.send_keys(self.produto, Keys.ENTER)
        self.pegar_valores_dos_resultados_da_pesquisa()


    def salvar_produto_pesquisado(self, produto):
        self.produto = produto


    def proximo_site(self, pesquisar_produto_chamou = False):
        if len(self.sites_usados) > 0:
            proximo_site = self.sites_usados.pop(0)
            self.site_atual = proximo_site

            info(f'Vai para o site: {proximo_site}')
            self.get(xpaths_e_links[self.site_atual]['site'])

            self.verificar_popups_cookies()
            if not pesquisar_produto_chamou:
                self.pesquisar_produto()
        else:
            info('Não há mais sites para pesquisar')
            self.salvar_tabela_produtos()

    
    def verificar_popups_cookies(self):
        try:
            info('Verificando popups e cookies')
            elemento = self.navegador.find_element(By.XPATH, xpaths_e_links[self.site_atual]['verificar_popups'])
            if elemento.is_displayed():
                elemento.click()
            self.fechar_popups_cookies()
        except:
            info('Não há popups ou cookies')


    def fechar_popups_cookies(self):
        try:
            info('Fechando popups e cookies')
            elemento = self.navegador.find_element(By.XPATH, xpaths_e_links[self.site_atual]['fechar_popups'])
            if elemento.is_displayed():
                elemento.click()
        except:
            info('Não há popups ou cookies de fechamento')


    def pegar_valores_dos_resultados_da_pesquisa(self):
        valores_produtos = []
        nomes_resultados = []
        links_resultados = []
        try:
            self.sleep(2)
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

        except Exception as err:
            error(f'Erro ao coletar os dados: {str(err)}')
            valores_produtos = []
            nomes_resultados = []
            links_resultados = []
        finally:
            info('Os valores dos resultados da pesquisa foram coletados')
            self.salvar_resultados_da_pesquisa_da_pagina_atual(valores_produtos, nomes_resultados, links_resultados)


    def conta_as_listas_do_resultado_da_pesquisa(self):
        return len(self.navegador.find_elements(By.XPATH, xpaths_e_links[self.site_atual]['verificar_layout']))


    def salvar_resultados_da_pesquisa_da_pagina_atual(self,valores_produtos, nomes_resultados,links_resultados):
        self.sleep(2)
        try:
            for i in range(0, len(valores_produtos)):
                self.lista_sites_produtos.append(self.site_atual)
                self.lista_nomes_produtos.append(nomes_resultados[i].text)
                self.lista_valores_produtos.append(valores_produtos[i].text.replace('R$ ', '').replace('.', '').replace(',', '.'))
                self.lista_links_produtos.append(links_resultados[i].get_attribute('href'))

            info('Os resultados da pesquisa da página atual foram salvas em listas')
        except Exception as err:
            error(f'Erro ao salvar os resultados em listas: {str(err)}')
        finally:
            self.ir_para_a_pagina_seguinte()


    def ir_para_a_pagina_seguinte(self):
        self.sleep(2)
        try:
            elemento = self.navegador.find_element(By.XPATH, f'{xpaths_e_links[self.site_atual]["proxima_pagina"]}')
            if elemento.is_displayed():
                elemento.click()
                info('Indo para a próxima página')
                self.pegar_valores_dos_resultados_da_pesquisa()
            else:
                self.proximo_site()

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

            self.tabela_produtos.to_excel(f'{self.nome_tabela}.xlsx', index=False)
            info('Tabela de produtos salva com sucesso')
            self.reset_lists()
            mensagens.config(text="Tabela de produtos salva com sucesso!!!", fg="green")
        except Exception as err:
            mensagens.config(text='Erro ao salvar a tabela como arquivo excel', fg='red')
            error(f'Erro ao salvar a tabela como arquivo excel: {str(err)}')
        finally:
            self.quit()

    def reset_lists(self):
        self.sites_usados = lista_sites
