# encoding: utf-8
import requests
from bs4 import BeautifulSoup


head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36',
        'Referer': 'http://daglyfw.ecjtu.jx.cn:81/by/'}
url = 'http://daglyfw.ecjtu.jx.cn:81/by/servlet/Search'
data = {
    'sname': "default",
    'snumber': "20110410090114",
    'idcardNo': ""
}
html = requests.post(url, data=data, headers=head)
soup = BeautifulSoup(html.text, "html.parser")
xy = soup.find(id="XY")["value"]
