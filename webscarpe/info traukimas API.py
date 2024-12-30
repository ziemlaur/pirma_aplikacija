search = input('please input your request: ')
url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={search}'

import requests

response = requests.get(url)
# print(response.json())

data = response.json()
file = open('tekstas.txt', 'w')
for drink in data['drinks']: 
    drink_type = drink['strAlcoholic']
    drink_name = drink['strDrink']
    file.write(f'{drink_type} {drink_name}\n')

file.close()






