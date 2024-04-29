import streamlit as st
import pandas as pd 
import plotly.express as px
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
from query import *

st.set_page_config(page_title="Dashboard", page_icon="🌎", layout="wide")
st.subheader("🔔 Insurance Descriptive Analysis")
st.markdown("##")

# fetch data
result = view_my_data()
df = pd.DataFrame(result, columns=["Policy", "Expiry", "Location", "State", "Region", "Investment", "Construction", "Business Type", "Earthquake", "Flood", "Rating", "id"])

# side bar
st.sidebar.image("logo1.jpg", caption="Online Analytics")

# switcher
st.sidebar.header("Please filter")
region = st.sidebar.multiselect(
    "Select Region", 
    options = df["Region"].unique(),
    default = df["Region"].unique(),
)

location = st.sidebar.multiselect(
    "Select Location", 
    options = df["Location"].unique(),
    default = df["Location"].unique(),
)

location = st.sidebar.multiselect(
    "Select Construction", 
    options = df["Location"].unique(),
    default = df["Location"].unique(),
)