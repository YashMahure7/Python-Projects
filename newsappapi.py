import requests

query=input("What kind of news are you interested in today: ")

api="673b8e2ce4444f0b9f01dacca183755d"
url=f"https://newsapi.org/v2/everything?q={query}&from=2025-10-25&sortBy=publishedAt&apiKey={api}"

print(url)
r=requests.get(url)

data=r.json()
articles=data["articles"]

for index, article in enumerate(articles):
    print(index+1, article["title"], article["url"])
    print("\n---------------------------------------------------------------------\n")