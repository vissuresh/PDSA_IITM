'''Write a function Find_Min_Difference(L, P) that accepts a list L of integers and P (positive integer) where the size of L 
is greater than P. The task is to pick P different elements from the list L, where the difference between the maximum value 
and the minimum value in selected elements is minimum compared to other differences in possible subset of p elements. The 
function returns this minimum difference value. Note - The list can contain more than one subset of p elements that have the
 same minimum difference value. Example Let L = [3, 4, 1, 9, 56, 7, 9, 12, 13] and P = 5 If we see the following two subsets 
 of 5 elements from L [3, 4, 7, 9, 9] or [7, 9, 9, 12, 13]'''

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
