from bs4 import BeautifulSoup
import requests

page = 1
url =f"https://www.yellowpages.com.au/search/listings?clue=Designer&eventType=pagination&locationClue=Canberra&pageNumber={page}&referredBy=www.yellowpages.com.au"
UA ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
cookie = '<enter the cookie>'
headers= {
    'user-agent' :UA,
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'cookie': cookie,
}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
# print(soup)

soup = BeautifulSoup(open('res.html'), 'html.parser')
# print(soup)
items = soup.findAll('div','search-contact-card-table-div cag-groups-2 cag-items-4')
print(items)
count =0
for item in items:
    names = item.find('a','listing-name').text
#     name = names.text
#     link = f"https://www.yellowpages.com.au{names['href']}"
#     phone = item.find('span','contact-text').text
#     email = item.find('a','contact contact-main contact-email')['data-email']
#     web = item.find('a','contact contact-main contact-url')['href']
#     try:
#         logo = item.find('img','listing-logo standard-logo')['src'].replace('//','')
#     except:
#         logo = 'No Logo'
#     headline = item.find('p','listing-heading').text.strip()
#     category = headline.split('-')[0].strip()
#     try:
#         addr = item.find('p','listing-address mappable-address mappable-address-with-poi').text
#     except:
#         addr = ''
#     print(names)
#     print(link)
#     print(phone)
#     print(email)
#     print(web)
#     print(logo)
#     print(headline)
#     print(addr)
#
#
#     count+=1
#     print(count)