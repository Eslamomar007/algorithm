def find_count(arr,x):
    first = find_first(arr,x)
    last =  find_last(arr,x)
    return last-first+1


def find_first(arr,x):
    index = -1
    low =0
    high= len(arr)-1
    while high>=low:
        mid= low+(high-low)//2
        if arr[mid]==x:
            index =  mid
            high = mid-1
        elif arr[mid]>x:
            high = mid-1
        else:
            low =mid+1
            
    return index

def find_last(arr,x):
    index = -1
    low =0
    high= len(arr)-1
    while high>=low:
        mid= low+(high-low)//2
        if arr[mid]==x:
            index =  mid
            low = mid+1
        elif arr[mid]>x:
            high = mid-1
        else:
            low =mid+1
            
    return index


arr = [11,22,33,33,33,44,44,44,44,55,66,66,66,66,66,88]
print(find_count(arr,66))