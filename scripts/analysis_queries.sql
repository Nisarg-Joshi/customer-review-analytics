
-- Query 1: Sentiment Distribution
SELECT "Sentiment", COUNT(*) as total 
FROM reviews 
GROUP BY "Sentiment" 
ORDER BY total DESC;

-- Query 2: Average Score by Sentiment
SELECT "Sentiment", 
       ROUND(AVG("Score"), 2) as avg_score,
       COUNT(*) as total_reviews
FROM reviews 
GROUP BY "Sentiment" 
ORDER BY avg_score DESC;

-- Query 3: Review Trends by Year
SELECT "Year",
       COUNT(*) as total_reviews,
       ROUND(AVG("Score"), 2) as avg_score
FROM reviews
GROUP BY "Year"
ORDER BY "Year" ASC;

-- Query 4: Top 10 Most Reviewed Products
SELECT "ProductId",
       COUNT(*) as total_reviews,
       ROUND(AVG("Score"), 2) as avg_score,
       COUNT(CASE WHEN "Sentiment" = 'Positive' THEN 1 END) as positive_count,
       COUNT(CASE WHEN "Sentiment" = 'Negative' THEN 1 END) as negative_count
FROM reviews
GROUP BY "ProductId"
ORDER BY total_reviews DESC
LIMIT 10;

-- Query 5: Ranking Products using Window Function
SELECT "ProductId",
       COUNT(*) as total_reviews,
       ROUND(AVG("Score"), 2) as avg_score,
       RANK() OVER (ORDER BY COUNT(*) DESC) as popularity_rank
FROM reviews
GROUP BY "ProductId"
ORDER BY popularity_rank ASC
LIMIT 10;

-- Query 6: Monthly Sentiment Trend using CTE
WITH monthly_sentiment AS (
    SELECT "Year",
           "Month",
           "Sentiment",
           COUNT(*) as total
    FROM reviews
    GROUP BY "Year", "Month", "Sentiment"
)
SELECT "Year",
       "Month",
       "Sentiment",
       total,
       ROUND(100.0 * total / SUM(total) OVER (PARTITION BY "Year", "Month"), 2) as percentage
FROM monthly_sentiment
ORDER BY "Year", "Month", "Sentiment";
