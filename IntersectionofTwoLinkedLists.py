# Definition for singly-linked list.
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

#因为多次遍历导致时间复杂度比较低
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         lenA=0
#         lenB=0
#         tmpA=headA
#         tmpB=headB
#         while tmpA!=None:
#             lenA+=1
#             tmpA=tmpA.next
#         while tmpB!=None:
#             lenB+=1
#             tmpB=tmpB.next
#         tmpA=headA
#         tmpB=headB
#         if lenA>lenB:
#             diff=lenA-lenB
#             while diff!=0:
#                 tmpA=tmpA.next
#                 diff-=1
#         elif lenB>lenA:
#             diff=lenB-lenA
#             while diff!=0:
#                 tmpB=tmpB.next
#                 diff-=1
#         while tmpA!=None:
#             if tmpA==tmpB:
#                 return tmpA
#             else:
#                 tmpA=tmpA.next
#                 tmpB=tmpB.next
#         return None

#结环遍历
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        tmpA=headA
        tmpB=headB
        if headA==None or headB==None:
            return None
        while tmpA!=None or tmpB!=None:
            if tmpA==None:
                tmpA=headB
            if tmpB==None:
                tmpB=headA
            if tmpA==tmpB:
                return tmpA
            tmpA=tmpA.next
            tmpB=tmpB.next
        return None

def main():
    l=ListNode(1)
    l.addNode(1)
    l.addNode(2)
    l.addNode(2)
    l.addNode(3)
    l.addNode(3)
    # l.printNode()
    b=ListNode(1)
    b.addNode(1)
    # b.addNode(2)
    # b.addNode(2)
    # b.addNode(3)
    # b.addNode(3)
    tmp=b
    while tmp.next!=None:
        tmp=tmp.next
    tmp.next=l.next.next
    # b.printNode()
    s=Solution()
    print(s.getIntersectionNode(l,b))

main()