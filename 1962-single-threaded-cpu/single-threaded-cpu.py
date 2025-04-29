class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for idx,task in enumerate(tasks):
            task.append(idx)
        
        tasks.sort(key=lambda x:x[0])
        time=tasks[0][0]
        i=0
        min_heap=[]
        ans=[]
        while min_heap or i<len(tasks):
            while i<len(tasks) and time>=tasks[i][0]:
                heapq.heappush(min_heap,[tasks[i][1],tasks[i][2]])
                i+=1
            if not min_heap:
                time=tasks[i][0]
            else:
                p_time,idx=heapq.heappop(min_heap)
                time+=p_time
                ans.append(idx)
            
        return ans 

            
    
        



















        # thread={}
        # for idx,val in enumerate(tasks):
        #     thread[val[1]]= idx
        # print(thread)
        # min_heap=[]
        # for key in thread:
        #     min_heap.append(key)
        # print(min_heap)
        # heapq.heapify(min_heap)
        # ans=[]
        # while min_heap:
        #     x=heapq.heappop(min_heap)
        #     y=heapq.heappop(min_heap)
        #     if x==y:
        #         ans.append(min(thread[x],thread[y]))
        #     else:
        #         ans.append(heapq.heappop(min_heap))
        # return ans
    
        