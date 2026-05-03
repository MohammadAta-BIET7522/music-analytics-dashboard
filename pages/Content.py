import streamlit as st
import pandas as pd

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

st.title("🎤 Content Performance")

st.subheader("Top Artists")
st.bar_chart(df['artist'].value_counts().head(10))

st.subheader("Top Tracks")
st.bar_chart(df['track'].value_counts().head(10))

st.subheader("Top Albums")
st.bar_chart(df['album'].value_counts().head(10))

st.markdown("---")
st.subheader("📥 Download Filtered Data")

csv = df.to_csv(index=False).encode('utf-8')

st.download_button(
    "⬇ Download Data",
    data=csv,
    file_name="filtered_data.csv",
    mime="text/csv"
)