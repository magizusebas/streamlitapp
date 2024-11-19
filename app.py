
import streamlit as st
import streamlit as st
from streamlit_option_menu import option_menu
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup


# Define background color CSS
background_color = "#D9BEF0"  # New color code

# CSS to set background for the main content area as well
css = f"""
<style>
    /* Set the background for the entire page */
    .stApp {{
        background-color: {background_color};
    }}
</style>
"""

# Inject CSS into Streamlit app
st.markdown(css, unsafe_allow_html=True)

with open('waves.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

###################################################################################

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

#IMPORT DATA SET


# Convert HTML table to a pandas DataFrame
df = pd.read_csv("exit_velocity.csv")

#CHANGE NAMES OF COLUMNS
df = df.rename(columns={
    'PLAYERPLAYER': 'PLAYER',
    'TEAMTEAM': 'TEAM',
    'GG':'G',
    'ABAB':'AB',
    'RR':'R',
    'HH':'H',
    '2B2B': '2B',
    '3B3B': '3B',
    'HRHR':'HR',
    'RBIRBI':'RBI',
    'BBBB':'BB',
    'SOSO':'SO',
    'SBSB':'SB',
    'CSCS': 'CS',
    'AVGAVG': 'AVG',
    'OBPOBP':'OBP',
    'SLGSLG':'SLG',
        # Add more as needed
})

st.title('Sport stats')
st.write('Look at the pretty waves')
st.markdown('<p class="dashboard_title">A Random App</p>', unsafe_allow_html = True)
st.markdown('<p class="dashboard_subtitle">Look at the pretty waves</p>', unsafe_allow_html = True)



# Horizontal Menu
menu_selected = option_menu(None, ["Home", "PLAYER", "AB", 'AVG'],
    icons=['house', 'cloud-upload', "list-task", 'gear'],
    menu_icon="cast", default_index=0, orientation="horizontal",
        styles={
        "container": {"background-color": "#B7A6F6"},
        "icon": {"color": "#802EF2", "font-size": "20px"},
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#88A3E2"},
        "nav-link-selected": {"background-color": "#7A577A"},
    }
)

if menu_selected=="PLAYER":
    st.write("The PLAYER page")
    # Create a selectbox for filtering
    selected_name = st.selectbox("Select a Team to view details:", df['TEAM'])

    # Filter the DataFrame based on the selected name
    filtered_df = df[df['TEAM'] == selected_name]

    # Display the filtered DataFrame
    st.write("Filtered DataFrame:")
    st.write(filtered_df)

if menu_selected=="AB":
    st.write("The AB page")
    def loadCategory(url):
      df=pd.read_csv(url)
      dfCategories = df.groupby('PLAYER')['AB'].sum().reset_index()
      fig1 = px.bar(dfCategories, x='PLAYER', y='AB', color="PLAYER", title="AB by Player")
      st.plotly_chart(fig1,use_container_width=True)

    loadCategory(url)

if menu_selected=="AVG":
    st.write("The AVG page")
