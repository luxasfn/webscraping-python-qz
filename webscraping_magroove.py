#bibliotecas utilizadas
import requests
from bs4 import BeautifulSoup
import re

#extraindo os dados da página
article_page = "https://qz.com/africa/latest/"
qz = requests.get(article_page)
soup = BeautifulSoup(qz.content, "html.parser")

#recorte
elements = soup.find_all(class_ = "_8OV9v _1dOXL")

#filtrando os dados
for element in elements:
    title = element.find("div", class_="esSAQ _8S5gh")
    subtitle = element.find("div", class_="f01AT aGNvr _5yjC0")
    link = element.find('a')['href']
    data = element.find("div", class_="eDfJP aGNvr")

    print("Title:", title.text)
    print("Subtitle:", subtitle.text)
    print("Link:", re.sub(r'/', 'https://qz.com/', link))
    print(re.sub(r'Quartz Africa •', 'Posted:', data.text))
    print()


