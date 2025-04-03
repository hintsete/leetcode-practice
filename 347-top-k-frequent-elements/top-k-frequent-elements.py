class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count=defaultdict(int)
        count=Counter(nums)
        max_val=max(count.values())
        frequency=[[] for _ in range(max_val+1)]
        
        # c is the number of counts used as an index in frequency 2d list and n is the list of values with that number of occurence
        for n,c in count.items():
            frequency[c].append(n)

        print(frequency)

        # now iterate through frequency in reverse order to pop the frequently occured number
        res=[]
        
        for i in range(max_val,0,-1):
            for n in frequency[i]:
                res.append(n)
                while len(res)==k:
                    return res
                
            
   

        
        