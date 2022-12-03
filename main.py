import requests
from send_mail import send_mail
import json

url =f"https://newsapi.org/v2/everything?q=tesla&from=2022-11-03&sortBy=\
       publishedAt&apiKey=6f620191b11f4e70bb25f3b8c6323e00"
api_key='6f620191b11f4e70bb25f3b8c6323e00'
#getting api using the key
request=requests.get(url)

content=request.json()
print(content)
body=""
for article in content['articles'][:20]:
    if article['title'] and article['description'] is not None:
        body='Subject:Todays News'\
             +'\n'+body+article['title']+2*"\n"+article['description']+2*"\n"
body = body.encode("utf-8")
print(body)
send_mail(body)