import requests
from bs4 import BeautifulSoup
import mysql.connector

def scrape_data():
    base_url = "https://sutarta.lt/skelbimai/garso-vaizdo-foto-technika/vaizdo-video-technika"
    ads = []
    page = 1

    while True:
        url = f"{base_url}?page_nr={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        ad_elements = soup.select('li[id^="ann_"]') 
        
        if not ad_elements:
            print(f"No ads found on page {page}. Assuming last page reached.")
            break 

        for ad in ad_elements:
            try:

                time = ad.select_one('div.list-date')  
                time = time.text.strip() if time else "No time"
                print(f"Time: {time}")

                pricebox = ad.select_one('div.desc > div.section')  
                price = pricebox.text.strip() if pricebox else "No price"


                addressbox = ad.select_one('div.cat-geo.clean-links > div.section:not(.section-category) > a')  
                address = addressbox.text.strip() if addressbox else "No address"
                print(f"Address: {address}")

                description = ad.select_one('div.desc-title')  
                description = description.text.strip() if description else "No description"
                print(f"Description: {description}")
                
                image_tag = ad.select_one('a img')  
                image_url = image_tag['src'] if image_tag and 'src' in image_tag.attrs else None
                print(f"Image URL: {image_url}")

                ads.append({
                    'time': time,
                    'price': price,
                    'address': address,
                    'description': description,
                    'image_url': image_url
                })

            except AttributeError:
                continue

        print(f"Fetched {len(ad_elements)} ads from page {page}.")
        
        next_button = soup.select_one('a.next')  
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
        database ='extract')

    print('connected')
    cur = cnx.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS sutarta_ads (
            id INT AUTO_INCREMENT PRIMARY KEY,
            time VARCHAR(30),
            price VARCHAR(255),
            address VARCHAR(255),
            description TEXT,
            image_url TEXT
        )
    ''')

    # Inserting data
    for ad in ads:
        try:
            cur.execute('''
                INSERT INTO sutarta_ads (time, price, address, description, image_url)
                VALUES (%s, %s, %s, %s, %s)
            ''', (ad['time'], ad['price'], ad['address'], ad['description'], ad['image_url']))
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
