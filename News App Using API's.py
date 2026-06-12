import requests

querry = input("What News do you want to read about?: ")
key = "" # Enter Here Your API Key (you can get it from newsapi.org)

url = f"https://newsapi.org/v2/everything?q={querry}&from=2026-05-12&sortBy=publishedAt&apiKey={key}"

a = requests.get(url)
data = a.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index+1, article["title"], article["url"])
    print("\n***********************\n")

