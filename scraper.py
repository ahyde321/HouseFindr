from bs4 import BeautifulSoup
import requests
import random
from fake_useragent import UserAgent

baseurl = "https://www.propertypal.com/property-to-rent/"
location = "belfast-city-centre"
url = baseurl+location

# Create an instance of the UserAgent class
# Examples : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
user_agent = UserAgent()

# Generate a random User-Agent
random_user_agent = user_agent.random

headers = {
    "User-Agent": random_user_agent
}

response = requests.get(url, headers=headers)
html_data = response.text
soup = BeautifulSoup(html_data, "html.parser")

house_divs = soup.find_all("div", class_="sc-dc2f0980-9 idpOBz")
for house_div in house_divs:
    name = house_div.find("h2", class_="sc-ccfad107-1 dplKSC").text.strip()
    price = house_div.find("strong", class_="sc-ccfad107-11 YnKCM pp-property-price-bold").text.strip()
    print("Name:", name)
    print("Price:", price)
    print()

