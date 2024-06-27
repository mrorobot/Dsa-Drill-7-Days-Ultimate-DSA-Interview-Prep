def largest_np_substring(s):
    li=[]
    count=0
    max_count=0
    for char in s:
        count=0
        
        if char in li:
            st=True
            while st:
                count+=1

                li.pop()
                if len(li)==0:
                    li.append(char)
                    
                    st=False
        
        else:
            li.append(char)
            
        if count>max_count:
            max_count=count
            

    return max_count
        
print(largest_np_substring('abcdabcdefefgefghghghi'))