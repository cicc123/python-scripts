from collections import defaultdict
with open(file='words.txt',mode='r') as fp:
    words = fp.readlines()
fp.close()
l = defaultdict(int)
#print(l)
for i in range(len(words)):
    for j in range(len(words[i].strip().split(' '))):
        l[words[i].strip().split(' ')[j]] += 1
l1 = sorted(l.items(), key=lambda x:x[1])
for i in range(1000):
    print(l1.pop())