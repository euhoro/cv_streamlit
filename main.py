import streamlit as st

import streamlit as st
from auth0.authentication import GetToken
from auth0.management import Auth0
import requests

import page1
import page2

AUTH0_DOMAIN = 'your-auth0-domain'
CLIENT_ID = 'your-client-id'
CLIENT_SECRET = 'your-client-secret'
REDIRECT_URI = 'http://localhost:8501'


def login():
    auth_url = f"https://{AUTH0_DOMAIN}/authorize?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"
    st.markdown(f'<a href="{auth_url}" target="_self">Login</a>', unsafe_allow_html=True)


def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Page 1", "Page 2"])

    if page == "Home":
        st.title("Welcome to the Multi-Page App with Auth0")
        login()
    elif page == "Page 1":
        page1.page1()
    elif page == "Page 2":
        if 'user_info' in st.session_state:
            page2.page2()
        else:
            st.warning("Please log in to access this page.")
            login()


if __name__ == "__main__":
    main()
