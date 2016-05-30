# encoding: utf-8
import requests


head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36',
        'Referer': 'http://daglyfw.ecjtu.jx.cn:81/by/'}
url = 'http://daglyfw.ecjtu.jx.cn:81/by/servlet/Search'
data = {
    'sname': "default",
    'snumber': "20110410090114",
    'idcardNo': ""
}
html = requests.post(url, data=data, headers=head)
print(html.text)
