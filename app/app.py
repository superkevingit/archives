# encoding: utf-8
from flask import Flask
from flask.ext.script import Manager
import requests
from bs4 import BeautifulSoup
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = '\xa1b\xcb\xb5\x9f\xb3N\x1b\xf7\xe9kC\x7f_\xa2\xf2k\x04 \xc2n0(\x93'
manager = Manager(app)
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36',
        'Referer': 'http://daglyfw.ecjtu.jx.cn:81/by/'}
url = 'http://daglyfw.ecjtu.jx.cn:81/by/servlet/Search'
infos = ['XM', 'SFZH', 'XY', 'ZYMC', 'STUDENTCODE', 'BJ']
hire_infos = ['JYTXBM', 'DAJSDZ', 'PQDWSZD']


@app.route('/<student_id>')
def app(student_id):
    data = {
        'snumber': student_id,
    }
    html = requests.post(url, data=data, headers=head)
    soup = BeautifulSoup(html.text, "html.parser")
    details = []
    for info in infos:
        detail = soup.find(id=info)["value"]
        details.append(detail)
    for hire_info in hire_infos:
        data = soup.find(id=hire_info).get_text()
        details.append(data)
    if details[8] == '':
        back_dict = {'result': False, 'details': {}}
        return json.dumps(back_dict)
    else:
        details_dict = {
            u'姓名': details[0],
            u'身份证号': details[1],
            u'学院': details[2],
            u'专业名称': details[3],
            u'学号': details[4],
            u'班级': details[5],
            u'EMS单号': details[6],
            u'邮寄地址': details[7],
            u'接受单位名称': details[8]
        }
        back_dict = {'result': True, 'details': details_dict}
        return json.dumps(back_dict)


if __name__ == '__main__':
    manager.run()
