# Definition for a binary tree node.
#用递归写这段代码确实比较蠢
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        res=[]
        self.recursionInorderTraversal(root,res)
        return res

    def recursionInorderTraversal(self, x ,res):
        if x!=None:
            self.recursionInorderTraversal(x.left,res)
            res.append(x.val)
            self.recursionInorderTraversal(x.right,res)
            return res
        else:
            return