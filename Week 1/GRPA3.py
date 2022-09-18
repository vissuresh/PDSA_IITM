def odd_one(L):
    d={}
    d[type(L[0])]=1
    for i in range(1,len(L)):
        if type(L[i]) not in d:
            d[type(L[i])]=1
        else:
            d[type(L[i])]+=1
    for key in d:
        if d[key]==1:
            return str(key)[8:].rstrip("'>")
    
print(odd_one(eval(input().strip())))