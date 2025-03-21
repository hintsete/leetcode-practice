# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans=[]
        queue=deque([root])
        while queue:
            level=len(queue)
            max_val=float("-inf")
            # ans.append(max(queue))
            for _ in range(level):
                node=queue.popleft()
                max_val=max(max_val,node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(max_val)
        return ans
            
        