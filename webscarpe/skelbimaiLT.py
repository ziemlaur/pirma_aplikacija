import requests
from bs4 import BeautifulSoup
import mysql.connector

def scrape_data():
    base_url = "https://www.skelbimai.lt/skelbimai/nekilnojamasis-turtas/butai"
    ads = []
    page = 1

    while True:
        url = f"{base_url}?page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        ad_elements = soup.select('div#classifieds-list a')  

        if not ad_elements:
            print(f"No ads found on page {page}. Assuming last page reached.")
            break

        for ad in ad_elements:
            try:
                ad_link = ad['href']
                ad_url = f"https://www.skelbimai.lt{ad_link}"

                ad_response = requests.get(ad_url)
                ad_soup = BeautifulSoup(ad_response.text, 'html.parser')



                gyvenviete_tag = ad_soup.select_one('div.row:-soup-contains("Gyvenvietė")')

                if gyvenviete_tag:
                    city_tag = gyvenviete_tag.select_one('div + div')  
                    city_name = city_tag.text.strip() if city_tag else "No City"
                else:
                    city_name = "No City"

                print(f"Miestas: {city_name}")




                statybos_metai_tag = ad_soup.select_one('div.row:-soup-contains("Statybos metai")')

                if statybos_metai_tag:
                    metai_tag = statybos_metai_tag.select_one('div + div')  
                    metai = metai_tag.text.strip() if metai_tag else "no year"
                else:
                    metai = "no year"

                print(f"Statybos metai: {metai}")



                aukstas_tag = ad_soup.select_one('div.row:-soup-contains("Aukštas")')

                if aukstas_tag:
                    skaicius_tag = aukstas_tag.select_one('div + div')  
                    aukstas = skaicius_tag.text.strip()
                else:
                    aukstas = "No floor"
                print(f"Aukstas: {aukstas}")




                price_tag = ad_soup.select_one('div.price')
                if price_tag: 
                    price =price_tag.get('content')
                print(f'Kaina = {price} EUR')


                phone_tag = ad_soup.select_one('div.row:-soup-contains("Telefonas")')

                if phone_tag:
                    number_tag = phone_tag.select_one('div + div')  
                    phone = number_tag.text.strip()
                else:
                    phone = "No phone number"
                print(f"Telefono numeris: {phone}")


                description_tag = ad_soup.select_one('section.info-bl div[itemprop="description"]')
                if description_tag:
                    description = description_tag.text.strip()
                else:
                    description = "no description"
                print(f'aprasymas = {description}')


                ads.append({
                    'Miestas': city_name,
                    'Statybos_metai': metai,
                    'Aukstas': aukstas,
                    'Kaina': price,
                    'Telefono_numeris': phone,
                    'aprasymas': description
                })

            except AttributeError as e:
                print(f"Error scraping ad: {e}")
                continue

        print(f"Fetched {len(ad_elements)} ads from page {page}.")
        
        next_button = soup.select_one('a.pagination__next')  
        if not next_button:
            print(f"No next page found. Stopping at page {page}.")
            break
        
        page += 1

    return ads


def insert_into_database(ads):
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="", 
        database='extract')

    print('connected')
    cur = cnx.cursor()

    cur.execute(''' 
        CREATE TABLE IF NOT EXISTS skelbimaiLT_ads (
            id INT AUTO_INCREMENT PRIMARY KEY,
            miestas VARCHAR(30),
            statybos_metai VARCHAR(5),
            aukstas VARCHAR(5),
            kaina TEXT,
            telefono_numeris TEXT,
            aprasymas VARCHAR(255)
        )
    ''')

    # Inserting data
    for ad in ads:
        try:
            cur.execute('''
                INSERT INTO skelbimai_ads (miestas, statybos metai, aukstas, kaina, telefono_numeris, aprasymas)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (ad['city_name'], ad['metai'], ad['aukstas'], ad['price'], ad['phone'], ad['description']))
        except Exception as e:
            print(f"Error inserting ad: {e}")

    cnx.commit()
    cur.close()
    cnx.close()


if __name__ == "__main__":
    ads = scrape_data()
    if ads:
        insert_into_database(ads)
        print(f"Inserted {len(ads)} ads into the database.")
    else:
        print("No ads to insert.")
