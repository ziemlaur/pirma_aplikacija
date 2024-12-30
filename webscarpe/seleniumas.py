from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

opcijos = Options()
opcijos.add_argument('--incognito')
opcijos.headless = True  

driver = webdriver.Chrome(options=opcijos)

base_url = "https://www.baldoras.lt/katalogas/valgomojo-stalai/"
driver.get(base_url)

prices = []

    
page = 1
while True:
    print(f"Scraping page {page}...")
    
    source = driver.page_source
    soup = BeautifulSoup(source, "html.parser")
    
    price_elements = soup.find_all("div", class_="product-card__actions")
    
    for price_element in price_elements:
        price = price_element.find("div", class_="product-card__prices")
        if price:
            try:
                price_value = price.get_text(strip=True).replace("€", "").replace(",", ".")
                price_value = float(price_value)
                prices.append(price_value)
                print(price_value)
            except ValueError:
                pass  
    
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, "li.page-item a[aria-label='Next']")  
        next_button.click()
        WebDriverWait(driver, 10).until(EC.staleness_of(next_button))  
        sleep(2) 
        page += 1  
    except Exception as e:
        print(f"No next page found or error")
        break  


if prices:
    average_price = sum(prices) / len(prices)
    print(f"Average price: €{average_price:.2f}")
else:
    print("No prices found.")


