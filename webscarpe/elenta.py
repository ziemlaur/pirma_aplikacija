import requests
from bs4 import BeautifulSoup
import mysql.connector

# Function to scrape the data
def scrape_data():
    base_url = "https://elenta.lt/skelbimai/nt/butai"
    ads = []
    page = 1

    while True:
        url = f"{base_url}?page={page}"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        ad_elements = soup.find_all('li', id=lambda x: x and x.startswith('unit-')) 

        if not ad_elements:
            print(f"No ads found on page {page}. Assuming last page reached.")
            break

        for ad in ad_elements:
            try:
                # Extracting required fields
                title = ad.find('h3', class_='ad-hyperlink').text.strip()
                price = ad.find('span', class_='price-box').text.strip()
                address = ad.find('span', class_='location-info-box').text.strip()
                description = ad.find('p').text.strip()
                
                link_tag = ad.find('a')
                image_tag = link_tag.find('img') if link_tag else None
                image_url = image_tag['src'] if image_tag and 'src' in image_tag.attrs else None
                print(image_url)



                ads.append({
                    'title': title,
                    'price': price,
                    'address': address,
                    'description': description,
                    'image_url': image_url
                })
            except AttributeError:
                # Skip ads with missing information
                continue

        print(f"Fetched {len(ad_elements)} ads from page {page}.")
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
        CREATE TABLE IF NOT EXISTS elenta_ads (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
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
                INSERT INTO elenta_ads (title, price, address, description, image_url)
                VALUES (%s, %s, %s, %s, %s)
            ''', (ad['title'], ad['price'], ad['address'], ad['description'], ad['image_url']))
        except Exception as e:
            print(f"Error inserting ad: {e}")

    cnx.commit()
    cur.close()
    cnx.close()

# Main script
if __name__ == "__main__":
    ads = scrape_data()
    if ads:
        # insert_into_database(ads)
        print(f"Inserted {len(ads)} ads into the database.")
    else:
        print("No ads to insert.")
