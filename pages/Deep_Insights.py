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
st.title("🧠 Deep Insights")

top_country = df['country'].value_counts().idxmax()
top_artist = df['artist'].value_counts().idxmax()

clicks = len(df[df['event'] == 'click'])
events = len(df)

ctr = (clicks / events) * 100

st.success(f"""
📊 Key Business Insights:

• 🌍 Highest traffic comes from: {top_country}  
• 🎤 Most engaging artist: {top_artist}  
• 📈 Click-through rate: {round(ctr,2)}%  

👉 Recommendation:
Focus marketing campaigns on top-performing regions and artists.
""")

st.markdown("---")