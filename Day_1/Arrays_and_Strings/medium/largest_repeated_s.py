"""
Problem statement
You are given a string 'str' of length 'N'. You can perform at most 'k' operations on this string.
 In one operation, you can choose any character of the string and change it to any 
 other uppercase English alphabet character.
Return the length of the longest substring containing same characters after performing
 the above operations.

For example :

Input:
str="AABC"  k=1
"""

def longestSubstringWithSameChars(str, k):
    left = 0
    max_length = 0
    max_count = 0
    freq = {}

    for right in range(len(str)):
        char = str[right]
        freq[char] = freq.get(char, 0) + 1
        max_count = max(max_count, freq[char])

        while (right - left + 1) - max_count > k:
            freq[str[left]] -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage
str = "ABCCAA"
k = 2
print(longestSubstringWithSameChars(str, k))  # Output should be: 3




