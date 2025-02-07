class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # sudoku=set()
        for row in board:
            num=set()
            for element in row:
                if element!="." and  element in num:
                    return False
                num.add(element)
        for i in range(9):
            num=set()
            for j in range(9):
                if board[j][i]!="." and board[j][i]  in num:
                    return False
                num.add(board[j][i])
            
        for i in range(0,9,3):
            for j in range(0,9,3):
                sudoku=set()
                for row in range(3):
                    
                    for col in range(3):
                        if board[i+row][j+col]!="." and board[i+row][j+col] in sudoku:
                            return False
                        sudoku.add(board[i+row][j+col])
        return True
        

        