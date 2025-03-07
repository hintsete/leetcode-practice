class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for astero in asteroids:
            while stack and stack[-1]>0 and astero<0:
                left=stack.pop()
                
                if abs(left)>abs(astero):
                    stack.append(left)
                    break
                elif abs(left)==abs(astero):
                    break
            else:
                stack.append(astero)
                
        return stack

            
            
        