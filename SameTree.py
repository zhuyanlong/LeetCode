# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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

#这种框架几乎是最好的，因为你不用去分开再判断左节点和右节点，只要判断现在遍历的节点即可
class Solution:
    def isSameTree(self, p, q):
        if p==None and q==None:
            return True
        elif p and q and p.val==q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return False


def main():
    t=BTree()
    t.treeInsert(1)
    t.treeInsert(2)
    t.treeInsert(3)
    t.treeInsert(4)
    t.treeInsert(5)

    l=BTree()
    l.treeInsert(1)
    l.treeInsert(2)
    l.treeInsert(3)
    l.treeInsert(4)
    l.treeInsert(5)
    s=Solution
    print(s.isSameTree(s,t.root,l.root))

main()