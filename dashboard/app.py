import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Customer Review Analytics", layout="wide")

# Title
st.title("🛍️ AI-Powered Customer Review Analytics")
st.markdown("Analyzing Amazon Fine Food Reviews using SQL + VADER Sentiment Analysis")

# Load data from CSV
@st.cache_data
def load_data():
    return pd.read_csv("data/reviews_with_sentiment.csv")

df = load_data()

# ---- Section 1: Sentiment Distribution ----
st.header("📊 Sentiment Distribution")
sentiment_counts = df["Sentiment"].value_counts().reset_index()
sentiment_counts.columns = ["Sentiment", "total"]
st.bar_chart(sentiment_counts.set_index("Sentiment"))

# ---- Section 2: Average Score by Sentiment ----
st.header("⭐ Average Score by Sentiment")
avg_score = df.groupby("Sentiment")["Score"].mean().round(2).reset_index()
avg_score.columns = ["Sentiment", "avg_score"]
st.dataframe(avg_score)

# ---- Section 3: Reviews Per Year ----
st.header("📅 Reviews Per Year")
yearly = df.groupby("Year")["Id"].count().reset_index()
yearly.columns = ["Year", "total_reviews"]
st.line_chart(yearly.set_index("Year"))

# ---- Section 4: Top 10 Products ----
st.header("🏆 Top 10 Most Reviewed Products")
top_products = df.groupby("ProductId").agg(
    total_reviews=("Id", "count"),
    avg_score=("Score", "mean")
).round(2).sort_values("total_reviews", ascending=False).head(10).reset_index()
st.dataframe(top_products)