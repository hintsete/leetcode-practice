class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        output=[]
        for i in range(len(img)):
            output.append([0]*len(img[0]))
        for i in range(len(img)):
            for j in range(len(img[0])):
                possible_idx=[[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]]
                count=0
                total=0
                for elem in possible_idx:
                    if 0<=elem[0]<len(img) and 0<=elem[1]<len(img[0]):
                        total+=img[elem[0]][elem[1]]
                        count+=1

                if count>0:
                    total=total//count
                output[i][j]=total
        return output
                       













        

        