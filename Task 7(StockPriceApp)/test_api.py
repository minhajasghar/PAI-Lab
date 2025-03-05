import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "Adj Close": 11,
    "High": 13,
    "Low": 13,
    "Open": 13,
    "Volume": 467832400,
    "Target": -1,
    "Score": 467832400
}

response = requests.post(url, json=data)
print(response.json()) 
