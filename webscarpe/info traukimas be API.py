import requests
from bs4 import BeautifulSoup

url = 'https://www.1551.lt/automobiliu-atsargines-dalys-reikmenys/'

# uzklausa
data = requests.get(url)

print(data.status_code)
# tekstas 
data = data.text

# konvertavimas
html = BeautifulSoup(data, 'html.parser')
# select first one
# print(html.select_one('.uk-panel-title a span'))

# # select all
# for title in html.select('.uk-panel-title a span'):
#     print(title.text)

# blokas
for box in html.select('.tm-result'):
    print(box.select_one('.uk-margin').text)


# duomenu bazes lentele:
# id
# title
# descr (text)
# address
# phone
