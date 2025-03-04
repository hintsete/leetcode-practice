class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        diff=0
        start_idx=0
        for i in range(len(gas)):
            diff+=gas[i]-cost[i]
            if diff<0:
                start_idx=i+1
                diff=0
        return start_idx
        # pair=list(zip(cost,gas))
        # pair.sort()
        # sorted_gas=[g for _,g in pair]
        # costs=[c for c,_ in pair]
        # print(sorted_gas)
        # print(costs)
        # sorted_gas=list(accumulate(sorted_gas))
        # costs=[0]+list(accumulate(costs))
        # print(sorted_gas)
        # print(costs)
        # i=0
        # while i<len(gas):
        #     if sorted_gas[i]-costs[i]<gas[i]:
        #         return -1
        #         break
        #     i+=1
        # return gas.index(sorted_gas[0])


        
        