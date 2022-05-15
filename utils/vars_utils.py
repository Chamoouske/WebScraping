lista_sites = ['mercado_livre', 'magazine_luiza']

xpath_base_result_mercado_livre = '//*[@id="root-app"]/div/div[1]'
xpath_base_result_magazine_luiza = '//*[@id="__next"]/div/main/section[4]'

xpaths_e_links = {
    'mercado_livre': {
        'site': 'https://www.mercadolivre.com.br/',
        'input_search': '//*[@id="cb1-edit"]',
        'verificar_layout': '//*[@id="root-app"]/div/div[1]/section/ol',

        'valores_resultados_layout_1':
            f'{xpath_base_result_mercado_livre}\
                /section/ol/li/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]',
        'nomes_resultados_layout_1':
            f'{xpath_base_result_mercado_livre}/section/ol/li/div/div/div[2]/div[1]/a/h2',
        'links_resultados_layout_1': f'{xpath_base_result_mercado_livre}/section/ol/li/div/div/div[2]/div[1]/a[1]',

        'valores_resultados_layout_2':
            f'{xpath_base_result_mercado_livre}/section/ol/li/div/div/a/div/div[1]/div/div/div/span[1]/span[2]/span[2]',
        'nomes_resultados_layout_2': f'{xpath_base_result_mercado_livre}/section/ol/li/div/div/a/div/div/h2',
        'links_resultados_layout_2': f'{xpath_base_result_mercado_livre}/section/ol/li/div/div/div[1]/a',

        'verificar_popups': '/html/body/div[2]/div[1]/div[2]/button[1]',
        'fechar_popups': '/html/body/div[2]/div[2]/div/button',
        'proxima_pagina': f'{xpath_base_result_mercado_livre}/section/div/ul/li[last()]/a',
    },

    'magazine_luiza': {
        'site': 'https://www.magazineluiza.com.br/',
        'input_search': '//*[@id="input-search"]',
        'verificar_layout': f'{xpath_base_result_magazine_luiza}/div[3]/div/ul',

        'valores_resultados_layout_1': f'{xpath_base_result_magazine_luiza}/div[3]/div/ul/li/a/div[3]/div[2]/div/p[1]',
        'nomes_resultados_layout_1': f'{xpath_base_result_magazine_luiza}/div[3]/div/ul/li/a/div[3]/h2',
        'links_resultados_layout_1': f'{xpath_base_result_magazine_luiza}/div[3]/div/ul/li/a',

        'verificar_popups': '//*[@id="__next"]/div/main/div[1]/div[2]/button',
        'fechar_popups': '',
        'proxima_pagina': f'{xpath_base_result_magazine_luiza}/div[4]/nav/ul/li[9]/button',
    }
}