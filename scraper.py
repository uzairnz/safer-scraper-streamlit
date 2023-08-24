import requests
from bs4 import BeautifulSoup

def scrape_company_data(usdot_code):
    url = f"https://example.com/companies?usdot={usdot_code}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract and parse company details from the soup object
        company_details = {
            "name": soup.find("span", class_="company-name").text,
            "address": soup.find("div", class_="company-address").text,
            # Add more details extraction as needed
        }
        return company_details
    else:
        return None