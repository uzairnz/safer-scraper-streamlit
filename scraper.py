import requests
import json
from bs4 import BeautifulSoup
from safer import CompanySnapshot

def scrape_company_data(usdot_code):
    client = CompanySnapshot()
    company = client.get_by_usdot_number(usdot_code)
    company_dict = json.loads(company)

    return company_dict
