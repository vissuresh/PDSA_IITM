from sys import maxsize

def find_Min_Difference(L, P):
    L.sort()
    diff = maxsize
    for i in range(len(L) - P + 1):
        diff = min(diff, L[i + P - 1]-L[i])
    return diff 
L=eval(input().strip())
P=int(input())
print(find_Min_Difference(L,P))
