def find_Min_Difference(L,P):
    import sys
    res=[[]]
    for i in L:
        for j in range(len(res)):
            if(len(res[j])!=P):
                res.append(res[j]+[i])

    j=0
    while(j<len(res)):
        if(len(res[j])!=P):
            res.pop(j)
        else:
            j+=1
    
    diff=sys.maxsize
    
    for j in range(len(res)):
        res[j].sort()
        if(res[j][-1]-res[j][0]<diff):
            diff=res[j][-1]-res[j][0]
            
    return diff

L=eval(input().strip())
P=int(input())
print(find_Min_Difference(L,P))
