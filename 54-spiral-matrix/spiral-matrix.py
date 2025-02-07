class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output=[]
        left=0
        right=len(matrix[0])-1
        top=0
        bottom=len(matrix)-1
        while left<=right and bottom>=top:
            for col in range(left,right+1):
                output.append(matrix[top][col])
            top+=1
                    
            for row in range(top,bottom+1):
                output.append(matrix[row][right])
            right-=1
            if left>right or top>bottom:
                break
            for col in range(right,left-1,-1):
                output.append(matrix[bottom][col])
            bottom-=1
            for row in range(bottom,top-1,-1):
                output.append(matrix[row][left])
            left+=1
        return output










        return output
        