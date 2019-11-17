import dns.resolver
import os

domain = 'nginx3'

A = dns.resolver.query(domain, 'A')
for i in A.response.answer:
        for j in i.items:
#               print(j.address)
                line ='/usr/local/bin/bridge_server -u http://'+j.address
                print(line)
                os.system(line)
