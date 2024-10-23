import requests



url = f'https://api.telegram.org/bot{token}/getUpdates'
url_send = f'https://api.telegram.org/bot{token}/sendMessage'


user_bot = 5159283492
data = {'chat_id': user_bot, 'text': 'погода не очень'}
# res = requests.get(url_send, json=data)

res = requests.get(url)
print(res.json())

# 7985795571:AAFs5VcM9Yo7K-CY8ufRPcl-zrMreKukPLc
