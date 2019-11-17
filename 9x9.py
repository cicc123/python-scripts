#print(i*j) for j in range(1,1+i) for i in range(10)
#print('\n'.join(['  '.join(['{}*{}={}'.format(j,i,i*j) for j in range(1, i+1)]) for i in range(1, 10)]))

#print((' '.join((['{}*{}={}'.format(j,i,i+j)) for j in range(1,i+1)])) for i in range(1,10))
#print('\n'.join([' '.join((['{}*{}={}'.format(j,5,5*j) for j in range(1,6)]))]))
#print('%s' % ''.join([str(i) for i in range(1,10)]))
#print('\n'.join((' '.join(['{}*{}={}'.format(j,i,j*i) for j in range(1,i+1)])) for i in range(1,10)))
#print('\n'.join((' '.join(['{}*{}={}'.format(j,i,j*i) for j in range(1,i+1)])) for i in range(1,10)))
#print(sum(range(1,101))
'''
def map(l:list):
    l1=[]
    for i in range(len(l)):
       l1.append(l[i]%2)
    return l1
a=[1,2,3,4]
print(map(a))
'''
#print(list(map(lambda x:x%2, [1,2,3,4])))
#print(list(map(lambda x:x**2,[1,2,3,4,5,6,7])))
#print(''.join(reversed(list('ilovechina'))))
print('iloveyou'[1:-1:2])