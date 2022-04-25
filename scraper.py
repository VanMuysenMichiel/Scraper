from bs4 import BeautifulSoup
import requests
from time import time, sleep
import logging 

x = 0
today = date.today()

while True:
    r = requests.get("https://www.blockchain.com/btc/unconfirmed-transactions")
    soup = BeautifulSoup(r.text)
    tags = soup.findAll('div', attrs={"class" : "sc-6nt7oh-0 PtIAf"})
    data = []
    for tag in tags:
      k = tag.text
      y= k.replace(" BTC", "")
      data.append(y)
    hashes = data[0::4]
    times = data[1::4]
    BTC1 = data[2::4]
    BTC = list(map(float, BTC1))
    USD = data[3::4]
    highest = max(BTC)
    index = BTC.index(highest)
    output = [hashes[index],times[index],str(BTC[index])+" BTC",USD[index]]
    if x == 0:
      logging.basicConfig(filename='VanMuysenMichiel.log', format='%(message)s', filemode='w')
      logger=logging.getLogger()
    if x > 0:
      print(output)
      with open('VanMuysenMichiel.log', 'a') as f:
        f.writelines('\n'.join(output))
        f.writelines('\n')
        f.writelines('\n')
    sleep(60 - time() % 60)
    x = x + 1