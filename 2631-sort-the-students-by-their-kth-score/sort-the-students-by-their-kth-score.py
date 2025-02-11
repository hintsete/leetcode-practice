class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(score)):
            for j in range(i+1,len(score)):
                if score[i][k]<score[j][k]:
                    score[i],score[j]=score[j],score[i]
        return score
        # i=0
        # while i+1<len(score):
        #     if score[i][k]<score[i+1][k]:
        #         score[i],score[i+1]=score[i+1],score[i]
        #     i+=1
            
        # return score
