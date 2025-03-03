class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points=sorted(points,key=lambda x:x[1])
        # print(points)
        last=points[0][1]
        arrow=1
        for start,end in points[1:]:
            if start>last:
                arrow+=1
                last=end
        return arrow
      
      

        