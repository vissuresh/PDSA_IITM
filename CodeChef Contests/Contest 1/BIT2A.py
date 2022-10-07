# cook your dish here
for _ in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    for i in range(n):
        count=0
        for j in range(n):
            if A[j]>A[i]:
                count+=1
        print(count,end=' ')
    print()