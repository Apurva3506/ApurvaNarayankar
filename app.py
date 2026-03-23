import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 1. Page Configuration
st.set_page_config(layout="wide", page_title="Coupon Usage & NPS Dashboard")

# 2. Header & Metrics (Replicating the top bar)
st.title("Coupon Usage Impact on Customer Experience")
col1, col2 = st.columns(2)
with col1:
    st.info("**Used Coupon at Checkout: 50.5%**  \nNPS: 19.8")
with col2:
    st.error("**Not Able to Use Coupon: 49.5%**  \nNPS: -18.6")

# 3. Main Dashboard Grid
top_row = st.columns((1, 1, 2)) # Adjusting widths for NPS charts and Map

with top_row[0]:
    st.subheader("Overall NPS YTD")
    # Using a Donut Chart for the 0.79 NPS figure
    fig_donut = px.pie(values=[40.3, 20.2, 39.5], names=['Detractor', 'Passive', 'Promoter'], hole=0.5)
    st.plotly_chart(fig_donut, use_container_width=True)

with top_row[1]:
    st.subheader("% Distribution")
    # Create sample data for stacked bar chart
    df_dist = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov'],
        'Promoter': [35, 37, 39, 38, 40, 41, 40, 39, 42, 41, 40],
        'Passive': [25, 24, 23, 25, 22, 21, 22, 23, 20, 21, 22],
        'Detractor': [40, 39, 38, 37, 38, 38, 38, 38, 38, 38, 38]
    })
    fig_dist = px.bar(df_dist, x='Month', y=['Promoter', 'Passive', 'Detractor'], 
                       title="Promoter/Passive/Detractor Distribution")
    st.plotly_chart(fig_dist, use_container_width=True)

with top_row[2]:
    st.subheader("NPS Distribution per State")
    # US Map visualization using Choropleth
    # You'll need to replace this with actual state data
    st.info("📍 US Map visualization - Add state-level NPS data")

# 4. Bottom Row (Trend and Word Cloud)
bottom_row = st.columns(2)

with bottom_row[0]:
    st.subheader("NPS Trend")
    # Line chart for monthly trends
    df_trend = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov'],
        'NPS': [-5, -2, 1, 0, 2, 3, 1, 0, 4, 3, 2]
    })
    fig_trend = px.line(df_trend, x='Month', y='NPS', markers=True, title="NPS Monthly Trend")
    st.plotly_chart(fig_trend, use_container_width=True)

with bottom_row[1]:
    st.subheader("Customer Sentiment (Word Cloud)")
    # Generate word cloud from feedback text
    text = "Product Out of Stock Checkout Slow Long Wait Unattended Service Quality Support"
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)