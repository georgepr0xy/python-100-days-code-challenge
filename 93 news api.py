import requests
import json
query=input("what type of news you want to see : ")

url ="https://newsapi.org/v2/everything?q={query}&from=2023-07-01&sortBy=publishedAt&apiKey=313e3ed011d64796bd97b03b36947dd1"
r=requests.get(url)
news = json.loads(r.text)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-------------------------------------------------")