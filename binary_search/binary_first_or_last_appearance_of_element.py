def binar_first_element(arr,low,high,x):
    result=-1
    while high>= low :
        mid = low+(high-low)//2
        if arr[mid] == x:
            result=mid
            #if i wanna the last apaerance uncomment the next line 
            # low=mid+1
            high=mid-1
        elif arr[mid]< x:
            low = mid+1 
        else:
            high = mid-1           
    return result

arr = [2,3,4,5,5,5,6,78,99,99,99,121,133]

result = binar_first_element(arr,0,len(arr)-1,99)
print(result)