class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # matrix=list(zip(*matrix))
        # print(matrix)
        # for i in range(len(matrix)):
        #     matrix[i]=matrix[i][::-1]
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for row in matrix:
            row[:]=row[::-1]
        
    
        