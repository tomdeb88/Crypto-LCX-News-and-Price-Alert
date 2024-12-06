import datetime as dt
import requests
import os

NEWS_API=os.environ.get("NEWS_API")

#getting today's date
now=dt.datetime.now()
today=f"{now.year}-{now.month}-{now.day}"

news_url="https://newsapi.org/v2/everything"

search_parameters={
    'apiKey':NEWS_API,
    'q':["LCX Crypto","LCX token","LCX Exchange"],
    'searchIn':"content,title,description",
    'from':today,
    'sortBy':'popularity',
    'pageSize':3,
    'language':'en'
}

response=requests.get(url=news_url,params=search_parameters)
response.raise_for_status()
data=response.json()







