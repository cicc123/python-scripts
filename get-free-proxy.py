import requests
import re
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
url = 'http://www.goubanjia.com/'
response = requests.get(url=url,headers=headers)
tdip = re.finditer(r'''(<td class="ip">.*?</td>)''',response.text)
tdptl = re.finditer(r'''>(https?)<''',response.text)
ip=[]
ptl=[]
def get_port(port_word):
    word = list(port_word)
    num_list = []
    for item in word:
        num = 'ABCDEFGHIZ'.find(item)
        num_list.append(str(num))
    return str(int(''.join(num_list)) >> 0x3)

#with open(file='proxy.txt',mode='w',encoding='utf-8') as fp:
for i in tdip:
    match1 = re.sub(r'''<p style='display\s*:\s*none;'>.*?</p>''', '', i.group())
  #  print(i.group())
    match2 = re.sub(r'''<.*?>''', '', match1)
    port_mask = re.findall(r'''<span class="port ([A-Z]+)">''', match1)
    ip.append(re.sub(r''':\d+''', ':' + get_port(port_mask[0]), match2)+'\n')
for j in tdptl:
     ptl.append(j.group().lstrip('>').rstrip('<'))
with open(file='proxy_list.txt',mode='w') as fp:
    for k in range(len(ip)):
        fp.write(ptl[k] + '://' + ip[k])
