# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
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

#这道题这样写时间复杂度有些高，应该是O(n)
#应该去想一些时间复杂度更低的算法
class Solution:
    def partition(self, head, x):
        head1=ListNode(0)
        head2=ListNode(0)
        phead1=head1
        phead2=head2
        tmp=head
        while tmp!=None:
            if tmp.val<x:
                phead1.next=tmp
                tmp=tmp.next
                phead1=phead1.next
                phead1.next=None
            else:
                phead2.next=tmp
                tmp=tmp.next
                phead2=phead2.next
                phead2.next=None
        phead1.next=head2.next
        return head1.next

def main():
    l=ListNode(1)
    l.addNode(4)
    l.addNode(3)
    l.addNode(2)
    l.addNode(5)
    l.addNode(2)
    l.printNode()
    x=3
    s=Solution
    s.partition(None,l,x).printNode()

main()