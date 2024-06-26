'''
Problem Statement
You are given a string str of length N. 
Your task is to reverse the original string word by word. 
There can be multiple spaces between words and leading or trailing spaces,
 but the output should have a single space between words with no leading or trailing spaces.'''

#Easy solution :
def reverseString(s: str) -> str:
    # Split the string by spaces into a list of words
    words = s.split()
    
    # Reverse the list of words
    reversed_words = words[::-1]
    
    # Join the reversed list of words with a single space
    reversed_string = ' '.join(reversed_words)
    
    return reversed_string

#Efficient solution:
""""
This solution avoids using too many built-in functions and focuses on manually processing
the string for better control and potential efficiency improvements."""
def reverseString(s: str) -> str:
    # Initialize variables
    length = len(s)
    words = []
    i = 0

    # Traverse the string to extract words
    while i < length:
        if s[i] != ' ':
            start = i
            while i < length and s[i] != ' ':
                i += 1
            words.append(s[start:i])
        i += 1
    
    # Reverse the list of words
    words.reverse()
    
    # Join the reversed list of words with a single space
    reversed_string = ' '.join(words)
    
    return reversed_string

