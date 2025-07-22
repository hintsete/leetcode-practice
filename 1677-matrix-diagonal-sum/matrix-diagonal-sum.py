class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total=0
        n=len(mat)
        for i in range(n):
            for j in range(n):
                if i==j:
                    total+=mat[i][j]

        for i in range(n):
            total+=mat[i][n-1-i]
        # print(total)
        if n%2==0:
            return total

        else:
            return total-mat[n//2][n//2]

        # 1 2 3
        # 4 5 6
        # 7 8 9