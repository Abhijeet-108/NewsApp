import requests
from send_email import send_email

api_key = "3b790786035a48dc86c656d2c1689d7c"
url = ("https://newsapi.org/v2/top-headlines?country=us&"\
       "category=business&apiKey=3b790786035a48dc86c656d2c1689d7c")

request = requests.get(url)

content = request.json()

body = ""
for article in content["articles"]:
    '''title = article["title"]
    description = article["description"] if article["description"] else ""
    body += f"{title}\n{description}\n\n"'''
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)

