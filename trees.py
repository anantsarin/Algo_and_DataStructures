from collections import deque


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    def pre_order(self, root):
        print("\n print pre order ")
        stack = deque()
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            print(node.data, " ", end="")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def in_order(self, root):
        print("\n print in order ")
        stack = deque()
        # stack.append(root)
        current = root
        while True:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.data, " ", end="")
                current = current.right
            else:
                break

    def peek(self, stack):
        if stack:
            return stack[-1]
        return None

    def post_order(self, root):
        print("\n print post order ")
        stack = deque()
        current = root
        while True:
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left
            root = stack.pop()

            if root.right and self.peek(stack) == root.right:
                stack.pop()
                stack.append(root)
                root = root.right

            else:
                print(root.data, " ", end="")
                root = None
            if len(stack) <= 0:
                break



    def zizagtraversal(self, root):
        print(" \n print zigzag  order ")
        # Base Case
        if root is None:
            return

        # Create two stacks to store current
        # and next level
        currentLevel = []
        nextLevel = []

        # if ltr is true push nodes from
        # left to right otherwise from
        # right to left
        ltr = True

        # append root to currentlevel stack
        currentLevel.append(root)

        # Check if stack is empty
        while len(currentLevel) > 0:
            # pop from stack
            temp = currentLevel.pop(-1)
            # print the data
            print(temp.data, " ", end="")

            if ltr:
                # if ltr is true push left
                # before right
                if temp.left:
                    nextLevel.append(temp.left)
                if temp.right:
                    nextLevel.append(temp.right)
            else:
                # else push right before left
                if temp.right:
                    nextLevel.append(temp.right)
                if temp.left:
                    nextLevel.append(temp.left)

            if len(currentLevel) == 0:
                # reverse ltr to push node in
                # opposite order
                ltr = not ltr
                # swapping of stacks
                currentLevel, nextLevel = nextLevel, currentLevel


root = Node(12)
root.insert(6)
root.insert(8)
root.insert(14)
root.insert(3)
root.insert(13)
root.insert(16)

# root.PrintTree()
root.pre_order(root)
root.in_order(root)
root.post_order(root)
root.zizagtraversal(root)
