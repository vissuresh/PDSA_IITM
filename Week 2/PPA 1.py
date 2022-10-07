'''Write a Python function binarySearchIndexAnd Comparisons ( L , k ) that accepts a list L sorted in
ascending order and an integer k and returns a tuple ( True / False , numComparisons ) . The first
part of this tuple will be True if integer k is present in list L , False otherwise . The second part
of the tuple is an integer which gives the number of elements in L that are actually compared to
k while searching k in the list L using binary search .
For consistency use ( left + right ) // 2 to calculate the middle index . '''

def binarySearchIndexAndComparisons(l,k):
    (left,right,count)=(0,len(l)-1,0)
    while left<=right:
        count+=1
        mid=(left+right)//2
        if l[mid]==k:
            return (True,count)
        elif k < l[mid]:
            right = mid-1
        else:
            left = mid+1
    return (False,count)