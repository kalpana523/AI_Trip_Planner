import streamlit as st
import datetime
import requests
import sys
BASE_URL="http://localhost:8000" #Backend endpoint

st.set_page_config()

st.title()
# Initiate chat history
if "messages" not in st.session_state:
    st.session_state.messages=[]


st.header()

with st.form():
    user_input=""
    submit_buttom=""
    
if submit_buttom and user_input.strip():
    pass