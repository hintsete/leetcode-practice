# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        if not root.left and not root.right:
            # stack.append(str(root.val))
            return [str(root.val)]
     
        left=self.binaryTreePaths(root.left)
        right= self.binaryTreePaths(root.right)

        paths=[]
        for path in left:
            paths.append(str(root.val)+"->"+path)

        for path in right:
            paths.append(str(root.val)+"->"+path)
        return paths

        
            

 
        # stack.append(str(root.val))
     
        # return stack
