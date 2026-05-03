import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- LOAD DATA ----------------
df = pd.read_csv("traffic.csv")

# Convert date
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df = df.dropna(subset=['date'])

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("🔍 Filters")

# Date filter
date_range = st.sidebar.date_input(
    "Select Date Range",
    [df['date'].min(), df['date'].max()]
)

if len(date_range) == 2:
    start, end = date_range
    df = df[(df['date'] >= pd.to_datetime(start)) & (df['date'] <= pd.to_datetime(end))]

# Country filter
selected_country = st.sidebar.multiselect(
    "Select Country",
    df['country'].dropna().unique()
)

# Artist filter
selected_artist = st.sidebar.multiselect(
    "Select Artist",
    df['artist'].dropna().unique()
)

if selected_country:
    df = df[df['country'].isin(selected_country)]

if selected_artist:
    df = df[df['artist'].isin(selected_artist)]

# ---------------- HANDLE EMPTY DATA ----------------
if df.empty:
    st.warning("No data available for selected filters")
    st.stop()

# ---------------- FEATURE ENGINEERING ----------------
df['event'] = df['event'].astype(str).str.strip().str.lower()

df['is_click'] = (df['event'] == 'click').astype(int)

daily = df.groupby('date').agg({
    'is_click': 'sum',
    'event': 'count'
}).rename(columns={'event': 'total_events'})

daily['CTR'] = (daily['is_click'] / daily['total_events']) * 100

# ---------------- UI ----------------
st.title("📊 Overview")

# CTR Trend
st.subheader("📈 CTR Trend Over Time")
st.line_chart(daily['CTR'])

st.markdown("---")

# ---------------- KPI SECTION ----------------
total_events = len(df)
total_clicks = df['is_click'].sum()
ctr = (total_clicks / total_events) * 100 if total_events > 0 else 0

active_countries = df['country'].nunique()
active_artists = df['artist'].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Events", total_events)
col2.metric("Clicks", total_clicks)
col3.metric("CTR (%)", round(ctr, 2))
col4.metric("Active Artists", active_artists)

st.markdown("---")

# ---------------- ARTIST SEGMENTATION ----------------
st.subheader("🎯 Top vs Low Performing Artists")

artist_perf = df.groupby('artist')['is_click'].mean().dropna().sort_values(ascending=False)

top_artists = artist_perf.head(5)
low_artists = artist_perf.tail(5)

col1, col2 = st.columns(2)

# Top Artists
with col1:
    st.write("🔥 Top Artists")

    top_df = top_artists.reset_index()
    top_df.columns = ['artist', 'CTR']

    fig = px.bar(
        top_df,
        x='CTR',
        y='artist',
        orientation='h',
        title="Top Artists by CTR",
        color='CTR'
    )

    st.plotly_chart(fig, use_container_width=True)

# Low Artists
with col2:
    st.write("⚠️ Low Performing Artists")

    low_df = low_artists.reset_index()
    low_df.columns = ['artist', 'CTR']

    low_df = low_df.fillna(0)
    low_df['CTR'] = low_df['CTR'] * 100
    low_df = low_df.sort_values(by="CTR", ascending=True)

    if low_df['CTR'].sum() == 0:
        st.warning("All low-performing artists have 0 engagement")

        st.write("📊 These artists are not receiving any clicks:")

        st.dataframe(low_df)

        # 🔥 ADD BUSINESS INSIGHT
        st.info("""
        💡 Insight:
        These artists are being viewed but not clicked.
        
        👉 Recommendation:
        - Improve content quality
        - Target the right audience
        - Optimize promotion strategy
        """)
    else:
        fig = px.bar(
            low_df,
            x='CTR',
            y='artist',
            orientation='h',
            title="Low Performing Artists",
            color='CTR'
        )

        fig.update_layout(xaxis_title="CTR (%)")

        st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ---------------- COUNTRY MAP ----------------
st.subheader("🌍 Country Performance (CTR)")

country_ctr = df.groupby('country')['is_click'].mean().dropna().sort_values(ascending=False)

country_data = country_ctr.reset_index()
country_data.columns = ['country', 'CTR']

fig = px.choropleth(
    country_data,
    locations='country',
    locationmode='country names',
    color='CTR',
    title="Country-wise CTR"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ---------------- INSIGHTS ----------------
st.subheader("🧠 Automated Insights")

if ctr > 60:
    st.success("🔥 Excellent engagement — users are highly interactive")
elif ctr > 30:
    st.info("👍 Moderate engagement — scope for improvement")
else:
    st.warning("⚠️ Low engagement — optimization needed")

st.write(f"Current CTR: {round(ctr, 2)}%")

top_country = country_ctr.idxmax()
low_country = country_ctr.idxmin()

top_artist = artist_perf.idxmax()
low_artist = artist_perf.idxmin()

st.success(f"""
📊 Key Insights:

• 🌍 Highest engagement country: {top_country}  
• ⚠️ Lowest engagement country: {low_country}  

• 🎤 Best performing artist: {top_artist}  
• 📉 Weakest artist: {low_artist}  

📈 CTR trend shows how user interaction quality changes over time.

👉 Recommendation:
Focus marketing on high-CTR countries and optimize low-performing artists.
""")

st.markdown("---")

# ---------------- ACTIVITY BY DAY ----------------
st.subheader("📅 Activity by Day")

daily_events = df.groupby(df['date'].dt.date).size()
st.bar_chart(daily_events)

st.markdown("---")

# ---------------- TRAFFIC TREND ----------------
st.subheader("📈 Traffic Trend")

trend = df.groupby('date').size()
st.line_chart(trend)

st.markdown("---")

# ---------------- FUNNEL ----------------
st.subheader("🔻 Conversion Funnel")

funnel_data = pd.DataFrame({
    "Stage": ["Events", "Clicks"],
    "Count": [total_events, total_clicks]
})

st.bar_chart(funnel_data.set_index("Stage"))

st.markdown("---")

# ---------------- DOWNLOAD ----------------
st.subheader("📥 Download Filtered Data")

csv = df.to_csv(index=False).encode('utf-8')

st.download_button(
    "⬇ Download Data",
    data=csv,
    file_name="filtered_data.csv",
    mime="text/csv"
)