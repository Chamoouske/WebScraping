<p align="center">
    <img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESNVOLVIMENTO&color=GREEN&style=for-the-badge" algin="center"/>
</p>

# Descrição sobre o projeto
<p>Este projeto é um web scraping de alguns e-commerces, como Mercado Livre, Magazine Luiza, Amazon*, Americanas*, entre outros.</p>

<sub>* Implementações futuras</sub>

# Função do projeto
<p>Este projeto tem como objetivo mapear e-commerces ao realizar a pesquisa de um determinado produto, informado pelo usuário. E gerar um arquivo excel contendo os valores, links e nomes dos produtos retornados como resultado da pesquisa feita nesses sites.</p>

# Pré-requisitos para rodar o projeto
## Instalação das bibliotecas usadas
        pip install -r requirements.txt
## Possuir o webdriver do navegador que será usado
<li><a href="https://chromedriver.chromium.org/downloads" target="_blank">Webdriver Chrome</a></li>
<li><a href="https://github.com/mozilla/geckodriver/releases" target="_blank">Webdriver Firefox</a></li>

# Modo de usar
<p>O método de uso ainda está amarrado no código, dentro do arquivo <code><a href="main.py">main.py</a></code>, onde tem uma função nomeada <code>pesquisar_produto</code>, a qual recebe uma <code>string</code> como parâmetro, então o selenium vai em cada site registrado no arquivo <code><a href="utils/vars_utils.py">vars_utils.py</a></code>, que contém informações sobre os sites que serão mapeados, como os xpaths dos inputs de pesquisa, botões/links para avançar para a próxima página, e também o link principal dos e-commerces que estão sendo mapeados.</p>
