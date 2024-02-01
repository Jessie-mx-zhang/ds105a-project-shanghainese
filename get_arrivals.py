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

combinations = [(line, station_id) for station_id in station_ids]