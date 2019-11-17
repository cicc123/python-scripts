with open(file='test.txt',mode='r+') as fp:
    num = int(fp.readline().split()[0])
    num +=1
    str1 = str(num)
fp.close()
with open(file='test.txt',mode='w') as fp:
    fp.write(str1)
fp.close()