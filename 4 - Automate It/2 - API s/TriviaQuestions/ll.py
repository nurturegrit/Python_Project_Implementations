class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.start = new_node
        self.end = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.end.next = new_node
        self.end = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.start
        self.start = new_node
        self.length += 1

    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise IndexError(f"Index:{index} is out the valid index range: 0 to {self.length}")
        elif index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            new_node = Node(value)
            current = self.start  # Start at 0 Index
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.length += 1

    def printlist(self):
        now = self.start
        while now is not None:
            print(now.value)
            now = now.next

ll = LinkedList(50)
ll.printlist()
print()
ll.append(10)
ll.printlist()
print()
ll.prepend(20)
ll.printlist()
print()
ll.insert(1,30)
ll.printlist()