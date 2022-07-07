# Wrap Scraper - Diário de Bordo

## Libraries

Requests

BeautifulSoup

re
## IDE

PyCharm
Colab

## Etapas do projeto

1. Estudei a documentação de requests e beautifulSoup e procurei exemplos práticos de como utilizar as bibliotecas

1. Analisei o código da página dos artigos, identificar as div corretas para fazer a raspagem foi um tanto trabalhoso.

1. Comecei a estruturar o código, primeiro programei a base do código, depois que consegui fazer o script ser executado sem erros, comecei a formatar os dados filtrados

1. Aproveitei para incremetar o script fazendo a raspagem de outros dados da página, além do título do artigo e do link que foi pedido no teste, utilizei o "subtítulo" do artigo e a da que foi postado.

1. Para melhorar a visualização dos dados utilizei a biblioteca re. Utilizei o re.sub em duas situações:

    5.1 O link do artigo era extraído a partir de "/africa", utilizei o re.sub para substituir a "/" por "https://qz.com/", deixando assim o link clicavel

    5.2  Para utilizar os dados da Data, utilizei novamente o re.sub, os dados eram extraídos da seguinte forma "Quartz Africa • DATA", usei o re.sub para substituir o "Quartz       Africa • " por "Posted:"

## References 
Requests 2.27.1 documentation:
https://pypi.org/project/requests/

BeautifuSoup documentation:
https://www.crummy.com/software/BeautifulSoup/bs4/doc/#differences-between-parsers

Real Python - Beautiful Soup: Build a Web Scraper With Python:
https://realpython.com/beautiful-soup-web-scraper-python/

Otávio Miranda - Expressões regulares em Python - Parte 1:
https://www.youtube.com/watch?v=wBI0yv2FG6U

Programação Dinâmica - RASPAGEM de DADOS com PYTHON usando BeautifulSoup | Python na Prática #9:
https://www.youtube.com/watch?v=kqvWOcPog4s&t=608s


 
