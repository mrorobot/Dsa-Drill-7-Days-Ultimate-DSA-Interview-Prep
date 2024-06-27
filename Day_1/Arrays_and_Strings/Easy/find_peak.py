"""
You are given an array 'arr' of length 'n'. 
Find the index(0-based) of a peak element in the array.
 If there are multiple peak numbers, return the index of any peak number.
Peak element is defined as that element that is greater than both of its neighbors.
If 'arr[i]' is the peak element, 'arr[i - 1]' < 'arr[i]' and 'arr[i + 1]' < 'arr[i]'
"""
def findPeakElement(arr: [int]) -> int:
    n = len(arr)
    if n == 1:
        return 0  # The only element is a peak
    if arr[0] > arr[1]:
        return 0  # The first element is a peak
    if arr[n-1] > arr[n-2]:
        return n-1  # The last element is a peak
    
    # Check for peaks in the middle of the array
    for i in range(1, n-1):
        if arr[i-1] < arr[i] and arr[i+1] < arr[i]:
            return i
    
    return -1  # This should not happen if the array has at least one peak

# Example usage:
arr = [1, 2, 3, 1]
print(findPeakElement(arr))  # Output: 2

"""
Efficient approach"""
def findPeakElement(arr: [int]) -> int:
    n = len(arr)
    left, right = 0, n - 1

    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            # We are in the decreasing part of the array
            # So the peak is in the left part (including mid)
            right = mid
        else:
            # We are in the increasing part of the array
            # So the peak is in the right part (excluding mid)
            left = mid + 1

    # Left and right will converge to the peak element
    return left
