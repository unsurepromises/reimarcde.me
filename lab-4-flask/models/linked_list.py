class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def delete(self, data):
        if not self.head:
            return False
        if str(self.head.data) == str(data):
            self.head = self.head.next
            return True
        curr = self.head
        while curr.next and str(curr.next.data) != str(data):
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next
            return True
        return False

    def clear(self):
        self.head = None

    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result


linked_list = LinkedList()
