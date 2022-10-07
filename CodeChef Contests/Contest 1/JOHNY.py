# cook your dish here
def bsearch(arr,low,high,key):
    if(low>high):
        return None
    mid=(low+high)//2
    
    if arr[mid]==key:
        return mid
    
    elif key<arr[mid]:
        return bsearch(arr,low,mid-1,key)
    
    else:
        return bsearch(arr,mid+1,high,key)
        
for i  in range(int(input())):
    n=int(input())
    play=list(map(int,input().split()))
    k=int(input())-1
    song=play[k]
    play.sort()
    print(bsearch(play,0,n-1,song)+1)
    
    
