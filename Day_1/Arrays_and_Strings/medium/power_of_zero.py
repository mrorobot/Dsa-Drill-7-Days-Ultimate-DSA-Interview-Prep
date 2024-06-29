def making_zero(matrix):
    n=len(matrix)
    m=len(matrix[0])
    col0=1
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                
                matrix[i][0]=0
                if j!=0:
                    matrix[0][j]=0
                else:
                    col0=0
                
                
             
    for i in range(1,n):
        for j  in range(1,m):
            if matrix[i][j]!=0:
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
    if matrix[0][0]==0:
        for i in range(m):
            matrix[0][i]=0

    if col0==0:
        for j in range(n):
            matrix[j][0]=0
    
    
        
    return matrix
   
arr=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(making_zero(arr))
            
        