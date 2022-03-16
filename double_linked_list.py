# Node of a doubly linked list
import re


class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next  # reference to next node in DLL
        self.prev = prev  # reference to previous node in DLL
        self.data = data


# Class to create a Doubly Linked List
class DoublyLinkedList:

    # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head: Node = None

    # Add data to begining (head)
    def push(self, new_data):
        new_node = Node(data=new_data, next=self.head)
        if self.head is None:
            self.head = new_node
            return

        self.head.prev = new_node
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        # 1. check if the given prev_node exists
        if prev_node is None:
            raise Exception("Previous node can't be null")

        # 2. Create new node &
        # 3. Put in the data
        new_node = Node(data=new_data)

        # 4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next

        # 5. Make the next of prev_node as new_node
        new_node.prev = prev_node

        # 6. make next of prev_node as new_node
        prev_node.next = new_node

        # 7. Change previous of new_node's next node
        if new_node.next is not None:
            new_node.next.prev = new_node

    def print_list(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


def main():
    dll = DoublyLinkedList()
    dll.push(1)
    dll.push(0)
    dll.insert_after(dll.head, 3)

    dll.print_list()


if __name__ == '__main__':
    main()
