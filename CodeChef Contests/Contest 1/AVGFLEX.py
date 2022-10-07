# cook your dish here
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    count=0
    for i in range(n):
        len_less=n-(arr[::-1].index(arr[i]))
        if(len_less>n-len_less):
            count+=1
    print(count)