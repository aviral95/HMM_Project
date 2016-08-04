def tri(n):
    return n*(n+1)/2
n=10000

while True:
    count=2
    y=tri(n)
    for x in range(2,int(y**0.5)+1):        
        if y%x==0:
            count+=2
    if count>=500:
        break
    print count
    n+=1
print tri(n)
