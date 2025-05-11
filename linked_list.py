#create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_at_end(data)
            return
        current_node = self.head

        count=0
        while current_node is not None and count+1!=index:
            current_node = current_node.next
            count+=1

        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index out of range")

    def delete_at_index(self, index):
        if index == 0 and self.head is not None:
            self.head = self.head.next
            return

        current_node = self.head
        position = 0

        while current_node is not None and position < index - 1:
            current_node = current_node.next
            position += 1

        if current_node is None or current_node.next is None:
            print("Index out of bounds.")
            return

        current_node.next = current_node.next.next

    def search(self, value):
        current_node = self.head
        index = 0
        while current_node is not None:
            if current_node.data == value:
                return index
            current_node = current_node.next
            index += 1
        return -1

    def display(self):
        current_node = self.head
        if current_node is None:
            print("The list is empty.")
            return
        while current_node is not None:
            print(current_node.data, end=" -> " if current_node.next is not None else "")
            current_node = current_node.next
        print()
