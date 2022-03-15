# Node class
class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next: Node = None  # Initialize
        # next as null


# Linked List class
class LinkedList:
    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head: Node = None

    # Add data to begining (head)
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        # 1. check if the given prev_node exists
        if prev_node is None:
            raise Exception("Previous node can't be null")

        # 2. Create new node &
        # 3. Put in the data
        new_node = Node(new_data)

        # 4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next

        # 5. make next of prev_node as new_node
        prev_node.next = new_node

    # Add data to end
    def append(self, new_data):
        # 1. Create new node &
        # 2. Put in the data
        new_node = Node(new_data)

        # 3. If the Linked List is empty, then make the
        #    new node as head
        if self.head is None:
            self.head = new_node
            return

        # 4. Else traverse till the last node
        last = self.head
        while last.next:
            last = last.next

        # 5. Change the next of last node
        last.next = new_node

    # Delete Node
    def delete(self, data):
        if self.head is not None and self.head.data == data:
            self.head = self.head.next
            return

        prev_node: Node = self.head

        while prev_node.next:
            if prev_node.data == data:
                break
            elif prev_node.next.data == data:
                break
            else:
                prev_node = prev_node.next

        if prev_node.next is None:
            return

        prev_node.next = prev_node.next.next

    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


def main():
    # Start with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    '''
    Three nodes have been created.
    We have references to these three blocks as head,
    second and third
 
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  | None |     | 2  | None |     |  3 | None |
    +----+------+     +----+------+     +----+------+
    '''

    # Link first node with second
    llist.head.next = second

    '''
    Now next of first Node refers to second.  So they
    both are linked.
 
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  | null |     |  3 | null |
    +----+------+     +----+------+     +----+------+
    '''

    # Link second node with the third node
    second.next = third

    '''
    Now next of second Node refers to third.  So all three
    nodes are linked.
 
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  |  o-------->|  3 | null |
    +----+------+     +----+------+     +----+------+
    '''

    llist.append(4)
    llist.push(5)
    llist.append(6)
    
    llist.delete(6)

    llist.printList()


if __name__ == '__main__':
    main()
