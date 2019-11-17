import random
import re
words=words1=[]
with open(file='linux.words',mode='r') as fp:
    words = fp.readlines()
fp.close()
pattern = re.compile('[^\d-]+$')
for i in range(len(words)):
    words[i] = words[i].strip()
    if re.match(pattern,words[i]):
        words1.append(words[i])
with open(file='words.txt',mode='w') as fp:
    for i in range(100000):
        fp.write(' '.join(random.sample(words1,5),)+"\n")
fp.close()