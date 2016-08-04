import collections
out=[
    ['G','A','V','L','I'],
    ['S','C','T','M'],
    ['P'],
    ['F','Y','W'],
    ['D','E','N','Q'],
    ['H','K','R']
    ]

fc=open("c:/Users/sony vaio/Desktop/core.txt",'r')
cores=fc.readlines()
cores=[i.rstrip() for i in cores]
cores=''.join(cores)

count=collections.Counter(cores)
print count


total=[]
k=0
for i in out:
    total.append(0)
    for j in i:
        total[k]=total[k]+count[j]
        print total[k]
    k+=1

print total
