class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        count={}
        for win, lose in matches:
            if win not in count:
                count[win]=0
            if lose not in count:
                count[lose]=1

            else:
                count[lose]+=1
        
        winner=[]
        loser=[]
        for key, value in count.items():

            if value==0:
                winner.append(key)
            elif value==1:
                loser.append(key)
            
           
        answer = [sorted(winner),sorted(loser)]
        return answer
       
