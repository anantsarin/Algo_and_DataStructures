# Python3 program to delete every k-th Node
# of a singly linked list.
import math


# Linked list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# To remove complete list (Needed for
# case when k is 1)
def freeList(node):
    while (node != None):
        next = node.next
        node = next
    return node

def deleteKthNode(head, k):
    if not head:
        return head
    if k == 1:
        return None
    count = 1
    temp = head
    while head and head.next:
        if count == k:
            head.next = head.next.next
            count = 1
            head = head.next
        else:
            count+=1
            head = head.next
    return temp

# Deletes every k-th node and
# returns head of modified list.
# def deleteKthNode(head, k):
#     # If linked list is empty
#     if (head == None):
#         return None
#
#     if (k == 1):
#         freeList(head)
#         return None
#
#     # Initialize ptr and prev before
#     # starting traversal.
#     ptr = head
#     prev = None
#
#     # Traverse list and delete every k-th node
#     count = 0
#     while (ptr != None):
#
#         # increment Node count
#         count = count + 1
#
#         # check if count is equal to k
#         # if yes, then delete current Node
#         if (k == count):
#             # put the next of current Node in
#             # the next of previous Node
#             # delete(prev.next)
#             prev.next = ptr.next
#
#             # set count = 0 to reach further
#             # k-th Node
#             count = 0
#
#         # update prev if count is not 0
#         if (count != 0):
#             prev = ptr
#
#         ptr = prev.next
#
#     return head


# Function to print linked list
def displayList(head):
    temp = head
    while (temp != None):
        print(temp.data, end=' ')
        temp = temp.next


# Utility function to create a new node.
def newNode(x):
    temp = Node(x)
    temp.data = x
    temp.next = None
    return temp


# Driver Code
if __name__ == '__main__':
    # Start with the empty list
    head = newNode(1)
    head.next = newNode(2)
    head.next.next = newNode(3)
    head.next.next.next = newNode(4)
    head.next.next.next.next = newNode(5)
    head.next.next.next.next.next = newNode(6)
    head.next.next.next.next.next.next = newNode(7)
    head.next.next.next.next.next.next.next = newNode(8)

    k = 3
    head = deleteKthNode(head, k)

    displayList(head)


