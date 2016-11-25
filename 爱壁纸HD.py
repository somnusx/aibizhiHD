import re
import requests
import redis

url = 'http://api.lovebizhi.com/windows_v3.php?a=index&model_id=106&width=1366&height=768&client_id=1004&channel=30001&uuid=2f1187596eb64b40b772fa9eb517cc25&screen_width=1366&screen_height=768&bizhi_width=1366&bizhi_height=768&language=zh-CN&version_code=33&runtime_version=4.0.30319.42000&os_version=6.2.9200.0&device_id=69332240=1004&platform=windows&brand=&model=&manufacturer=ASUSTeK%20COMPUTER%20INC.&os_apilevel=0&imei=&device_id=69332240'



def req(url):    
    r = requests.get(url).text
    links = re.findall(r'http:\\/\\/api.lovebizhi.com.+?(?=")',r)
    pe = re.findall(r'http:\\/\\/s.qdcdn.com\\/c.+?(?=")',r)

    for i in pe:
        i = i.replace('\\','')
        if not red.get(i):
            red.set(i,i)
            print('runing.................')
            with open('HD.txt','ab') as code:
                code.write(i + '\r\n')

    if links:
        for l in links:
            print 0
            if not red.get(l):
                red.set(l,l)
                lin = l.replace('\\','')
                req(lin)
                            

if __name__ == '__main__':
    red = redis.StrictRedis(host='127.0.0.1',port=6379,db=1)
    red.set(url,url)
    req(url)
