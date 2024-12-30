import requests
from bs4 import BeautifulSoup
import mysql.connector

# Connect to the MySQL database
cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="", 
    database ='extract')

print('connected')
cur = cnx.cursor()


# URL of the target page
url = "https://www.1551.lt/automobiliu-atsargines-dalys-reikmenys/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract data using CSS selectors
titles = [title.get_text(strip=True) for title in soup.select('.uk-panel-title a')]
phone_numbers = [phone.get_text(strip=True) for phone in soup.select('.uk-width-medium-3-10 a span')]
addresses = [address.get_text(strip=True) for address in soup.select('.uk-width-medium-7-10 span')]

descriptions = []
for box in soup.select('.tm-result'):
    description = box.select_one('.uk-margin')
    if description:
        descriptions.append(description.text.strip())
    else:
        descriptions.append("no description")

# Insert data into the database
for i in range(len(titles)):
    title = titles[i]
    phone = phone_numbers[i] if i < len(phone_numbers) else None
    address = addresses[i] if i < len(addresses) else None
    description = descriptions[i] if i < len(descriptions) else None

    cur.execute("""
    INSERT INTO automobiliu_dalys (title, description, address, phone_number )
    VALUES (%s, %s, %s, %s)
    """, (title, description, address, phone))

# Commit the changes and close the connection
cnx.commit()
cur.close()
cnx.close()

print("Data has been successfully inserted into the database.")
