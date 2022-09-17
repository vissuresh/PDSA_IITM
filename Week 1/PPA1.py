def Twin_Primes(n,m):
    fin=[]
    def isprime(x):
        if x<2:
            return False
        for i in range(2,int(x/2)+1):
            if x%i==0:
                return False
        return True
        
    for ele in range(n,m-1):
        if(isprime(ele) and isprime(ele+2)):
            fin.append((ele,ele+2))
    
    return fin
n=int(input())
m=int(input())
print(sorted(Twin_Primes(n, m)))
