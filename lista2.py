import requests
from bs4 import BeautifulSoup
import datetime
import re
from listaTemas import temas, linksPorTema


def main(url, tema):
    pattern = r'srcset="([^"]+)"'  # re

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    livros = soup.find_all(
        'div', class_='sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16')
    linksBook = soup.find_all('a', class_='a-link-normal s-no-outline')
    imagens = soup.find_all(
        'div', class_='a-section aok-relative s-image-fixed-height')

    nomeLivros = []
    linkLivros = []
    imagensLivrs = []

    for itens in imagens:
        img = itens.find('img', class_='s-image')
        match = re.search(pattern, str(img))
        if match:
            links = match.group(1).split(", ")
            last_link = links[-1].split()[0]
            imagensLivrs.append(last_link)

    for itens in livros:
        nome = itens.find(
            'span', class_='a-size-medium a-color-base a-text-normal').get_text()
        nomeArrumado = "" + nome.replace('"', "'")
        nomeLivros.append(nomeArrumado)

    for it in linksBook:
        linkDoLivro = it.get('href')
        linksCompletos = f'https://www.amazon.com.br{linkDoLivro}&linkCode=ll1&tag=ofertasespeciais-20'
        linkLivros.append(""+linksCompletos)
    escreveArquivo(linkLivros, nomeLivros, imagensLivrs, url, tema)

def escreveArquivo(linkLivros, nomeLivros, imagensLivrs, url, tema):
    with open('livros2.js', 'a', encoding='utf-8') as arquivo:
        try:
            for i in range(8):
                titulTema = tema
                urlBook = linkLivros[i]
                nameBook = nomeLivros[i]
                imgBook = imagensLivrs[i]
                objetoLivro = f'{{"imagem": "{imgBook}", "url": "{urlBook}", "nome": "{nameBook}", "tema" : "{titulTema}"}}\n'
                arquivo.write(objetoLivro)
                arquivo.write(',')
        except Exception as e:
            main(url, tema)
            print("exception " + tema)
        finally:
            print("executando " + tema)

    
    with open('livros2.js', 'r', encoding='utf-8') as arq:
        linhas = arq.readlines()
        if len(linhas) < 2:
            main(url, tema)



with open('livros2.js', 'w', encoding='utf-8') as arquivo:
    arquivo.write('export const listaLivros = [')

for i in range(29):
    main(linksPorTema[i], temas[i])

with open('livros2.js', 'a', encoding='utf-8') as arquivo:
    arquivo.write('];')
print("Fim")



            