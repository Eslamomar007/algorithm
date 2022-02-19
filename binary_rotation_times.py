# this code will use binary algorithm to determine how many times did an array rotated
def rotated_times(arr):
    low=0
    high = len(arr)-1
    n = len(arr)
    while high>=low:
        mid = low +(high-low)//2
        prev =(mid+n-1)%n
        next =(mid-1)%n

        if arr[low] < arr[high]: return low        

        elif arr[mid] <prev and arr[mid]<=next: return mid

        elif arr[mid] <=prev: high = mid -1

        elif arr[mid]>=next: low =mid+1

        else: return 0
    
    return -1

arr = [5,6,7,8,9,1,2,3,4]
arr = [66,77,88,33,44,55]
# arr = [22,33,55,88]
print(rotated_times(arr))