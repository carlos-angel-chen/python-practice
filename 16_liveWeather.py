from bs4 import BeautifulSoup
from matplotlib.backend_bases import LocationEvent
from requests import request
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/58.0.3029.110 Safari/537.3'}

def weather(city):
    city = city.replace(" ","+")
    res = requests.get(f'https://www.google.com/search?q={city}\
        &oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=\
        chrome&ie=UTF-8', headers=headers)
    print("Searching....")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    
    return location, time, info, weather

city = input("Enter a city name: ")
city = city+" weather"

location, time, info, temp = weather(city)
print(location)
print(time)
print(info)
print(temp+" C")