class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		head=ListNode(0)
		answer=head
		carry=0
		while l1 and l2:
			add=l1.val+l2.val+carry
			if add>=10:
				carry=1
			else:
				carry=0
			head.next=ListNode(add%10)
			head=head.next

		l=l1 if l1 else l2

		while l:
			add=l.val+carry
			if add>=10:
				carry=1
			else:
				carry=0
			head.next=ListNode(add%10)
			head=head.next

		if carry==1:
			head.next=ListNode(1)

		return answer.next
