# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minValueNode(self,node):
        while node.left is not None:
            node=node.left
        return node
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if key<root.val:
            root.left=self.deleteNode(root.left,key)
        elif key>root.val:
            root.right=self.deleteNode(root.right,key)

        else:

            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            temp=self.minValueNode(root.right)
            root.val=temp.val
            root.right=self.deleteNode(root.right,temp.val)
        return root
        
        