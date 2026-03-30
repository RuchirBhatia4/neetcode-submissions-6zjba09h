# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l = []
        self.inorder(root, l)
        return l[k-1]
    
    def inorder(self, node: Optional[TreeNode], l: List[int]):
        if not node:
            return
        self.inorder(node.left, l)
        l.append(node.val)
        self.inorder(node.right, l)