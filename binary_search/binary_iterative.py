def binary_search(arr,start,end,x):
    
    while end>=start:
        mid = start+(end-start)//2
        if x==arr[mid]:
            return mid 
        elif x >arr[mid]:
            start = mid+1
        else:
            end = mid-1
    return -1

arr = [2,3,4,5,6,78,99,121,133]

result = binary_search(arr,0,len(arr),133)
print(result)