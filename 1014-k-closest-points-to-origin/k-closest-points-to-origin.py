class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist=[]
        for i in range(len(points)):
            x=points[i][0]
            y=points[i][1]
            dist.append([x**2+y**2, i])
        print(dist)
        heapq.heapify(dist)
        print(dist)
        ans=[]
        for i in range(k):
            temp=heapq.heappop(dist)
            idx=temp[1]
            print(temp)
            print(idx)
            ans.append(points[idx])

        return ans


        