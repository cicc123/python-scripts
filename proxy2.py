import get_free_proxy_v2
import requests
import random
import time

#print(get_free_proxy_v2.get_proxy())
proxies = [{'https':'https://106.14.3.97:6666'},
{'http':'http://221.238.207.39:81'},
{'https':'https://117.95.9.180:61234'},
{'http':'http://121.17.210.114:8060'},
{'https':'https://61.173.3.137:9090'},
{'https':'https://119.97.172.186:4321'},
{'http':'http://39.137.69.6:8080'},
{'https':'https://27.159.72.44:65001'},
{'http':'http://116.114.19.204:443'},
{'http':'http://111.29.3.226:8080'},
{'http':'http://111.29.3.221:8080'},
{'http':'http://111.29.3.194:8080'},
{'http':'http://111.29.3.224:8080'},
{'http':'http://111.29.3.185:8080'},
{'http':'http://111.29.3.184:8080'},
{'http':'http://111.29.3.220:8080'},
{'http':'http://111.29.3.195:80'},
{'http':'http://111.29.3.187:8080'},
{'http':'http://111.29.3.225:8080'},
{'https':'https://39.108.245.29:20113'}]
while True:
    response = requests.get('http://youtube.com', proxies=random.choice(proxies))
    print('via proxy ' + response.text.strip())
    time.sleep(1)