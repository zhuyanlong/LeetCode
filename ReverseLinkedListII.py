# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#最简单好理解的一种做法
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def addNode(self,val):
        l=ListNode(val)
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
    def reverseBetween(self, head, m, n):
        if head==None or head.next==None:
            return head
        if m==n:
            return head
        i=1
        first=head
        par=ListNode()
        par.next=head
        while i!=m:
            first=first.next
            par=par.next
            i+=1
        j=0
        last=head
        while j!=n:
            last=last.next
            j+=1
        c=first.next
        p=c.next
        first.next=last
        while c.next!=last:
            c.next=first
            first=c
            c=p
            p=p.next
        c.next=first
        par.next=c
        if m==1:
            return c
        else:
            return head

def main():
    l=ListNode(1)
    l.addNode(2)
    l.addNode(3)
    l.addNode(4)
    l.addNode(5)
    l.addNode(6)
    l.printNode()
    s=Solution
    s.reverseBetween(s, l, 2, 5).printNode()

main()

