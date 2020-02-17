import json
import urllib3
import os

http=urllib3.PoolManager()

city=input('the name of the city')
key='2dc12cf0db924773a835bcde81237483'
url='http://free-api.heweather.net/s6/weather/now?location='+city+'&key='+key

html=http.request('GET',url)
hjson=json.loads(html.data.decode())
nowtq_status=hjson['HeWeather6'][0]['now']

print('当前室外温度:\t%s度'%(nowtq_status['tmp'].encode('utf-8')))
print('体感温度:\t%s'%(nowtq_status['fl'].encode('utf-8')))
print('天气描述:\t%s'%(nowtq_status['cond_txt'].encode('utf-8')))
print('相对湿度(%):\t'+'%s%%'%(nowtq_status['hum'].encode('utf-8')))
print('风力/风向:\t%s/%s级'%(nowtq_status['wind_dir'].encode('utf-8'),nowtq_status['wind_sc'].encode('utf-8')))
print('能见度(km):\t%skm'%(nowtq_status['vis'].encode('utf-8')))

    