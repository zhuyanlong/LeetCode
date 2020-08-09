# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        self.dfs(root)
        return root
    def dfs(self,root):
        if root.left==None and root.right==None:
            return
        root.left,root.right=root.right,root.left
        self.dfs(root.left)
        self.dfs(root.right)

def main()