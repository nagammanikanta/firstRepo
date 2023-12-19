from hmac import new
from sqlite3 import paramstyle
import requests
import csv

url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen"

querystring = {"formatType":"test"}

headers = {
	"X-RapidAPI-Key": "7dd05ca27bmsh9118c5565e3d6d6p1a52c7jsn470e396b1d41",
	"X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
}

params = {
    "formatType": "odi"
}

response = requests.get(url, headers=headers, params=querystring)


if response.status_code == 200:
    data = response.json().get('rank', [])
    csv_filename = 'batsmen_rankings.csv'
    if data:
        field_names = ['rank', 'name', 'country']
        with open(csv_filename, 'w',newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            for entry in data:
                writer.writerow({field: entry.get(field) for field in field_names})
                print(f'Data fetched successfully and written to {csv_filename}')
            else:
                print("No data avaiable frm the API.")
   
    else:
        print("failed to fetch data:", response.status_code)
