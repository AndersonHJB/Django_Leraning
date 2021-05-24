from aip import AipOcr
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),}
#图片转文字模块
""" 你的 APPID AK SK """
APP_ID = '23771318'
API_KEY = '0wqWkZ0Ww50uz8hZu5G3WEgG'
SECRET_KEY = 'bPmhDxHDZQZb0GzGQoHWEE9QjGYhGta6'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

i = open('denggao.png','rb')
img = i.read()
message = client.basicGeneral(img)
for i in message.get('words_result'):
 print(i.get('words'))
#识别结果替换为变量
a=i.get('words')
#生成uuid
import datetime
import string
import random
from uuid import *

nod_uuid = lambda x: str(uuid5(NAMESPACE_X500, str(x) + str(datetime.datetime.now()) + ''.join(
    random.sample(string.ascii_letters + string.digits, 8))))

print(nod_uuid(''))

#创建索引
print(es.create(index='a1',id=nod_uuid(''),body={"内容":a}))