# -*- coding:utf-8 -*-
import requests
url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=20191031814386'

session = requests.session()
headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }
pc_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Cookie': 'anonymid=k2x3vmqf-9pdxrl; depovince=GW; _r01_=1; JSESSIONID=abcHD8lW4eHmn7jTAlK5w; ick_login=d5a93646-e0d9-45a8-9826-1c753a7ba0bd; _de=F84DEE386FDF5937; ick=1ab6b029-3b34-416b-aed1-b57e84a86bfb; t=8458c1b37d27580dc263f4bde34aee890; societyguester=8458c1b37d27580dc263f4bde34aee890; id=972853730; xnsid=9ba4b08a; XNESSESSIONID=c5432dd3d0b5; jebecookies=a022bd0a-1b99-4a97-9e87-fd6f50c295cc|||||; ver=7.0; loginfrom=null; wp_fold=0'

}

get_url = 'http://www.renren.com/972853730/profile'
#session.post(url=url, headers=pc_headers, data=cookies)
#response = session.get(url=get_url,headers=pc_headers)
#response.encoding='utf-8'

response = requests.get(url=get_url,headers=pc_headers)

print(response.text)
with open(file='renren-cookie.html',mode='w',encoding='utf-8') as fp:
    fp.write(response.text)