import pandas as pd
import requests
import json

# Step 1: Read the CSV file
csv_file = "creditcard.csv"  # Replace with the path to your CSV file
data = pd.read_csv(csv_file)
print(f"Number of data points: {len(data)}")

# Step 2: Remove the 'Class' column
if 'Class' in data.columns:
    data = data.drop(columns=['Class'])

# Step 3: Convert the DataFrame to a JSON array
json_data = data.to_json(orient='records')

# Step 4: Make a network call to the Flask API
url = "http://127.0.0.1:5000/predict"  # Replace with your Flask API URL

headers = {'Content-Type': 'application/json'}  # Set the content type to JSON

try:
    # Sending the POST request
    response = requests.post(url, data=json_data, headers=headers)
    
    # Step 5: Print only fraud transactions (predicted as 1)
    if response.status_code == 200:
        predictions = response.json().get('predictions', [])
        fraud_indices = [i for i, pred in enumerate(predictions) if pred == 1]  # Indices of fraud predictions
        fraud_transactions = data.iloc[fraud_indices]  # Select corresponding rows from the original data
        
        print("Fraud Transactions:")
        print(fraud_transactions)  # Display fraud transactions
    else:
        print(f"Error: {response.status_code}")
        print(response.text)  # Print error details
except Exception as e:
    print(f"An error occurred: {e}")
