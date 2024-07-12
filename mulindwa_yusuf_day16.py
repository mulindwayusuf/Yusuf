# Web Scrapping
# Libraries for web-scrapping;
# Request, BeautifulSoup, lxml, scrappy, Selenium
# API keys

# step1:
import requests
from bs4 import BeautifulSoup
import csv
import json

# step2: Fetch the web pages

url = 'http://ryeko.org'
response = requests.get(url)
html_content = response.text
# api_key = 'your api key'

# step3: Parse the html using beautifulsoup
soup = BeautifulSoup(html_content, 'html.parser')

# step4: Find the specific data
data = []
for item in soup.find_all('a'):
    title = item.text.strip()
    link = item.get('href')
    data.append({'title': title, 'link': link})
 


# step5: Save the data to csv
csv_file = 'weather_data.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'link'])
    writer.writeheader()
    for row in data:
       writer.writerow(row)
# step6: Save the data to json
json_file = 'weather_data.json'
with open(json_file, mode='w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# step7: print the data
print(f'Data saved seccessfully to {csv_file} and {json_file} format!')


# Exercises , scrape data from the http://openweathermap.org
# get the current weather data,
