# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def addNode(self,x):
        l=ListNode(x)
        tmp=self
        while tmp.next!=None:
            tmp=tmp.next
        tmp.next=l

    def printNode(self):
        tmp=self
        res=[]
        while tmp.next!=None:
            res.append(tmp.val)
            tmp=tmp.next
        res.append(tmp.val)
        print(res)

class Solution:
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        c=head.next
        p=c.next
        head.next=None
        while c.next!=None:
            c.next=head
            head=ListNode(c.val,c.next)
            c=ListNode(p.val,p.next)
            p=p.next
        c.next=head
        return c


def main():
    l=ListNode(1)
    l.addNode(1)
    l.addNode(2)
    l.addNode(2)
    l.addNode(3)
    l.addNode(3)
    l.printNode()
    s=Solution
    s.reverseList(s,l).printNode()

main()