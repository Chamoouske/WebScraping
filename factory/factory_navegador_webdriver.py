from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

xpath_base_result_mercado_livre = '//*[@id="root-app"]/div/div[1]/section/ol/li'
xpaths = {
    'mercado_livre': {
        'input_search_mercado_livre': '//*[@id="cb1-edit"]',
        'verificar_layout_mercado_livre': '//*[@id="root-app"]/div/div[1]/section/ol',
        'valores_resultados_mercado_livre_layout_1':
            f'{xpath_base_result_mercado_livre}/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]',
        'nomes_resultados_mercado_livre_layout_1':
            f'{xpath_base_result_mercado_livre}/div/div/div[2]/div[1]/a/h2',
        'valores_resultados_mercado_livre_layout_2':
            f'{xpath_base_result_mercado_livre}/div/div/a/div/div[1]/div/div/div/span[1]/span[2]/span[2]',
        'nomes_resultados_mercado_livre_layout_2': f'{xpath_base_result_mercado_livre}/div/div/a/div/div/h2'
    }
}


class Navegador:
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        return super(Navegador, cls).__new__(cls, *args, **kwargs)

    def get(self, ir_para):
        self.navegador.get(ir_para)

    def quit(self):
        self.navegador.quit()

    def pesquisar_produto(self, produto, site):
        elemento = self.navegador.find_element(By.XPATH, self.xpath_usado_para_pesquisa(site))
        elemento.send_keys(produto)
        elemento.send_keys(Keys.ENTER)

    def xpath_usado_para_pesquisa(self, site):
        if site == 'mercadolivre':
            return xpaths['mercado_livre']['input_search_mercado_livre']

    def pegar_valores_dos_resultados_da_pesquisa(self):
        try:
            if self.conta_as_ols_do_resultado_da_pesquisa() > 1:
                valores_resultados = self.navegador.find_elements(By.XPATH,
                                                                  xpaths['mercado_livre']
                                                                  ['valores_resultados_mercado_livre_layout_2'])
                nomes_resultadis = self.navegador.find_elements(By.XPATH,
                                                                xpaths['mercado_livre']
                                                                ['nomes_resultados_mercado_livre_layout_2'])
            else:
                valores_resultados = self.navegador.find_elements(By.XPATH,
                                                                  xpaths['mercado_livre']
                                                                  ['valores_resultados_mercado_livre_layout_1'])
                nomes_resultadis = self.navegador.find_elements(By.XPATH,
                                                                xpaths['mercado_livre']
                                                                ['nomes_resultados_mercado_livre_layout_1'])
            for i in range(0, len(valores_resultados)):
                print(f'{i + 1} -> {nomes_resultadis[i].text}: R${valores_resultados[i].text}')
        except:
            print('Erro ao pegar os valores na página')

    def conta_as_ols_do_resultado_da_pesquisa(self):
        return len(self.navegador.find_elements(By.XPATH, xpaths['mercado_livre']['verificar_layout_mercado_livre']))
