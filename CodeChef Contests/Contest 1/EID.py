# cook your dish here
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    min_diff=arr[1]-arr[0]
    for i in range(1,n-1):
        if arr[i+1]-arr[i]<min_diff:
            min_diff=arr[i+1]-arr[i]
    print(min_diff)
        