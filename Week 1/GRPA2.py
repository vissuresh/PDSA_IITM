'''Goldbach's Conjecture'''

def isprime(x):
        if x<2:
            return False
        for i in range(2,int(x/2)+1):
            if(x%i==0):
                return False
        return True

def Goldbach(n):        
    res=[]
    for i in range(2,int(n/2)+1):
        if(isprime(i) and isprime(n-i)):
          res.append((i,n-i))
    return res
n=int(input())
print(sorted(Goldbach(n)))