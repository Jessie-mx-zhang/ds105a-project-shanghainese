import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('API_KEY')
if not api_key:
    raise ValueError("No API_KEY found.")


base_url = 'https://api.tfl.gov.uk/Line/{line}/Timetable/{station_id}'
params = {'app_key': api_key,
          'direction': 'inbound'}
lines = ['1', '59', '68', '91', '188', '243', 'N1', 'N68', 'N91', 'N171', 'SL6',
         '9', '23','87', '172', 'N9', 'N44', 'N87', 'N155']
station_ids = ['490000112M', '490003191F', '490019703Z']

combinations = [(line, station_id) for line in lines for station_id in station_ids]


filename = 'timetable.jsonl'
file_path = os.path('data', filename)


with open(file_path, 'a') as file:
    for line, station_id in combinations:
        url = base_url.format(line=line, station_id=station_id)
        response = requests.get(url, params=params)
        
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
                if data:
                    json_record = json.dumps(data)
                    file.write(json_record, '\n')
        else:
            print(f"Failed to fetch data for line {line}: HTTP Status Code {response.status_code}")

print("Data has been saved to timetable.jsonl")