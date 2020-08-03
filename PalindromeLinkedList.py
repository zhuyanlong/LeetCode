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

#stack法
class Solution:
    def isPalindrome(self, head):
        stack=[]
        slow=head
        fast=head
        while fast!=None:
            fast=fast.next
            if fast:
                fast=fast.next
                stack.append(slow.val)
            slow=slow.next
        # print(stack)
        while slow!=None:
            if stack[-1]!=slow.val:
                return False
            slow=slow.next
            stack.pop()
        return True

#翻转链表，还没有成功
# class Solution:
#     def isPalindrome(self, head):
#         slow=head
#         fast=head
#         while fast!=None:
#             fast=fast.next
#             if fast:
#                 fast=fast.next
#             slow=slow.next
#         if slow.next==None:
#             if slow.val==head.val:
#                 return True
#             else:
#                 return False
#         tmp=slow.next
#         p=tmp.next
#         slow.next=None
#         while p!=None:
#             tmp.next=slow
#             slow=tmp
#             tmp=p
#             p=p.next
#         tmp.next=slow
#         slow=tmp
#         tmp=head
#         while slow!=None:
#             if slow.val!=tmp.val:
#                 return False
#             slow=slow.next
#             tmp=tmp.next
#         return True


def main():
    l=ListNode(1)
    l.addNode(2)
    # l.addNode(3)
    # l.addNode(3)
    # l.addNode(2)
    # l.addNode(1)
    # l.addNode(1)
    # l.addNode(2)
    # l.addNode(3)
    # l.printNode()
    s=Solution()
    print(s.isPalindrome(l))

main()
