# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res=[]
        def inorder(curr):
            if curr:
                inorder(curr.left)
                res.append(curr.val)
                inorder(curr.right)
        inorder(root)

        print(res)
        def build(l,r,res):
            if l>r:
                return None

            mid=(l+r)//2
            node=TreeNode(res[mid])
            node.left=build(l,mid-1,res)
            node.right=build(mid+1,r,res)
            return node

        return build(0,len(res)-1,res)
    

        