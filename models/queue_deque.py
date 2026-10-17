class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = QueueNode(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

    def to_list(self):
        result = []
        current = self.front
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __iter__(self):
        current = self.front
        while current:
            yield current.data
            current = current.next

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")



class DequeNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedDeque:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def add_front(self, data):
        new_node = DequeNode(data)
        if self.is_empty():
            self.front = self.rear = new_node
            return
        new_node.next = self.front
        self.front.prev = new_node
        self.front = new_node

    def add_rear(self, data):
        new_node = DequeNode(data)
        if self.is_empty():
            self.front = self.rear = new_node
            return
        new_node.prev = self.rear
        self.rear.next = new_node
        self.rear = new_node

    def remove_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None
        return temp.data

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        temp = self.rear
        self.rear = temp.prev
        if self.rear is None:
            self.front = None
        else:
            self.rear.next = None
        return temp.data

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.front.data

    def peek_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.rear.data

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def to_list(self):
        result = []
        current = self.front
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __iter__(self):
        current = self.front
        while current:
            yield current.data
            current = current.next