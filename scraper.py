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
