import re

def operate(prot):
    global cores
    caps=re.findall("[A-Z]+",prot)
    temp=[]
    for i in caps:
        st=i
        for j in cores:
            if (j in i):
                st=st.replace(j,'$'*len(j)) #$ indicates core
        temp+=[st]
    nc=reduce(lambda i,j:i+j,temp)
    final=''
    for i in nc:
        if i=='$':
            final+='C'
        else: final+='N'
    return final

def count(string):
    global ci,ni,c2c,n2n,c2n,n2c
    if string[0]=='C':
        cur='C'
        ci+=1
    if string[0]=='N':
        cur='N'
        ni+=1

    for i in range(1,len(string)):
        if string[i]==cur=='C':
            c2c+=1
            cur=string[i]
        if string[i]==cur=='N':
            n2n+=1
            cur=string[i]
        if cur=='C' and string[i]=='N':
            c2n+=1
            cur=string[i]
        if cur=='N' and string[i]=='C':
            n2c+=1
            cur=string[i]
        



fp=open("c:/Users/sony vaio/Desktop/proteins.txt",'r')
fc=open("c:/Users/sony vaio/Desktop/core.txt",'r')
cores=fc.readlines()
cores=[i.rstrip() for i in cores]
cores.sort(key=len,reverse=True)

fpw=open("c:/Users/sony vaio/Desktop/proteins_new.txt","w")

protein=''
n2c=0
c2n=0
n2n=0
c2c=0
ci=0
ni=0
for i in fp.readlines():
    if i[0]=='>':
        #print protein
        try:
            x=operate(protein)

        #### To get the proteins containing cores.
            
           #if 'C' in x:
           #    print protein
           #    print x
            count(x)
        except:
            pass
        protein=''
        continue
    protein+=i.rstrip()

print 'starting prob of c = ',float(ci)/(ci+ni)
print 'starting prob of n = ',float(ni)/(ci+ni)
print 'transition prob c to n = ', float(c2n)/(c2c+c2n)
print 'transition prob n to c = ', float(n2c)/(n2n+n2c)
print 'transition prob n to n = ', float(n2n)/(n2n+n2c)
print 'transition prob c to c = ', float(c2c)/(c2c+c2n)
