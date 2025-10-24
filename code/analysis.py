import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load data
df = pd.read_csv('data/zomato_sample.csv')
print('Loaded', len(df), 'rows')

# Basic EDA
print('Average rating:', df['aggregate_rating'].mean())
print('Median delivery time:', df['delivery_time_mins'].median())

# Save cleaned data to SQLite
conn = sqlite3.connect('data/zomato.db')
df.to_sql('restaurants', conn, if_exists='replace', index=False)
print('Saved to SQLite: data/zomato.db')

# Run a sample SQL query
q = """SELECT city, COUNT(*) AS total_restaurants, ROUND(AVG(aggregate_rating),2) AS avg_rating
FROM restaurants GROUP BY city ORDER BY total_restaurants DESC;"""
print(pd.read_sql(q, conn))

# Prepare features for predicting delivery time
# Use numeric features: aggregate_rating, votes, average_cost_for_two, is_online_delivery
X = df[['aggregate_rating','votes','average_cost_for_two','is_online_delivery']].copy()
y = df['delivery_time_mins']
# Basic preprocessing
X['votes'] = np.log1p(X['votes'])  # reduce skew

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)
preds = model.predict(X_test)

# Metrics
mse = mean_squared_error(y_test, preds)
r2 = r2_score(y_test, preds)
print(f'MSE: {mse:.2f}, R2: {r2:.2f}')

# Save predictions
out = X_test.copy()
out['actual_delivery_time'] = y_test.values
out['predicted_delivery_time'] = np.round(preds,1)
out.to_csv('data/predictions.csv', index=False)
print('Saved data/predictions.csv')

# Plot actual vs predicted (scatter)
plt.scatter(out['actual_delivery_time'], out['predicted_delivery_time'])
plt.xlabel('Actual Delivery Time (mins)')
plt.ylabel('Predicted Delivery Time (mins)')
plt.title('Actual vs Predicted Delivery Time')
plt.tight_layout()
plt.savefig('data/actual_vs_predicted.png')
print('Saved data/actual_vs_predicted.png')
conn.close()
