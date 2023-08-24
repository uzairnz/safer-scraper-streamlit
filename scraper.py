import requests
import json
from bs4 import BeautifulSoup
from safer import CompanySnapshot


def scrape_company_data(usdot_code):
    client = CompanySnapshot()
    company = client.get_by_usdot_number(usdot_code)
    json_string = company.to_json()
    company_dict = json.loads(json_string)

    return company_dict


def scrape_email_from_url(usdot_code):
    url = f"https://ai.fmcsa.dot.gov/SMS/Carrier/{usdot_code}/CarrierRegistration.aspx"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        label_tag = soup.find('label', text='Email:')
        if label_tag:
            email_tag = label_tag.find_next('span', {'class': 'dat'})
            if email_tag:
                return email_tag.text.strip()
            else:
                return "Email not found on the page"
        else:
            return "Label 'Email:' not found on the page"
    else:
        return "Unable to fetch the webpage"