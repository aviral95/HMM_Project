def fib(n):
    a=0
    b=1
    if n==0:
        return a
    if n==1:
        return b
    
    for i in range(1,n):
        t=a
        a=b
        b=a+t
    return b


k=0
x=0
while x==0:
    x=fib(k)
    k+=1
    for i in range(1,1000):
        x=x/10
        if x==0:
            break
print k-1
        
    

        
            
        
    
    
    

                
        
    
    
