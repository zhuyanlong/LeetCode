class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BTree:
    def __init__(self):
        self.root=None
    def treeInsert(self,value):
        #用来定位待插入节点的父节点
        y=None
        x=self.root
        t=TreeNode(value)
        while x!=None:
            y=x
            if t.val<x.val:
                x=x.left
            else:
                x=x.right
        if y==None:
            self.root=t
        else:
            if t.val<y.val:
                y.left=t
            else:
                y.right=t
    def inorderTravel(self,x):
        if x!=None:
            self.inorderTravel(x.left)
            print(x.val)
            self.inorderTravel(x.right)
        else:
            return

    def preorderTravel(self,x):
        if x!=None:
            print(x.val)
            self.preorderTravel(x.left)
            self.preorderTravel(x.right)
        else:
            return
    def postorderTravel(self,x):
        if x!=None:
            self.preorderTravel(x.left)
            self.preorderTravel(x.right)
            print(x.val)
        else:
            return
    def maxDepth(self, root):
        if root==None:
            return 0
        else:
            leftnode=self.maxDepth(self,root.left)
            rightnode=self.maxDepth(self,root.right)
        return max(leftnode+1,rightnode+1)

# class Solution:
#     def isValidBST(self, root):
#         lower=-float('inf')
#         higher=float('inf')
#         return self.dfs(root,lower,higher)
#     def dfs(self,root,lower,higher):
#         if root==None:
#             return True
#         if  root.val<=lower or root.val>=higher:
#             return False
#         return self.dfs(root.left,lower,root.val) and self.dfs(root.right,root.val,higher)

class Solution:
    res=[]
    def isValidBST(self, root):
        self.res=[]
        self.inorderTravel(root)
        for i in range(1,len(self.res)):
            if self.res[i]<=self.res[i-1]:
                return False
        return True

    def inorderTravel(self,x):
        if x!=None:
            self.inorderTravel(x.left)
            self.res.append(x.val)
            self.inorderTravel(x.right)
        else:
            return

def main():
    l=TreeNode(val=10)
    l.left=TreeNode(val=5)
    l.right=TreeNode(val=15)
    # l.left.left=TreeNode(val=3)
    # l.left.left.left=TreeNode(val=3)
    # l.left.left.right=TreeNode(val=2)
    l.right.left=TreeNode(val=6)
    l.right.right=TreeNode(val=20)
    # l.right.right.right=TreeNode(val=1)
    s=Solution()
    print(s.isValidBST(l))

main()
