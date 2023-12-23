import streamlit as st
from streamlit_gsheets import GSheetsConnection
from google.oauth2 import service_account
import gspread
import pandas as pd

# @st.cache_data
# def load_data(sheets_url):
#     csv_url = sheets_url.replace('edit?usp=sharing', 'export?format=csv&gid=0')
#     return pd.read_csv(csv_url)

def teste():   

    # Create a connection object.
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=[
            "https://www.googleapis.com/auth/spreadsheets",
        ],
    )
    gc = gspread.authorize(credentials)
    
    # Get the Google Sheet by URL.
    sheet_url = pd.read_csv(st.secrets["private_gsheets_url"])
    # sheet = gc.open_by_url(sheet_url)
    df = pd.DataFrame(sheet_url)
    st.write(sheet)
