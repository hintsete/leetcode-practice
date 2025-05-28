class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car=sorted(zip(position,speed), reverse=True)
        
        

        # # n=len(position)
        # # for i in range(n):
        # #     my_dict[position[i]]=speed[i]
        stack=[]
        
        for key,val in car:
            time=(target-key)/val
            if not stack or stack[-1]<time:
                stack.append(time)



        return len(stack)

        


        