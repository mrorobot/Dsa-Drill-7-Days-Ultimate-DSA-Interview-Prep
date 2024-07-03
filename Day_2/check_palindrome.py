def isPalindrome(string: str) -> bool:
    if len(string)==1 or len(string)==2:
        return True
    
    else:
        length=len(string)
        if length%2==0:
            first=string[0:length//2]
            second=string[:length//2-1:-1]
            print(first, second)
            if first==second:
                return True
            else:
                False
        else:
            first=string[0:length//2+1]
            second=string[:length//2-1:-1]
            print(first, second)
            if first==second:
                return True
            else:
                False


print(isPalindrome("sucuhhucus"))

#Populer way 

def isPalindrome(string: str) -> bool:
    length = len(string)
    
    # Edge case: Single character or empty string is a palindrome
    if length <= 1:
        return True

    left = 0
    right = length - 1

    # Compare characters from both ends
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    
    return True

