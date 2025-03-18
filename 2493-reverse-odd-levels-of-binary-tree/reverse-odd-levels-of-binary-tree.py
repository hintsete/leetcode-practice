# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue=deque([root])
        position=0
        while queue:
            
            if position%2==1:
                left=0
                right=len(queue)-1
                while left<right:
                    queue[left].val,queue[right].val=queue[right].val,queue[left].val
                    left+=1
                    right-=1
        
            for _ in range(len(queue)):
            
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            position+=1
        return root
      
    
        