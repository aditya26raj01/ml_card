import pandas as pd

df = pd.read_csv('creditcard.csv').head(5).drop(columns=['Amount', 'Class'])
json_data = df.to_json(orient='records')
print(json_data)