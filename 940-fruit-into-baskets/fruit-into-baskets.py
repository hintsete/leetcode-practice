class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        my_fruit=defaultdict(int)
        left=0
        total=0
        res=0
        for right in range(len(fruits)):
            my_fruit[fruits[right]]+=1
            total+=1
            while len(my_fruit)>2:
                my_fruit[fruits[left]]-=1
                total-=1
                if my_fruit[fruits[left]]==0:
                    del my_fruit[fruits[left]] 
                left+=1
            res=max(res,total)
        return res
