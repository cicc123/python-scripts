from bs4 import BeautifulSoup
import requests
import re
p = ''
def get_port(port_word):
        word = list(port_word)
        num_list = []
        for item in word:
            num = 'ABCDEFGHIZ'.find(item)
            num_list.append(str(num))
        return str(int(''.join(num_list)) >> 0x3)
def get_proxy():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    url = 'http://www.goubanjia.com/'
    response = requests.get(url=url,headers=headers)
    soap = BeautifulSoup(response.content,'lxml')
    proxy=[]
    p=[]
    x =1
    for o_td in soap.find_all(["td","a"]):
#        print(x,o_td)
        tags = o_td.find_all(["span","div","a"])
        a=[]
        for tag in tags:
#            print(tag.attrs)
            if tag.name == 'a':
                if tag.contents[0]  in ('http','https'):
 #                   global p
                    p.append(tag.contents[0])
                   # print(p)
                    continue
                else:
                    continue
#            print(x,p)
            if tag.string != None:
                a.append(tag.string)
  #              print(tag)
            if tag.attrs != {} and tag.get('class') != None:
                pre_port = get_port(tag['class'][1])
                #print(a)
 #               print(tag)
                proxy.append(''.join(a[:-1])+':'+pre_port)
       #         proxy[''.join(a[:-1])+':'+pre_port] = p
#                proxy[''.join(a[:-1]) + ':' + str(x)] = p
 #       break
        x+=1
    return dict(zip(proxy,p))
#    return proxy,p
if __name__ == "__main__":
    print(get_proxy())