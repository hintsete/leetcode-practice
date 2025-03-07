class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        total=0
        queue=deque()
        arr.append(0)
        for i in range(len(arr)):
            while queue and arr[i]<arr[queue[-1]]:
                mid=queue.pop()
                left=queue[-1] if queue else -1
                right=i
                count=(mid-left)*(right-mid)
                total+=arr[mid]*count

                
                # queue.popleft()
                
            queue.append(i)
            
        return total%(10**9+7)

        