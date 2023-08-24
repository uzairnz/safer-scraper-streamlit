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
