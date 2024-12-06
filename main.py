from article import Article
from api_articles import data
import price_api
from twilio.rest import Client
import os

twilio_account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
my_number=os.environ.get('MY_PHONE_NUMBER')


number_of_articles=len(data['articles'])
list_of_articles=list()

info_message = f"{price_api.lcx_price}$ {price_api.percent_difference()} MC: {price_api.lcx_market_cap}\n"
client = Client(twilio_account_sid, twilio_auth_token)


if number_of_articles<1:
    info_message+='No articles today'
else:
    for num in range(number_of_articles):
        source=data['articles'][num]['source']['name']
        author=data['articles'][num]['author']
        title=data['articles'][num]['title']
        description=data['articles'][num]['description']
        link=data['articles'][num]['url']
        article=Article(source,author,title,description,link)
        list_of_articles.append(article)
    for art in list_of_articles:
        info_message+=art.get_article()
        message = client.messages.create(
            from_='+17752786214',
            body=info_message,
            to=my_number
        )

print(info_message)

