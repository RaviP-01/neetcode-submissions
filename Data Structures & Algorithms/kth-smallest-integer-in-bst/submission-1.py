# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        result = 0
        def inorder(root):
            nonlocal counter, result
            if not root:
                return
            if counter >= k:
                return

            inorder(root.left)
            counter += 1
            if counter == k:
                result = root.val
            inorder(root.right)
        inorder(root)
        return result
            

            

        