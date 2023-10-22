import requests

city_name = input('Enter a city name:')
print(city_name)
print('Display weather report for:', city_name)
url = f'https://www.accuweather.com/{city_name}'
res = requests.get(url)
print(res.text)