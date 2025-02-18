class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []

        left=0
        right=0
        res=[]
        while left<len(firstList) and right<len(secondList):
            start1,end1=firstList[left]
            start2,end2=secondList[right]

            if start1<=end2 and start2<=end1:
                res.append([max(start1,start2), min(end1,end2)])
            if end1>end2:
                right+=1
            else:
                left+=1

            # if start1>end2:
            #     right+=1
            # elif start2>end1:
            #     left+=1
            # else:
            #     res.append([max(start1,start2), min(end1,end2)])

            #     if end1>end2:
            #         left+=1
            #     else:
            #         right+=1
        return res
            

        