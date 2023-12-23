import streamlit as st
from streamlit_gsheets import GSheetsConnection
from google.oauth2 import service_account
import gspread
import pandas as pd

@st.cache_data
def load_data(sheets_url):
    csv_url = sheets_url.replace('edit?usp=sharing', 'export?format=csv&gid=0')
    return pd.read_csv(csv_url)

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
    df = load_data(st.secrets["private_gsheets_url"])
    df = pd.DataFrame(df)
    # sheet_url = st.secrets["private_gsheets_url"]
    # csv = pd.read_csv(sheet_url)
    # sheet = gc.open_by_url(sheet_url)
    # df = pd.DataFrame(csv)
    st.write(df)
