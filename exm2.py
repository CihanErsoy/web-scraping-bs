import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# specify the url
sayfa = "https://www.coinmarketcap.com"

# query the website and return the html to the variable ‘page’
page = urllib.request.urlopen(sayfa).read()

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

list1 = list()
list2 = list()
isimler =soup.find_all('a', attrs={'class':'currency-name-container link-secondary'})
for y in isimler:
    b=y.text
    list1.append(b)

sonuc = soup.find_all('a', attrs={'class':'price'})
for x in sonuc:
    a=x.text
    list2.append(a)

for m, n in zip(list1, list2):
    print(m,":", n)
