class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """docstring for LinkedList"""

    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data, end=",")
            tmp = tmp.next
        print()


# reverse a LL

def LL_reverse(head):
    head = head
    temp = None
    while head is not None:
        # print(head.data)
        nextNode = head.next
        head.next = temp
        temp = head
        head = nextNode
    # print(temp.data)
    # print("head.data")
    return temp


def printList(head):
    tmp = head
    while tmp is not None:
        print(tmp.data, end=",")
        tmp = tmp.next
    print()


ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
ll.push(6)
ll.printList()

print("abc")
head1 = LL_reverse(ll.head)
print("abc")
printList(head1)
print("abc")
