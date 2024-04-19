import requests

api_key = "3b790786035a48dc86c656d2c1689d7c"
url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=3b790786035a48dc86c656d2c1689d7c"

request = requests.get(url)
content = request.json()

print(content["articles"])