from typing import List, Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value) -> bool:
        """
        Sample Linked List:
        11 -> 3 -> 23 -> 7
        0     1    2     3

        self.append(4)
        11 -> 3 -> 23 -> 7 -> 4
        0     1    2     3    4

        :param value: appended value
        :return: True if append successfully
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail

            self.tail = new_node

        self.length += 1

        return True

    def prepend(self, value) -> bool:
        """
        Sample Linked List:
        11 -> 3 -> 23 -> 7
        0     1    2     3

        self.prepend(4)
        4 -> 11 -> 3 -> 23 -> 7
        0    1     2     3    4

        :param value: prepended value
        :return: True if prepend successfully
        """
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1

        return True

    @property
    def pop(self) -> Optional[Node]:
        """
        Sample Linked List:
        11 -> 3 -> 23 -> 7 -> 4
        0     1    2     3    4

        self.pop()
        11 -> 3 -> 23 -> 7
        0     1    2     3

        :return: popped Node
        """
        if self.length == 0:
            raise LookupError("The Linked List is empty")

        temp = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None

        self.length -= 1

        return temp

    @property
    def pop_first(self) -> Optional[Node]:
        """
        Sample Linked List:
        4 -> 11 -> 3 -> 23 -> 7
        0    1     2     3    4

        self.pop_first()
        11 -> 3 -> 23 -> 7
        0     1    2     3

        :return: popped Node
        """
        if self.length == 0:
            raise LookupError("The Linked List is empty")

        temp = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            self.head.prev = None
            temp.next = None

        self.length -= 1

        return temp

    def get(self, index) -> Optional[Node]:
        """
        Sample Linked List:
        11 -> 3 -> 23 -> 7
        0     1    2     3

        :param index: index from 0 to length - 1
        :return: Node
        """
        if self.length == 0:
            raise LookupError("The Linked List is empty")

        if index < 0 or index >= self.length:
            raise ValueError(f"Index should be between 0 and {self.length -1}")

        if index < self.length / 2:
            node = self.head
            for _ in range(index):
                node = node.next
        else:
            node = self.tail
            for _ in range(self.length - 1, index, -1):
                node = node.prev

        return node

    def set_value(self, index, value) -> Optional[Node]:
        """
        Sample Linked List:
        11 -> 3 -> 23 -> 7
        0     1    2     3

        :param index: index from 0 to length - 1
        :param value: value of node with the index
        :return: Node
        """
        node = self.get(index)
        node.value = value

        return node

    def insert(self, index, value) -> bool:
        """
        Sample Linked List:
        11 -> 5 -> 23 -> 7
        0     1    2     3

        self.insert(2, 20)
        11 -> 5 -> 20 -> 23 -> 7
        0     1    2     3     4

        :param index: index from 0 to length - 1
        :param value: value of node with the index
        :return: True if insert successfully
        """
        if index < 0 or index > self.length:
            raise ValueError(f"Index should be between 0 and {self.length}")

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        after = self.get(index)
        before = after.prev

        before.next = new_node
        after.prev = new_node

        new_node.prev = before
        new_node.next = after

        self.length += 1

        return True

    def delete(self, index) -> Optional[Node]:
        """
        Sample Linked List:
        11 -> 5 -> 20 -> 23 -> 7
        0     1    2     3     4

        self.delete(2)
        11 -> 5 -> 23 -> 7
        0     1    2     3

        :param index: index from 0 to length - 1
        :return: True if delete successfully
        """
        deleted_node = self.get(index)

        if self.length == 1:
            self.head = None
            self.tail = None

        if index == 0:
            return self.pop_first
        elif index == self.length - 1:
            return self.pop
        else:
            deleted_node.prev.next = deleted_node.next
            deleted_node.next.prev = deleted_node.prev

            deleted_node.prev = None
            deleted_node.next = None

            self.length -= 1

        return deleted_node

    @property
    def print_list(self) -> List:
        output = []
        temp = self.head
        while temp:
            output.append(temp.value)
            temp = temp.next

        print("-----" * 10)
        return output


my_doubly_linked_list = DoublyLinkedList(11)
print(my_doubly_linked_list.print_list)

my_doubly_linked_list.append(3)
my_doubly_linked_list.append(23)
my_doubly_linked_list.append(7)
my_doubly_linked_list.append(4)
print(my_doubly_linked_list.print_list)

print(my_doubly_linked_list.pop.value)
print(my_doubly_linked_list.print_list)

my_doubly_linked_list.prepend(4)
print(my_doubly_linked_list.print_list)

print(my_doubly_linked_list.pop_first.value)
print(my_doubly_linked_list.print_list)

print(my_doubly_linked_list.get(2).value)
print(my_doubly_linked_list.set_value(1, 5).value)
print(my_doubly_linked_list.print_list)

my_doubly_linked_list.insert(2, 20)
print(my_doubly_linked_list.print_list)

print(my_doubly_linked_list.delete(3).value)
print(my_doubly_linked_list.print_list)
