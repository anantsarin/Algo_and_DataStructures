# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1.val ==0 and l1.next==None):
            return l2
        if (l2.val ==0 and l2.next==None):
            return l1

        l3 = ListNode()
        l3start = l3
        start_flag = True
        carry = 0

        while (l1 != None and l2!= None):
            if not start_flag:
                l3.next = ListNode(val = carry)
                l3 = l3.next

            sum1 = (l1.val + l2.val + l3.val)
            l3.val = sum1%10
            carry = (sum1)//10
            l1 = l1.next
            l2 = l2.next
            start_flag = False


        if l1 == None:
            while l2:
                l3.next = ListNode(val=carry)
                l3 = l3.next
                sum1 = (l2.val + l3.val)
                l3.val = sum1%10
                carry = (sum1)//10
                l2 = l2.next


        if l2 == None:
            while l1:
                l3.next = ListNode(val=carry)
                l3 = l3.next
                sum1 = (l1.val + l3.val)
                l3.val = sum1%10
                carry = (sum1)//10
                l1 = l1.next

        if carry == 1:
            l3.next = ListNode(val=carry)

        return l3start