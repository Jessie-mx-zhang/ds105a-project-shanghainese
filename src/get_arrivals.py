import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
if not API_KEY:
    raise ValueError("No API_KEY found.")

base_url = 'https://api.tfl.gov.uk/Line/{lines}/Arrivals/{station_id}'
params = {'app_key': API_KEY}
lines = ['1', '59', '68', '91', '188', '243', 'N1', 'N68', 'N91', 'N171', 'SL6',
          '9', '23','87', '172', 'N9', 'N44', 'N87', 'N155']
station_ids = ['490000112M', '490003191F', '490019703Z']

combinations = [(line, station_id) for line in lines for station_id in station_ids]

filename = 'arrival.jsonl'
file_path = os.path.join('data', filename)
os.makedirs(os.path.dirname(file_path), exist_ok=True)

with open(file_path, 'a') as file:

    urls = [base_url.format(lines=line, station_id=station_id) for line, station_id in combinations]
    responses = [requests.get(url, params=params) for url in urls]

    for response in responses:
        if response.status_code == 200:
            data = response.json()        
            if isinstance(data, list):
                for record in data:
                    if record: 
                        json_record = json.dumps(record)
                        file.write(json_record + '\n')
                    else:
                        continue
            else:
                json_record = json.dumps(data)
        else:
            print(f"Failed to fetch data for line {lines}: HTTP Status Code {response.status_code}")

print("Data has been saved to arrival.jsonl")
