# Python program to reverse a
# linked list in group of given size

# Node class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def reverse(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

    def reverse_ll_group(self, head, k):
        prev = None
        temp = None
        count = 0
        list_head = head
        while head and count < k:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
            count += 1
        if temp != None:
            list_head.next = self.reverse_ll_group(temp, k)
        return prev

    def printll(self, head):
        while head:
            print(head.data)
            head = head.next

    def reverse_ll_alternate_group(self, head, k):
        if not head:
            return None
        curr_head = head
        prev = None
        temp = None
        count = 0

        while head and count < k:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
            count += 1

        count = 0
        curr_head.next = temp
        while curr_head and count < k:
            curr_head = curr_head.next
            count += 1
        if curr_head != None:
            curr_head.next = self.reverse_ll_alternate_group(curr_head.next, k)

        return prev

    def skip_m_delete_n(self, head, m, n):
        curr = head
        while curr:
            count = 1
            # skip m nodes
            while (curr and count < m):
                curr = curr.next
                count += 1
            count = 0
            # delete n nodes
            while (curr and curr.next and count < n):
                curr.next = curr.next.next
                count += 1
            if curr:
                curr = curr.next
        return head


# Driver program
llist = linkedList()
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print("Given linked list")
llist.printll(llist.head)
llist.head = llist.reverse(llist.head)

print("\nReversed Linked list")
llist.printll(llist.head)

llist.head = llist.reverse_ll_group(llist.head, 3)

print("\nReversed Linked list by group")
llist.printll(llist.head)

llist.head = llist.reverse_ll_alternate_group(llist.head, 3)
print("\nReversed Linked list alternate group")
llist.printll(llist.head)

llist.head = llist.skip_m_delete_n(llist.head, 2, 2)
print("\nskip M and delete N ")
llist.printll(llist.head)

