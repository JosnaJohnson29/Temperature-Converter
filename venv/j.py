import requests

city_name = "Chennai"
api_key = "2dc84e4fb970658c88a4894bc8bcabdf"

url = "https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

response = requests.get(url)
data = response.json()

print(data)