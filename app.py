import requests
import urllib.request 
from bs4 import BeautifulSoup as bs
import pandas as pd
import datetime 
import asyncio




i = 1
all_ids = []





for _ in range(1,60):
    site_url = f'https://v-tylu.work/?transaction_type=offering-with-online-payment&page={i}'
    html_parse = urllib.request.urlopen(site_url)

while True:

    site_url = f'https://v-tylu.work/?transaction_type=offering-with-online-payment&page={i}'
    html_parse = urllib.request.urlopen(site_url)


    print(html_parse)

    ids = []
    # htmlParse = list(bs(html_parse, 'html.parser').find_all('h2'))
    # for item in htmlParse:
    #         a_tag = item.find('a')
    #         if a_tag is not None:
    #             href_attr = a_tag.attrs['href']
    #             id = href_attr.split('/')[3][:7]
    #             ids.append(id)
    #             all_ids.append(id)
    # if ids == []:
    #     break
    i=i+1
    if i > 3:
        break
    print(i)



# payload = {
#     "ids": all_ids,
#     "language": "uk"
# }

# header_post = {
# 'authority': 'listing-service.v-tylu.com',
# 'method': 'POST',
# 'path': '/work/listings',
# 'scheme': 'https',
# 'accept': 'application/json',
# 'accept-encoding': 'gzip, deflate, br',
# 'accept-language': 'en,ru;q=0.9,ru-RU;q=0.8,en-US;q=0.7,la;q=0.6,tr;q=0.5,az;q=0.4',
# 'content-length': '265',
# 'content-type': 'application/json',
# 'origin': 'https://v-tylu.work',
# 'referer': 'https://v-tylu.work/',
# 'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
# 'sec-ch-ua-mobile':'?0',
# 'sec-ch-ua-platform': "Linux",
# 'sec-fetch-dest': 'empty',
# 'sec-fetch-mode': 'cors',
# 'sec-fetch-site': 'cross-site',
# 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
# }
# url_post = 'https://listing-service.v-tylu.com/work/listings'

# res = requests.request(method='POST', url=url_post, json=payload)

# data = res.json()

# print(data)



# async def count(i):
#     print(i)
#     await asyncio.sleep(1)
#     print("hm")




    


# async def main():
#     for item in datas:
#         asyncio.create_task(count(item))

#         # asyncio.gather(count(item))


# asyncio.run(main())



