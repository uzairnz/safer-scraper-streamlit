import streamlit as st
import pandas as pd
from scraper import scrape_company_data, scrape_email_from_url

def main():
    st.title("Company Data Scraper")
    usdot_code_start = st.number_input("Enter Starting US DOT Code", value=0, step=1, format="%d")
    batch_size = 10000
    
    if st.button("Fetch and Export Data"):
        data = []
        for i in range(usdot_code_start, usdot_code_start + batch_size):
            company_details = scrape_company_data(i)  # Pass integer i instead of str(i)
            email = scrape_email_from_url(i)  # Pass integer i instead of str(i)
            
            if company_details:
                company_details['email'] = email
                data.append(company_details)

        if data:
            df = pd.DataFrame(data)
            st.write("Data successfully fetched and exported to Excel:")
            st.dataframe(df)
            
            # Export to Excel
            excel_filename = "company_data.xlsx"
            df.to_excel(excel_filename, index=False)
            st.write(f"Data exported to {excel_filename}")
        else:
            st.write("No data fetched or an error occurred.")

if __name__ == "__main__":
    main()



# import streamlit as st
# from scraper import scrape_company_data, scrape_email_from_url
# import json

# def main():
#     st.title("Company Data Scraper")
#     usdot_code = st.number_input("Enter US DOT Code", value=0, step=1)
#     if st.button("Fetch Company Details"):
#         if usdot_code:
#             company_details = scrape_company_data(usdot_code)
#             email = scrape_email_from_url(usdot_code)
#             if company_details:
#                 st.write("Company Details:")
#                 st.write(f"Name: {company_details['legal_name']}")
#                 st.write(f"Email: {email}")
#                 st.write(f"Physical Address: {company_details['physical_address']}")
#                 st.write(f"Mailing Address: {company_details['mailing_address']}")
#                 st.write(f"Phone: {company_details['phone']}")
#                 st.write(f"Operational Status: {company_details['operating_status']}")
#                 st.write("United States Inspections:")
#                 us_inspections = company_details['us_inspections']
#                 for inspection_type, inspection_data in us_inspections.items():
#                     st.write(f"- {inspection_type.capitalize()}:")
#                     st.write(f"  Out of Service: {inspection_data['out_of_service']}")
#                     st.write(f"  Inspections: {inspection_data['inspections']}")
#                     st.write(f"  Out of Service Percent: {inspection_data['out_of_service_percent']}")
#                     st.write(f"  National Average: {inspection_data['national_average']}")
#                 st.write("United States Crashes:")
#                 us_crashes = company_details['united_states_crashes']
#                 st.write(f"- Injury: {us_crashes['injury']}")
#                 st.write(f"- Total: {us_crashes['total']}")
#                 st.write(f"- Fatal: {us_crashes['fatal']}")
#                 st.write(f"- Tow: {us_crashes['tow']}")
#                 st.write(f"URL: {company_details['url']}")
#                 st.write(f"Latest Update: {company_details['latest_update']}")
#                 # Display more details
#             else:
#                 st.write("Company not found or an error occurred.")

# if __name__ == "__main__":
#     main()


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
