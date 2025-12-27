class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        my_dict=defaultdict(int)
        for i in range(len(nums)):
            if my_dict[nums[i]]<2:
                my_dict[nums[i]]+=1
            else:
                nums[i]=float(inf)
        for key,val in my_dict.items():
            k+=val
        print(k)
        print(nums)
        # print(my_dict)
        nums.sort()
        return len(nums[:k])

           
            # if nums[i] in my_dict and my_dict[nums[i]]<2:
            #     print(nums[i])
            #     my_dict[nums[i]]+=1
            #     print(my_dict[nums[i]])
            # elif nums[i] in my_dict and my_dict[nums[i]]==2:
            #     print(nums[i])
            #     # nums[i]=float(inf)
        # print(nums)
        # count=Counter(nums)
        # k=0

        # for i in range(len(nums)):
        #     if count[nums[i]]>2:
        #         count[nums[i]]-=1
        # print(count)
        # for key,val in count.items():
        #     k+=val
        # print(k)
            
        # print(nums)
        # nums.sort()
        # # return len()
        