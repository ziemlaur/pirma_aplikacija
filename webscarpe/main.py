import requests
from bs4 import BeautifulSoup
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
import sys
import csv

def scrape_data(url):
    ads = []
    page = 1
    total_value = 0.0

    while True:
        response = requests.get(f"{url}?page={page}")
        soup = BeautifulSoup(response.text, 'html.parser')
        ad_elements = soup.find_all('li', id=lambda x: x and x.startswith('unit-'))

        if not ad_elements:
            print(f"No ads found on page {page}.")
            break

        for ad in ad_elements:
            try:
                title = ad.find('h3', class_='ad-hyperlink').text.strip()
                price = ad.find('span', class_='price-box').text.strip()
                price = float(price.replace("€", "").replace(",", "").replace(" ", "").strip())  

                ads.append({
                    'title': title,
                    'price': price
                })

                total_value += price  
            except AttributeError:
                continue

        print(f"{len(ad_elements)} ads in page {page}.")
        page += 1

    return ads, total_value

def save_to_csv(ads):
    filename = "skelbimu_suvestine.csv"
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'price'])
        writer.writeheader()
        writer.writerows(ads)
    print(f"Data saved to {filename}")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Skelbimų Surinkimas")
        self.setGeometry(100, 100, 400, 200)
        self.window()

    def window(self):
        layout = QVBoxLayout()

        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Įveskite tinklapio adresą")
        layout.addWidget(self.url_input)

        self.scrape_button = QPushButton("Surinkti skelbimus", self)
        self.scrape_button.clicked.connect(self.scrape)
        layout.addWidget(self.scrape_button)

        self.setLayout(layout)

    def scrape(self):
        url = self.url_input.text().strip()

        if not url.startswith("https://") or "elenta.lt" not in url:
            self.show_message("Netinkamas tinklapio adresas. Prašome įvesti tinkamą URL.", "Klaida", QMessageBox.Icon.Critical)
            return

        ads, total_value = scrape_data(url)

        if ads:
            save_to_csv(ads)
            self.show_message(f"Surinkta {len(ads)} skelbimų. Bendra vertė: {total_value:.2f}€, informacija patalpinta skelbimu_suvestine.csv faile", 'OK', QMessageBox.Icon.Information)
        else:
            self.show_message("Nepavyko surinkti skelbimų. Patikrinkite tinklapį arba tinklapio struktūrą.", "Klaida", QMessageBox.Icon.Critical)

        self.url_input.clear()

    def show_message(self, message, title, icon):
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

