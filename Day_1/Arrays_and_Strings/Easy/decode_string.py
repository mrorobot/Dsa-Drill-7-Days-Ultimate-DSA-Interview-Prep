'''
Problem statement
You have been given an encoded string. Your task is to decode it back to the original string.

- An encoded string will be of the form <count>[encoded_string], where the 'encoded_string' inside the square brackets is being repeated exactly 'count' times. Note that 'count' is guaranteed to be a positive integer and can be greater than 9.
- There are no extra white spaces and square brackets are well-formed.
For example -
Input: 2[a]
“a” is encoded 2 times, hence the decoded string will be "aa".
'''
#Easy way using stack:
def decodeString(s: str) -> str:
    stack = []
    for char in s:
        if char != ']':
            stack.append(char)
        else:
            # Get the encoded string inside the brackets
            encoded_string = ''
            while stack and stack[-1] != '[':
                encoded_string = stack.pop() + encoded_string
            stack.pop()  # pop the '['
            
            # Get the count
            count = ''
            while stack and stack[-1].isdigit():
                count = stack.pop() + count
            stack.append(int(count) * encoded_string)
    
    return ''.join(stack)
''''
Easy Solution:

Uses a stack to keep track of characters and encoded segments.
When a closing bracket ] is encountered, it pops the stack to retrieve the encoded string and the count, then repeats the encoded string the required number of times.
Finally, it reconstructs the decoded string from the stack.'''

#Efficient solution using recursion

def decodeString(s: str) -> str:
    def helper(index: int) -> (str, int):
        decoded_string = ""
        while index < len(s) and s[index] != ']':
            if not s[index].isdigit():
                decoded_string += s[index]
                index += 1
            else:
                count = 0
                while index < len(s) and s[index].isdigit():
                    count = count * 10 + int(s[index])
                    index += 1
                index += 1  # skip the '['
                decoded_segment, index = helper(index)
                index += 1  # skip the ']'
                decoded_string += decoded_segment * count
        return decoded_string, index

    decoded_result, _ = helper(0)
    return decoded_result
''''
Efficient Solution:

Uses a recursive helper function to decode segments of the string.
Handles nested encoded strings more naturally and efficiently by leveraging recursion.
The helper function processes characters until it encounters a closing bracket, then repeats the encoded segment as needed.
        



'''