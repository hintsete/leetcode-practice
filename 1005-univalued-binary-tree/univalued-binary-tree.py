# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        valid = True
        if not root:
            return True
        queue = deque([root])
        while queue:
            node = queue.popleft()
            # if node.left and node.right:
            #     if node.val != node.left.val or node.val != node.right.val:
            #         valid = False
            #         break
            if node.left:
                if node.val != node.left.val:
                    valid =  False
                    break 
                queue.append(node.left)
               
            if node.right:
                if node.val != node.right.val:
                    valid = False
                    break
                queue.append(node.right)
               
        return valid