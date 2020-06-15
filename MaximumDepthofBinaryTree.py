# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        if root==None:
            return 0
        else:
            leftnode=self.maxDepth(self,root.left)
            rightnode=self.maxDepth(self,root.right)
        return max(leftnode+1,rightnode+1)

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

def main():
    t=BTree()
    
    t.treeInsert(1)
    t.treeInsert(2)
    t.treeInsert(3)
    t.treeInsert(4)
    t.treeInsert(5)
    t.inorderTravel(t.root)
    s=Solution
    print(s.maxDepth(s,t.root))

main()