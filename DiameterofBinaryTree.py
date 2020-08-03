# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#这道题还是一个设计递归的问题
class Solution:
    res=0
    def diameterOfBinaryTree(self, root):
        
        self.maxdepth(root)
        return self.res

    def maxdepth(self,root):
        if root==None:
            return 0
        left=self.maxdepth(root.left)
        right=self.maxdepth(root.right)
        self.res=max(self.res,left+right)
        return max(left,right)+1

def main():
    l=TreeNode(val=1)
    l.left=TreeNode(val=2)
    # l.left.left=TreeNode(val=3)
    l.right=TreeNode(val=4)
    l.right.right=TreeNode(val=5)
    l.right.right.left=TreeNode(val=6)
    s=Solution()
    print(s.diameterOfBinaryTree(l))

main()