class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows=len(mat)
        cols=len(mat[0])
        diagonal=[[] for _ in range(rows+cols-1)]
        for i in range(rows):
            for j in range(cols):
                diagonal[i+j].append(mat[i][j])
            
        ans=[]
        for idx in range(len(diagonal)):
            if idx%2==0:
                ans.extend(diagonal[idx][::-1])

            else:
                ans.extend(diagonal[idx])
        return ans
        