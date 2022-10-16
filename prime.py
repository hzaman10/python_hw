def myPrime(x):
    k=0
    i=2

    while (k==0 and i<x):
        if (x%i==0):
            k=1
        #print (x,' : ',i,' : ',x%i)
        i+=1
    return k        

     
y=int(input('Enter a value for y : '))
p=myPrime(y)
if (p==1):
    print(y,' is not a prime number.')
else:
    print(y, ' is a prime number.')
