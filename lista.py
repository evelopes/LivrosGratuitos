import requests
from bs4 import BeautifulSoup
import datetime
import re


def main():
    pattern = r'srcset="([^"]+)"'  # re

    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute

    data_atual = datetime.date.today()
    data_em_texto = data_atual.strftime('%d/%m/%Y')

    # LINK E CABEÇALHO DO SCRAP
    if 0 <= hour < 12:
        url = 'https://amzn.to/40Tudnz'
    elif 12 <= hour < 18:
        url = 'https://amzn.to/3UvzdN2'
    elif 18 <= hour < 22:
        url = 'https://amzn.to/3KN1cEv'
    else:
        url = 'https://amzn.to/3MqqTvY'

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
    escreveArquivo(linkLivros, nomeLivros, imagensLivrs)

def escreveArquivo(linkLivros, nomeLivros, imagensLivrs):
    with open('livros.js', 'w', encoding='utf-8') as arquivo:
        arquivo.write('export const listaLivros = [')
        try:
            for i in range(16):
                urlBook = linkLivros[i]
                nameBook = nomeLivros[i]
                imgBook = imagensLivrs[i]
                objetoLivro = f'{{"imagem": "{imgBook}", "url": "{urlBook}", "nome": "{nameBook}"}}\n'
                arquivo.write(objetoLivro)
                arquivo.write(',')
            arquivo.write('];')
        except Exception as e:
            main()
        finally:
            print("executando de novo")

    
    with open('livros.js', 'r', encoding='utf-8') as arq:
        linhas = arq.readlines()
        if len(linhas) < 2:
            main()

main()
