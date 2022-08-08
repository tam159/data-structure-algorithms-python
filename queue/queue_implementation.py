from typing import List, Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    # O(1)
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1

    # O(1)
    @property
    def dequeue(self) -> Optional[Node]:
        if self.length == 0:
            return None

        de_node = self.first

        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            de_node.next = None

        self.length -= 1

        return de_node

    @property
    def print_queue(self) -> List:
        output = []
        temp = self.first

        while temp:
            output.append(temp.value)
            temp = temp.next

        print("-----" * 10)
        return output


if __name__ == "__main__":
    my_queue = Queue(1)
    my_queue.enqueue(2)

    print(my_queue.print_queue)

    print(my_queue.dequeue.value)
    print(my_queue.dequeue.value)
    print(my_queue.print_queue)
