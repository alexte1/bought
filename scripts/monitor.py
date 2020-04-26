# https://chrisalbon.com/python/web_scraping/monitor_a_website/
# https://2.python-requests.org//en/master/user/quickstart/
# https://elitedatascience.com/python-web-scraping-libraries
import requests
from bs4 import BeautifulSoup
import time

start = time.time()
req = requests.get("https://www.supremenewyork.com/shop/accessories/rzo2wtqnr/f87bjgxz6")
soup = BeautifulSoup(req.text, 'lxml')
# a = soup.select("script")
# print(a[0])
print(soup.prettify())
print("Total time: {}".format(time.time()-start))