def peak(arr):
    n=len(arr)
    for i in range(1,n-1):
        if arr[i-1]<arr[i] and arr[i+1]<arr[i]:
                return i
        
print(peak([1,1,1,1,3]))