import requests
from bs4 import BeautifulSoup

# hacer una solicitud HTTP a la página web
url = 'https://saintseiya.fandom.com/es/wiki/Saint_Seiya'
response = requests.get(url)

# crear un objeto BeautifulSoup para analizar el HTML
soup = BeautifulSoup(response.content, 'html.parser')

# encontrar el elemento con el tag "div" y el id "toc"
toc_element = soup.find('div', {'id': 'toc'})

# extraer el contenido del elemento y guardarlo en una variable
toc_content = toc_element.text

# imprimir el contenido extraído
print(toc_content)