import requests
import csv
import json

api_key = 'f4d0c423ad17b0541176f737878aa966'
city = 'Jinja'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'


# Make a request to the OpenWeatherMap API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

# Extracting specific data
    weather_data = {
        "city": city,
        "temperature": data['main']['temp'],
        "weather_description": data['weather'][0]['description'],
        "humidity": data['main']['humidity'],
        "wind_speed": data['wind']['speed']
    }

# Save to JSON file
    json_file = 'weather_data.json'
    with open(json_file, mode='w', encoding='utf-8') as file:
        json.dump(weather_data, file, indent=4, ensure_ascii=False)

# Save to CSV file using csv module
    csv_file = 'weather_data.csv'
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=weather_data.keys())
        writer.writeheader()
        writer.writerow(weather_data)
    
# Confirm data saved
    print(f'Data saved to {csv_file} and {json_file}')
else:
    print(f"Error: {response.status_code}")