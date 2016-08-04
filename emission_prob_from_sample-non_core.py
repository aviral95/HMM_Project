fp=open("c:/Users/sony vaio/Desktop/proteins.txt",'r')
import collections

protein=''
for i in fp.readlines()[0:200]:
    if i[0]!='>':
        protein+=i.rstrip()
    protein=''.join([c for c in protein if c.isupper()])

#print protein

aa='A C D E F G H I K L M N P Q R S T V W Y'
aa=aa.split()


count=collections.Counter(protein)
sum=sum(count.values())

for i in aa:
    count[i]=float(count[i])/sum

print count

