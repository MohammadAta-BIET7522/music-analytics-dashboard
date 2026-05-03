import streamlit as st

st.set_page_config(page_title="Music Analytics", layout="wide")

# ---------------- HEADER ----------------
st.title("🎧 Music Analytics Platform")


st.info("Use the sidebar to navigate between sections.")

# ---------------- QUICK SUMMARY ----------------
st.subheader("📊 What this dashboard does")

st.markdown("""
This platform helps analyze **music traffic data** and provides insights into:

- 🎯 User engagement (CTR)
- 🌍 Geographic performance
- 🎤 Artist & track performance
- 📈 Traffic trends over time
""")

# ---------------- NAVIGATION GUIDE ----------------
st.subheader("🧭 Sections")

col1, col2, col3, col4 = st.columns(4)

col1.info("📊 Overview\n\nKPIs, CTR, Trends")
col2.info("🌍 Geography\n\nCountry-level insights")
col3.info("🎤 Content\n\nTop artists & tracks")
col4.info("🧠 Insights\n\nBusiness recommendations")

# ---------------- FOOTER ----------------
st.markdown("---")
