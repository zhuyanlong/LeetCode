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

#这大概是最普通的一种解法，效率也是最低的，高效解法要利用好，排序数组
# class Solution:
#     def deleteDuplicates(self, head):
#         i=head
#         while i!=None:
#             p=i
#             j=i.next
#             while j!=None:
#                 if j.val==i.val:
#                     j=j.next
#                     p.next=j
#                 else:
#                     j=j.next
#                     p=p.next
#             # i.printNode()
#             i=i.next
#         return head

#用这种方式后，时间复杂度大幅度缩减，但还是不够快
# class Solution:
#     def deleteDuplicates(self, head):
#         i=head
#         while i!=None:
#             p=i
#             j=i.next
#             while j!=None:
#                 if j.val==i.val:
#                     j=j.next
#                     p.next=j
#                 else:
#                     break
#             i=i.next
#         return head

#可以试着用空间来换时间，重新构造一个链表，这样子可能要快很多
#实际上得到的结果并没有快很多
# class Solution:
#     def deleteDuplicates(self, head):
#         if head==None:
#             return head
#         i=head
#         res=ListNode(i.val)
#         head=res
#         i=i.next
#         while i!=None:
#             if i.val!=res.val:
#                 res.next=ListNode(i.val)
#                 res=res.next
#             i=i.next
#         return head

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
        p = head
        while p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head

def main():
    l=ListNode(1)
    l.addNode(1)
    # l.addNode(2)
    # l.addNode(2)
    # l.addNode(3)
    # l.addNode(3)
    # l.printNode()
    s=Solution
    s.deleteDuplicates(None,l).printNode()
    # l.printNode()

main()
