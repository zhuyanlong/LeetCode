# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root):
        return self.judgeTree(root)

    def judgeTree(self,root):
        if root==None:
            return True
        left=self.treeHeight(root.left)
        right=self.treeHeight(root.right)
        if abs(left-right)<=1:
            return self.judgeTree(root.left) and self.judgeTree(root.right)
        else:
            return False

    def treeHeight(self, root):
        if root==None:
            return 0
        return max(self.treeHeight(root.left),self.treeHeight(root.right))+1

def main():
    t=TreeNode(1)
    t.left=TreeNode(2)
    t.right=TreeNode(2)
    t.left.left=TreeNode(3)
    t.left.right=TreeNode(3)
    t.left.left.left=TreeNode(4)
    t.left.left.right=TreeNode(5)
    s=Solution()
    print(s.isBalanced(t))

main()