# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxDiff=0
        def dfs(node,curr_min,curr_max):
            nonlocal maxDiff
            if not node:
                return 0
            dfs_min=abs(node.val-curr_min)
            dfs_max=abs(node.val-curr_max)
            maxDiff=max(maxDiff,dfs_min,dfs_max)
            curr_min=min(curr_min,node.val)
            curr_max=max(curr_max,node.val)
            dfs(node.left,curr_min,curr_max)
            dfs(node.right,curr_min,curr_max)
        dfs(root,root.val,root.val)
        return maxDiff
        
            
            
        
        # def findmin(node):
        #     while node and  node.left:
        #         node=node.left
        #     return node
        # def findmax(node):
        #     while node and node.right:
        #         node=node.right
        #     return node
        # if not root:
        #     return 0
        # if not root.left and not root.right:
        #     return root.val
        # elif not root.left and root.right:
        #     return abs(root.val-root.right.val)
        # elif not root.right and root.left:
        #     return abs(root.val-root.left.val)
        
       

        # else:
        #     return max(abs(root.val-findmin(root.left).val),abs(root.val-findmax(root.right).val),abs(root.val-findmin(root.right).val),abs(root.val-findmax(root.left).val))
            