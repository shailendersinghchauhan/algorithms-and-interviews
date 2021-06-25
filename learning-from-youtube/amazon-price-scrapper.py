import requests
#from bs4 import BeautifulSoup
import bs4
def get_price():
 url = 'https://www.amazon.in/Practical-Site-Reliability-Engineering-developing/dp/1788839560'
 headers = {
     "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0'
 }
 page = requests.get(url,headers=headers)
 soup = BeautifulSoup(page.content,'html.parser')

 title = soup.find
 #price = soup.find(id="a-autoid-7-announce").get_text()
 print(title)

get_price()