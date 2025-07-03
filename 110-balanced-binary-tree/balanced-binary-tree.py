# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 
        def helper(node):
            if not node:
                return 0

            return 1+max(helper(node.left), helper(node.right))

        left_height=helper(root.left)
        right_height=helper(root.right)

        return abs(left_height-right_height) <=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        