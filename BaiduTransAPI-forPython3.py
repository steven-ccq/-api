# BaiDu翻译的官方api调用示例，下方的appid和secretKey是我注册账号后申请的，在使用时请输入自己的APP ID与密钥

import http.client
import hashlib
import urllib
import random
import json

appid = '20200222000387204'  # 填写你的appid
secretKey = 'phr2Wy_0ZScBYzVb7eJl'  # 填写你的密钥

httpClient = None
myurl = '/api/trans/vip/translate'

fromLang = 'auto'   #原文语种
toLang = 'zh'   #译文语种
salt = random.randint(32768, 65536)
q= 'apple'
sign = appid + q + str(salt) + secretKey
sign = hashlib.md5(sign.encode()).hexdigest()
myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
salt) + '&sign=' + sign

try:
    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)

    response = httpClient.getresponse()
    result_all = response.read().decode("utf-8")
    result = json.loads(result_all)

    print (result['trans_result'][0]['dst'])

except Exception as e:
    print (e)
finally:
    if httpClient:
        httpClient.close()