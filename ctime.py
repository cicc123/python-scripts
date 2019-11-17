# coding:utf-8

import time
import re

def application(env, start_response):
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    start_response(status, headers)
#    return time.ctime()
    with open(file='count.txt',mode='r+') as fp:
        num = re.findall('\d+',fp.readline())
        if num == None:
            counter = 1
        else:
            counter = num[0]
    fp.close()
    with open(file='count.txt', mode='w') as fp:
        fp.write(str(int(counter)+1))
    fp.close()
    return counter