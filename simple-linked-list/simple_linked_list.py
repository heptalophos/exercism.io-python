class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def value(self):
        return self.value

    def next(self):
        return self.next


class LinkedList:
    def __init__(self, values=[]):
        self.elements = values
        self.first = None
        for x in values:
            self.push(x)

    def __len__(self):
        size, node = 0, self.first
        while node:
            node = node.next()
            size += 1
        return size
    
    def __iter__(self):
        node = self.head()
        while node is not None:
            yield node.value()
            node = node.next()

    def head(self):
        if not self.first:
            raise EmptyListException("The list is empty.")
        return self.first            

    def push(self, value):
        node = Node(self.head())
        self.first = node
        return self

    def pop(self):
        if self.head() is None:
            raise EmptyListException("The list is empty.")
        popped = self.head().value()
        self.first = self.first.next()
        return popped

    def reversed(self):
        return LinkedList(self)


class EmptyListException(Exception):
    def __init__(self, message: str=None):
        self.message = message
