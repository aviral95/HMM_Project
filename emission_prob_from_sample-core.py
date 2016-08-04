fc=open("c:/Users/sony vaio/Desktop/core.txt",'r')
cores=fc.readlines()
cores=[i.rstrip() for i in cores]
import collections

cores=''.join(cores)
#print cores

aa='A C D E F G H I K L M N P Q R S T V W Y'
aa=aa.split()
print aa

count=collections.Counter(cores)

sum=sum(count.values())
print sum

for i in aa:
    count[i]=float(count[i])/sum

print count
