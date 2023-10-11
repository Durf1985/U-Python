import requests
from datetime import datetime, timedelta
from newsapi import NewsApiClient

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stock_param = {
    "function": "TIME_SERIES_DAILY",
    "apikey": "VYVY98BO2ZK2QZDR",
    "symbol": "TSLA",
    "outputsize": "compact"

}

data = requests.get(url=STOCK_ENDPOINT, params=stock_param)
data.raise_for_status()

today = data.json()["Meta Data"]["3. Last Refreshed"]
previous_day = (datetime.strptime(today, "%Y-%m-%d") - timedelta(days=1)).strftime("%Y-%m-%d")

today_close_price = data.json()["Time Series (Daily)"][today]["4. close"]
yesterday_close_price = data.json()["Time Series (Daily)"][previous_day]["4. close"]

print(today_close_price, yesterday_close_price)
diff = abs(float(today_close_price) - float(yesterday_close_price))
diff_percent = (diff / float(yesterday_close_price)) * 100

if diff_percent > 0.5:
    news_param = {
        "apiKey": "288965ae41074d108845cb45851b72ec",
        "q": "tesla"
    }
    newsapi = NewsApiClient(api_key='288965ae41074d108845cb45851b72ec')
    top_headlines = newsapi.get_top_headlines(q="tesla", language='en', page_size=3)
    for article in top_headlines["articles"]:
        print(article["title"])



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
