#!/usr/bin/env python
# encoding: utf-8
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36',
        'Referer': 'http://daglyfw.ecjtu.jx.cn:81/by/'}
url1 = 'http://daglyfw.ecjtu.jx.cn:81/by/servlet/Search'
data = {
        'sname': "default",
        'snumber': "20110410090114",
        'idcardNo': ""
        }
loginhtml = requests.post(url1, data=data, headers=head)
url2 = 'http://daglyfw.ecjtu.jx.cn:81/by/servlet/Search'
documenthtml = requests.get(url2, cookies=loginhtml.cookies, headers=head)
print documenthtml.text
