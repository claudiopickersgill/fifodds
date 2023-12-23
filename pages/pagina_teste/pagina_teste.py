import streamlit as st
from streamlit_gsheets import GSheetsConnection
from google.oauth2 import service_account
import gspread
import pandas as pd

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
    sheet_url = load_data(st.secrets["private_gsheets_url"])
    # sheet = gc.open_by_url(sheet_url)
    df = pd.DataFrame(sheet_url)
    st.write(sheet)
