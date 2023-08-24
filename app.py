import streamlit as st
from scraper import scrape_company_data
import json

def main():
    st.title("Company Data Scraper")
    usdot_code = st.text_input("Enter US DOT Code")
    usdot_code_int = int(usdot_code)
    if st.button("Fetch Company Details"):
        if usdot_code:
            company_details = scrape_company_data(usdot_code_int)
            if company_details:
                st.write("Company Details:")
                st.write(f"Name: {company_details['legal_name']}")
                st.write(f"Physical Address: {company_details['physical_address']}")
                st.write(f"Mailing Address: {company_details['mailing_address']}")
                st.write(f"Phone: {company_details['phone']}")
                st.write(f"Operational Status: {company_details['operating_status']}")
                st.write("United States Inspections:")
                us_inspections = company_details['us_inspections']
                for inspection_type, inspection_data in us_inspections.items():
                    st.write(f"- {inspection_type.capitalize()}:")
                    st.write(f"  Out of Service: {inspection_data['out_of_service']}")
                    st.write(f"  Inspections: {inspection_data['inspections']}")
                    st.write(f"  Out of Service Percent: {inspection_data['out_of_service_percent']}")
                    st.write(f"  National Average: {inspection_data['national_average']}")
                st.write("United States Crashes:")
                us_crashes = company_details['united_states_crashes']
                st.write(f"- Injury: {us_crashes['injury']}")
                st.write(f"- Total: {us_crashes['total']}")
                st.write(f"- Fatal: {us_crashes['fatal']}")
                st.write(f"- Tow: {us_crashes['tow']}")
                st.write(f"URL: {company_details['url']}")
                st.write(f"Latest Update: {company_details['latest_update']}")
                # Display more details
            else:
                st.write("Company not found or an error occurred.")

if __name__ == "__main__":
    main()


# Input range for MC/MX Number and also handling for null data. Skip null in this
# Fetch in batches of 10k


# Entity Type:	CARRIER  
# Operating Status:	AUTHORIZED FOR Property	Out of Service Date:	None
# Legal Name:	IRELAND SOLUTION INC 
# DBA Name:	JT GLOBAL LOAD TRUCKING 
# Physical Address:	8383 WILSHIRE BLVD SUITE 800
# BEVERLY HILLS , CA   90211  
# Phone:	(213) 278-7120  
# Mailing Address:	8383 WILSHIRE BLVD SUITE 800
# BEVERLY HILLS , CA   90211  
# USDOT Number:	3423627 	State Carrier ID Number:	 
# MC/MX/FF Number(s):	MC-1107367
#  	DUNS Number:	-- 
# Power Units:	1 	Drivers:	1 
# MCS-150 Form Date:	07/27/2022 	MCS-150 Mileage (Year):	600 (2021) 

# Other information for this carrier
# SMS Results (Carrier Registration) -----> Carrier registration details ------> Email
