import os
import requests
from datetime import datetime,timedelta

ARROW_UP="⬆️"
ARROW_DOWN="⬇️"

PRICE_API=os.environ.get("PRICE_API")

yesterday_date=datetime.now()-timedelta(1)
yesterday=datetime.strftime(yesterday_date,'%d-%m-%Y')

url_today_data = "https://api.coingecko.com/api/v3/simple/price?ids=lcx&vs_currencies=usd&include_market_cap=true&include_24hr_change=true&precision=3"
url_yesterday_data = f"https://api.coingecko.com/api/v3/coins/lcx/history?date={yesterday}&localization=false"


headers = {
    "x-cg-demo-api-key": PRICE_API
}

response_1 = requests.get(url=url_today_data,headers=headers)
response_2=requests.get(url=url_yesterday_data,headers=headers)
today_data=response_1.json()
yesterday_data=response_2.json()

# get today's lcx price
lcx_price=today_data['lcx']['usd']

# get yesterday's lcx price
lcx_yesterday_price=yesterday_data['market_data']['current_price']['usd']
lcx_yesterday_price=round(lcx_yesterday_price,3)

# get market cap value
lcx_market_cap=round(today_data["lcx"]["usd_market_cap"])
lcx_market_cap="{:,} USD".format(lcx_market_cap)




#get percentage change
def percent_difference():
    result=round(float(((lcx_price - lcx_yesterday_price) * 100) / lcx_yesterday_price), 2)
    if lcx_price>lcx_yesterday_price:
        return f"{result}% {ARROW_UP}"
    elif lcx_price<lcx_yesterday_price:
        return f"{result}% {ARROW_DOWN}"
    else:
        return  f"{result}%"

