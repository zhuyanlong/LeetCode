# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root):
        if root==None:
            return 0
        stack=[(root,1)]
        res=float("inf")
        while stack:
            tmp=stack.pop()
            if tmp[0].left:
                stack.append((tmp[0].left,tmp[1]+1))
            if tmp[0].right:
                stack.append((tmp[0].right,tmp[1]+1))
            if (not tmp[0].left) and (not tmp[0].right):
                if res>tmp[1]:
                    res=tmp[1]
        return res

def main():
    t=TreeNode(1)
    t.left=TreeNode(2)
    t.right=TreeNode(3)
    t.left.left=TreeNode(4)
    t.right.right=TreeNode(5)
    s=Solution()
    print(s.minDepth(t))

main()