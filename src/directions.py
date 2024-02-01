import requests
import json
import os
from tqdm import tqdm 
from datetime import datetime   
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('Google_API_KEY')
if not API_KEY:
    raise ValueError("No API_KEY found.")

date = datetime.now().strftime('%Y-%m-%d %H:%M')
timestamp = datetime.now().timestamp()


base_url = "https://maps.googleapis.com/maps/api/directions/json"
destination_place_id = "ChIJWwWza3sadkgR77gsD5ccs70"
lse_accommodations = {
    "Urbanest Westminster Bridge Student Accomodation": "ChIJP0pRvrgEdkgR9BMcCzmR0bM",
    "Lilian Knowles House": "ChIJfRFPibMcdkgR7IhIkV7vGwo",
    "College Hall": "ChIJCyFK4S8bdkgRlSzWqrwRglg",
    "International Hall": "ChIJYUbmBTcbdkgRjiBhxz6q7qU",
    "LSE Butler's Wharf": "ChIJr6t3UkYDdkgRE7x7168Sm7k",
    "Bankside House": "ChIJPUtU26gEdkgR3nL-avgjmOM",
    "LSE Carr-Saunders Hall": "ChIJdRIvpikbdkgRmQr7-OPt8KY",
    "Unite Students - Sidney Webb House": "ChIJHwX_fV4DdkgRsM6csCYOlhY",
    "Connaught Hall": "ChIJ10m-4y8bdkgRtMt9BZfpeKw",
    "LSE High Holborn": "ChIJ4-06ODMbdkgRLAh7hcFiy9M",
    "Passfield Hall": "ChIJG93Rii8bdkgRx94YE5spvrM",
    "Nutford House, London": "ChIJMZzK8soadkgR3hFDJScRqUo",
    "Garden Halls": "ChIJdSS3YTobdkgR5kspQSjORnU",
    "Rosebery Hall": "ChIJbVq3PEUbdkgR2aNFq1irjBM"}

modes = ['walking','bicycling','driving','transit']
transit_modes = ['subway', 'bus']

request_params = []

for mode in tqdm(modes, desc='Modes'):
    filename = f'data/directions_{mode}_{date}.jsonl'
    file_path = os.path.join(filename)
    
    for accommodation, place_id in tqdm(lse_accommodations.items(), desc='Accommodation'):
        if mode == 'transit':

            for transit_mode in tqdm(transit_modes, desc='Transit Modes'):
                filename = f'data/directions_{mode}_{transit_mode}_{date}.jsonl'
                file_path = os.path.join(filename)

                params = {         
                    'origin': 'place_id:' + place_id,
                    'destination': 'place_id:' + destination_place_id,
                    'key': API_KEY, 
                    'mode': mode,
                    'transit_mode': transit_mode
                }
                request_params.append((params, file_path)) #Mind the Indentation

        else:
            params = {         
                'origin': 'place_id:' + place_id,
                'destination': 'place_id:' + destination_place_id,
                'key': API_KEY, 
                'mode': mode
                }
            request_params.append((params, file_path))


for params, file_path in tqdm(request_params, desc='Requests'):  
    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        print(f"Failed to fetch data for {accommodation}: HTTP Status Code {response.status_code}")
    else:
        resp = response.json()
        resp['timestamp'] = timestamp
        resp['date'] = date
        resp = json.dumps(resp) 
        with open(file_path, 'a+') as f:        
            f.write(resp + '\n')

print("Data have been saved to respective files.")
