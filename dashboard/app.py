import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

# Page config
st.set_page_config(page_title="Customer Review Analytics", layout="wide")

# Title
st.title("🛍️ AI-Powered Customer Review Analytics")
st.markdown("Analyzing Amazon Fine Food Reviews using SQL + VADER Sentiment Analysis")

# Database connection
@st.cache_resource
def get_engine():
    return create_engine('postgresql+psycopg2://postgres:Nisarg282000*@localhost:5432/customer_reviews')

engine = get_engine()

# ---- Section 1: Sentiment Distribution ----
st.header("📊 Sentiment Distribution")
df_sentiment = pd.read_sql(text('SELECT "Sentiment", COUNT(*) as total FROM reviews GROUP BY "Sentiment" ORDER BY total DESC'), engine)
st.bar_chart(df_sentiment.set_index("Sentiment"))

# ---- Section 2: Average Score by Sentiment ----
st.header("⭐ Average Score by Sentiment")
df_avg = pd.read_sql(text('SELECT "Sentiment", ROUND(AVG("Score"), 2) as avg_score FROM reviews GROUP BY "Sentiment" ORDER BY avg_score DESC'), engine)
st.dataframe(df_avg)

# ---- Section 3: Reviews Per Year ----
st.header("📅 Reviews Per Year")
df_yearly = pd.read_sql(text('SELECT "Year", COUNT(*) as total_reviews FROM reviews GROUP BY "Year" ORDER BY "Year" ASC'), engine)
st.line_chart(df_yearly.set_index("Year"))

# ---- Section 4: Top 10 Products ----
st.header("🏆 Top 10 Most Reviewed Products")
df_products = pd.read_sql(text('SELECT "ProductId", COUNT(*) as total_reviews, ROUND(AVG("Score"), 2) as avg_score FROM reviews GROUP BY "ProductId" ORDER BY total_reviews DESC LIMIT 10'), engine)
st.dataframe(df_products)

