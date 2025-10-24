-- Top queries (SQLite compatible)

SELECT COUNT(*) AS total_restaurants FROM restaurants;

SELECT ROUND(AVG(aggregate_rating),2) AS avg_rating FROM restaurants;

SELECT city, COUNT(*) AS total_restaurants FROM restaurants GROUP BY city ORDER BY total_restaurants DESC LIMIT 5;

SELECT cuisine, ROUND(AVG(aggregate_rating),2) AS avg_rating FROM restaurants GROUP BY cuisine ORDER BY avg_rating DESC LIMIT 5;

SELECT city, ROUND(AVG(delivery_time_mins),2) AS avg_delivery_time FROM restaurants GROUP BY city ORDER BY avg_delivery_time;

SELECT cuisine, ROUND(AVG(average_cost_for_two),0) AS avg_cost FROM restaurants GROUP BY cuisine ORDER BY avg_cost DESC;

SELECT COUNT(*) AS online_delivery_restaurants FROM restaurants WHERE is_online_delivery = 1;

SELECT ROUND(100.0 * SUM(CASE WHEN delivery_time_mins <= 30 THEN 1 ELSE 0 END)/COUNT(*),2) AS pct_under_30_mins FROM restaurants;

SELECT name, city, cuisine, aggregate_rating, delivery_time_mins FROM restaurants WHERE aggregate_rating >= 4.5 AND delivery_time_mins <= 30 ORDER BY aggregate_rating DESC;
