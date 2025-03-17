# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def findMax(node):
            if not node:
                return 0
            left=1+findMax(node.left)
            right=1+findMax(node.right)
            return max(left,right)
        return findMax(root)

        # res=0
        # def count(curr):
        #     if curr.val==null:
        #         res+=1
        #     else:
                
        # return res+1
        
       