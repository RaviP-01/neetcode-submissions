# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        # Recursive
        # if val > root.val:
        #     root.right = self.insertIntoBST(root.right, val)
        # elif val < root.val:
        #     root.left = self.insertIntoBST(root.left, val)
        # return root

        # iterative
        temp = root
        while True:
            if val > temp.val:
                if not temp.right:
                    temp.right = TreeNode(val)
                    return root
                temp = temp.right
            else:
                if not temp.left:
                    temp.left = TreeNode(val)
                    return root
                temp = temp.left