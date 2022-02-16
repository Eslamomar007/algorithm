def binary_search(arr,start,end,x):  
    mid = start+ (end-start)//2
    if end <= start:
        return-1

    elif x==arr[mid]:
        return mid 
    elif x >arr[mid]:
        start = mid+1
        return binary_search(arr[start:],0,len(arr[start:])-1,x)
    else:
        end = mid-1
        return    binary_search(arr[start:end],start,len(arr[start:end])-1,x)


arr = [2,3,4,5,6,78,99,121,133]

result = binary_search(arr,0,len(arr)-1,121)
print(result)