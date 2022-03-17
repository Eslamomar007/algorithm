def find_number(arr,x):
    low = 0
    n = len(arr)
    high = n-1
    result = -1
    while high >=low:
        mid = low+(high-low)//2
        if arr[mid]==x:
            result = mid
            return result
        elif arr[mid]<arr[high]:
            if arr[mid]<x & arr[high]>x:
                low  = mid+1
            else: 
                high = mid-1
        else:
            if arr[mid]>x & arr[low]<x:
                high = mid-1
            else:
                low = mid+1

    return result


arr = [33,44,55,66,77,88,11,22,25,27]
print(find_number(arr,44))