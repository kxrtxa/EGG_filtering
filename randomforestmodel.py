import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Load the mapped features dataset
df = pd.read_csv("mapped_eeg_features.csv")

# Drop the 'Type' column if present
df = df.drop(columns=['Type'], errors='ignore')

# Use only the first (180 rows) as input (Noisy) and the next (180 rows) as output (Clean)
X = df.iloc[:180, :-4]  # Exclude the last 4 columns (reserved for testing)
Y = df.iloc[180:360, :-4]  # Corresponding clean data

# Ensure indexing is reset for clean mapping
Y = Y.reset_index(drop=True)

# Split data into train and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, Y_train)

# Predictions on test data
Y_pred = model.predict(X_test)

# Evaluate model performance
mae = mean_absolute_error(Y_test, Y_pred)
print(f"Mean Absolute Error: {mae}")

# Save the trained model
import joblib
joblib.dump(model, "random_forest_eeg_model.pkl")

print("Model training completed and saved as 'random_forest_eeg_model.pkl'")
