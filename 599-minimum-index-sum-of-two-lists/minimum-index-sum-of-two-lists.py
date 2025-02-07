class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # dict1={val:index for index, val in enumerate(list1)}
        # dict2={val:index for index,val in enumerate(list2)}
        # idx_sum=[]
        # res=[]
        # for key in dict1.keys():
        #     if key in dict2:
        #         # idx_sum.append([dict1[key]+dict2[key],key])
        #         # if dict1[key]+dict2[key] < idx_sum:
        #         #     idx_sum=dict1[key]+dict2[key]
        #         idx_sum.append((dict1[key]+dict2[key],key))
        # print(idx_sum)    
        # _min=min(idx_sum)
        # print(_min)
        # # for key in dict1.keys():
        # #     if key in dict2:        
        # #         res.append(list2[idx_sum])
        # # if list1[_min] in dict2 and list2[_min] in dict1:
        # #     res.append(list1[_min])
        
        # return res
            
        n=len(list1)
        m=len(list2)
        min_index=2000
        res=[]
        for i in range(n):
            for j in range(m):
                if list1[i]==list2[j]:
                    least=i+j
                    if least< min_index:
                        res=[list1[i]]
                        min_index=min(least,min_index)
                    elif least==min_index:
                        res.append(list1[i])
        return res

        