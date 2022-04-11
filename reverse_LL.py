# reverse  ll in pairs
from interview import Node, LinkedList, LL_reverse, printList


def reverse_Ll_in_pair(head):
    # temp = None
    if head is None or head.next is None:
        return
    else:
        temp = head.next
        head.next = head.next.next
        temp.next = head
        head = temp

        head.next.next = reverse_Ll_in_pair(head.next.next)
        return head


def revert_ll_iteratave(head):
    temp1 = None
    temp2 = None
    while head is not None and head.next is not None:
        if temp1 is not None:
            temp1.next.next = head.next
        temp1 = head.next
        head.next = head.next.next
        temp1.next = head
        if temp2 is None:
            temp2 = temp1
        head = head.next

    return temp2

#def revert_k_elements(head):


ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
# ll.push(6)
ll.printList()

print("abc")
head1 = revert_ll_iteratave(ll.head)
print("abc")
printList(head1)
