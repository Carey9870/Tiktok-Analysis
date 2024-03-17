# NOTE: To run app: streamlit run app.py

import streamlit as st
import pandas as pd
import plotly.express as px

# Set page width to wide
st.set_page_config(layout='wide')

st.error("This dashboard allows you to analyse trending 📈 tiktoks using Python  and Streamlit .")

# Create sidebar
st.sidebar.markdown("<div><img src='https://png2png.com/wp-content/uploads/2021/08/Tiktok-logo-png.png' width=100 /><h1 style='display:inline-block'><u>Tiktok Analytics</u></h1></div>", unsafe_allow_html=True)
# st.sidebar.markdown("This dashboard allows you to analyse trending 📈 tiktoks using Python and Streamlit.")
st.sidebar.markdown("To get started: <ol><li>Enter the <i><u>hashtag</u></i> you wish to analyse</li> <li>Hit <i><u>Get Data</u></i>.</li> <li>Get <u>analyzing</u></li></ol>",unsafe_allow_html=True)

hashtag = st.text_input('Search for a hashtag here', value='')

# Button
if st.button('Get Data'):
    # Load in existing data to test it out
    tiktok = pd.read_csv('tiktokdata.csv')

    # Plotly viz here
    fig = px.histogram(tiktok, x='desc', hover_data=['desc'], y='stats_diggCount', height=300) 
    st.plotly_chart(fig, use_container_width=True)

    # Split columns
    left_col, right_col = st.columns(2)

    # First Chart - video stats
    scatter1 = px.scatter(tiktok, x='stats_shareCount', y='stats_commentCount', hover_data=['desc'], size='stats_playCount', color='stats_playCount')
    left_col.plotly_chart(scatter1, use_container_width=True)

    # Second Chart
    scatter2 = px.scatter(tiktok, x='authorStats_videoCount', y='authorStats_heartCount', hover_data=['author_nickname'], size='authorStats_followerCount', color='authorStats_followerCount')
    right_col.plotly_chart(scatter2, use_container_width=True)


    # Show tabular dataframe in streamlit
    tiktok