class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        output=[]
        for i in range(len(matrix[0])):
            arr=[]
            for j in range(len(matrix)):
                arr.append(matrix[j][i])
            output.append(arr)
        return output
        #     new_arr=[arr[j] for j in range(len(matrix))]
        #     output.append(new_arr)

        # return output
        # matrix=list(zip(*matrix))
        # return matrix
     