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
        while tmp.next!=None:
            print(tmp.val)
            tmp=tmp.next
        print(tmp.val)

# class Solution:
#     def removeNthFromEnd(self, head, n):
#         num=0
#         tmp=head
#         l=head
#         p=head
#         while tmp!=None:
#             tmp=tmp.next
#             num+=1
#         if num==1 or num==0:
#             return None
#         if num==n:
#             return l.next
#         target=num-n+1
#         i=1
#         while i!=target:
#             p=head
#             head=head.next
#             i+=1
#         p.next=head.next
#         return l


class Solution:
    def removeNthFromEnd(self, head, n):
        tmp=ListNode(0)
        tmp.next=head
        p1=p2=tmp
        for i in range(n):
            p1=p1.next
        while p1.next!=None:
            p1=p1.next
            p2=p2.next
        p2.next=p2.next.next
        return tmp


def main():
    l=ListNode(1)
    # l.addNode(2)
    # l.addNode(3)
    # l.addNode(4)
    # l.addNode(5)
    s=Solution
    s.removeNthFromEnd(None,l,1).printNode()
    # l.printNode()

main()