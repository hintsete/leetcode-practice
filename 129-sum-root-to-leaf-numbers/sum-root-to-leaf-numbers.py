# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue=deque()
        queue.append([root,str(root.val)])
        total=0

        while queue:
            # curr_val=""
            for _ in range(len(queue)):
                node,curr_val=queue.popleft()
                if not node.left and not node.right:
                    total+=int(curr_val)
                if node.left:
                    queue.append([node.left,curr_val+str(node.left.val)])
                if node.right:
                    queue.append([node.right,curr_val+str(node.right.val)])
                # node=queue.popleft()
                # curr_val+=str(node.val)
                # print(curr_val)
                # if node.left:
                #     queue.append(node.left)
                # if node.right:
                #     queue.append(node.right)
                # if not node.left and not node.right:
                #     print(curr_val)
                #     curr_val+=str(node)
                #     ans.append(int(curr_val))
                #     curr_val=""
        return total

            

        