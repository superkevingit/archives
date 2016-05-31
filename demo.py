# encoding: utf-8
import requests
from bs4 import BeautifulSoup


head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36',
        'Referer': 'http://daglyfw.ecjtu.jx.cn:81/by/'}
url = 'http://daglyfw.ecjtu.jx.cn:81/by/servlet/Search'
data = {
    'snumber': "20110410090114",
}
infos = ['XM', 'SFZH', 'XY', 'ZYMC', 'STUDENTCODE', 'BJ']
hire_infos = ['JYTXBM', 'DAJSDZ', 'PQDWSZD']
html = requests.post(url, data=data, headers=head)
soup = BeautifulSoup(html.text, "html.parser")
for info in infos:
    xy = soup.find(id=info)["value"]
    print xy
for hire_info in hire_infos:
    hire = soup.find(id=hire_info).get_text()
    print hire
