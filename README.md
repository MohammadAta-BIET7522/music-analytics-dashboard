# 🎧 Music Analytics Dashboard

## 🚀 Overview
This project is an interactive **multi-page analytics dashboard** built using Streamlit to analyze music traffic data.  
It provides insights into user engagement, artist performance, and geographic trends.

---

## 🎯 Business Problem
Understanding user engagement across music links to identify:
- High-performing artists
- Low-performing content
- Geographic engagement trends

---

## 💡 Features

### 📊 Overview
- KPI metrics (Total Events, Clicks, CTR)
- CTR trend over time
- Conversion funnel analysis

### 🎯 Artist Analysis
- Top performing artists
- Low performing artists
- Engagement-based segmentation

### 🌍 Geographic Insights
- Country-level CTR visualization (interactive map)

### 🧠 Smart Insights
- Automated engagement analysis (High / Medium / Low)
- Business recommendations

### 📅 Time Analysis
- Activity by day
- Traffic trends

### 🔍 Filters
- Date range filter
- Country filter
- Artist filter

### 📥 Export
- Download filtered dataset as CSV

---

## 🛠 Tech Stack

- Python
- Pandas
- Streamlit
- Plotly

---

## 📂 Project Structure
music-analytics/
│
├── app.py
├── traffic.csv
├── requirements.txt
├── README.md
└── pages/
├── Overview.py
├── Geography.py
├── Content.py
└── Deep_Insights.py


---

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py

🌐 Live Demo



🧠 Key Insights
Some artists show zero engagement (CTR = 0%), indicating poor user interaction
Engagement varies significantly across countries
CTR is a better metric than raw clicks for measuring performance
💼 Resume Description

Built a multi-page interactive analytics dashboard using Streamlit to analyze user engagement data, implementing CTR metrics, segmentation, and automated insights for business decision-making.

🚀 Future Improvements
Add machine learning model (click prediction)
Improve recommendation system
Add user segmentation
Enhance UI/UX design

👨‍💻 Author

Mohammad Ata
