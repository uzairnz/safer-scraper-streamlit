import streamlit as st
from scraper import scrape_company_data

def main():
    st.title("Company Data Scraper")
    usdot_code = st.text_input("Enter US DOT Code")

    if st.button("Fetch Company Details"):
        if usdot_code:
            company_details = scrape_company_data(usdot_code)
            if company_details:
                st.write("Company Details:")
                st.write(f"Name: {company_details['name']}")
                st.write(f"Address: {company_details['address']}")
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
