# Definition for a binary tree node.
# Definition for a binary tree node.
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
    def BFS(self,root):
        res=[]
        queue=[root]
        if root!=None:
            res.append(root.val)
        while queue:
            tmp=queue[0]
            del queue[0]
            if tmp.left!=None:
                queue.append(tmp.left)
                res.append(queue[-1].val)
            else:
                res.append(None)
            if tmp.right!=None:
                queue.append(tmp.right)
                res.append(queue[-1].val)
            else:
                res.append(None)
        print(res)

#这题的思路比较简单，在queue里再添加一位用来表示现在所处的层次
class Solution:
    def levelOrder(self, root):
        res=[]
        queue=[(root,0)]
        if root==None:
            return []
        res.append([root.val])
        while queue:
            tmp=queue[0]
            del queue[0]
            if tmp[0].left!=None:
                queue.append((tmp[0].left,tmp[1]+1))
                if len(res)<=tmp[1]+1:
                    res.append([queue[-1][0].val])
                else:
                    res[tmp[1]+1].append(queue[-1][0].val)
            # print(res)
            # print(tmp)
            if tmp[0].right!=None:
                queue.append((tmp[0].right,tmp[1]+1))
                if len(res)<=tmp[1]+1:
                    res.append([queue[-1][0].val])
                else:
                    res[tmp[1]+1].append(queue[-1][0].val)
        print(res)
        return res

def main():
    t=BTree()
    t.treeInsert(1)
    t.treeInsert(2)
    t.treeInsert(3)
    t.treeInsert(4)
    t.treeInsert(5)
    s=Solution()
    s.levelOrder(t.root)

main()