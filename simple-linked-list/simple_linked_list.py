class Node:
    def __init__(self, value, next):
        self._value = value
        self._next = next
    def value(self):
        return self._value
    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=[]):
        self._head = None
        for x in values:
            self.push(x)
    def __len__(self):
        size, node = 0, self._head
        while node:
            size += 1
            node = node.next()
        return size
    def __iter__(self):
        cur = self._head
        while cur:
            yield cur.value()
            cur = cur.next()
    def head(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")
        return self._head      
    def push(self, value):
        node = Node(value, self._head)
        self._head = node
        return self
    def pop(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")
        popped = self._head
        self._head = popped.next()
        popped._next = None
        return popped.value()
    def reversed(self):
        rev = LinkedList()
        for x in self:
            rev.push(x)
        return rev

class EmptyListException(Exception):
    def __init__(self, message: str=None):
        self.error_message = message
