# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        _list = []
        if not root:
            return []
        while queue:
            list_elements = []
            for _ in range(len(queue)):
                node = queue.popleft()
                list_elements.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            _list.append(list_elements)
        return _list

           

        