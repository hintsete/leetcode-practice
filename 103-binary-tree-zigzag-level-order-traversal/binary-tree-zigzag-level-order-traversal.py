# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=deque([root])
        level=0
        ans=[]
        while queue:
            level_node=[]
            for i in range(len(queue)):
                node=queue.popleft()
                level_node.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level%2!=0:
                level_node=level_node[::-1]
            ans.append(level_node)
                
            level+=1
        return ans
