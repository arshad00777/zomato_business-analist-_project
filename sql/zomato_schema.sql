CREATE DATABASE IF NOT EXISTS zomato_analysis;
-- For SQLite just create a table
CREATE TABLE restaurants (
    restaurant_id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT,
    cuisine TEXT,
    aggregate_rating REAL,
    votes INTEGER,
    average_cost_for_two INTEGER,
    delivery_time_mins INTEGER,
    is_online_delivery INTEGER,
    has_table_booking INTEGER,
    restaurant_type TEXT
);
