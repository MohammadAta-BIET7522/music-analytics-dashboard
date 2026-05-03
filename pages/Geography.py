import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("traffic.csv")
df['date'] = pd.to_datetime(df['date'], errors='coerce')

df['is_click'] = df['event'].apply(lambda x: 1 if x == 'click' else 0)

daily = df.groupby('date').agg({
    'is_click': 'sum',
    'event': 'count'
}).rename(columns={'event': 'total_events'})

daily['CTR'] = (daily['is_click'] / daily['total_events']) * 100

# ---------------- NOW USE IT ----------------
st.title("📊 Overview")

st.line_chart(daily['CTR'])

st.title("🌍 Geography")

country_data = df['country'].value_counts().reset_index()
country_data.columns = ['country', 'count']

fig = px.choropleth(
    country_data,
    locations='country',
    locationmode='country names',
    color='count'
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Top Cities")
st.bar_chart(df['city'].value_counts().head(10))

st.markdown("---")
st.subheader("📥 Download Filtered Data")

csv = df.to_csv(index=False).encode('utf-8')

st.download_button(
    "⬇ Download Data",
    data=csv,
    file_name="filtered_data.csv",
    mime="text/csv"
)