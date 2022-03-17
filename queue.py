
class Queue:
    # FIFO (First In First Out)
    # __init__ function
    def __init__(self):
        self.Q: list = []

    def is_empty(self) -> bool:
        return len(self.Q) == 0

    # Function to add an item to the queue.
    # It changes rear and size
    def en_queue(self, item):
        self.Q.append(item)
        print("'% s' enqueued to queue" % str(item))

    # Function to remove an item from queue.
    # It changes front and size
    def de_queue(self):
        if self.is_empty():
            raise Exception('Queue is Empty')

        print("% s dequeued from queue" % str(self.Q[0]))
        self.Q.pop(0)

    # Function to get front of queue
    def que_front(self):
        if self.is_empty():
            print("Queue is empty")
        print("Front item is", self.Q[0])

    # Function to get rear of queue
    def que_rear(self):
        if self.is_empty():
            print("Queue is empty")
        print("Rear item is",  self.Q[len(self.Q)-1])


def main():
    queue = Queue()
    queue.en_queue('a')
    queue.en_queue('b')
    queue.en_queue('c')
    print(queue.Q)

    queue.de_queue()
    print(queue.Q)

    queue.que_front()
    queue.que_rear()


if __name__ == '__main__':
    main()
