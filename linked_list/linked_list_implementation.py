from typing import Optional, List


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value) -> bool:
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

        return True

    def prepend(self, value) -> bool:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

        if not self.tail:
            self.tail = new_node

        self.length += 1

        return True

    @property
    def pop(self) -> Optional[Node]:
        global pre

        if not self.head:
            return None

        else:
            temp = self.head
            if self.length == 1:
                self.head = None
                self.tail = None

            else:
                while temp.next:
                    pre = temp
                    temp = temp.next

                self.tail = pre
                self.tail.next = None

            self.length -= 1
            return temp

    @property
    def pop_first(self) -> Optional[Node]:
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None

            if self.length == 1:
                self.tail = None

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

        node = self.head

        for _ in range(index):
            node = node.next

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
        11 -> 3 -> 23 -> 7
        0     1    2     3

        self.insert(2, 20)
        11 -> 3 -> 20 -> 23 -> 7
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
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node

        self.length += 1

        return True

    def delete(self, index) -> Optional[Node]:
        """
        Sample Linked List:
        11 -> 3 -> 20 -> 23 -> 7
        0     1    2     3     4

        self.delete(2)
        11 -> 3 -> 23 -> 7
        0     1    2     3

        :param index: index from 0 to length - 1
        :return: True if delete successfully
        """
        node = self.get(index)
        if self.length == 1:
            self.head = None
            self.tail = None

        else:
            self.get(index - 1).next = node.next
            node.next = None

        self.length -= 1
        return node

    def reverse(self):
        """
        Sample Linked List:
        11 -> 3 -> 32 -> 7
        0     1    2     3

        self.reverse(2)
        7 -> 32 -> 3 -> 11
        0     1    2    3

        :return: reversed Linked List
        """
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before

            before = temp
            temp = after

        return self

    @property
    def print_list(self) -> List:
        output = []

        temp = self.head
        while temp:
            output.append(temp.value)
            temp = temp.next

        return output


if __name__ == "__main__":
    my_linked_list = LinkedList(1)
    my_linked_list.append(2)
    my_linked_list.append(3)

    print(my_linked_list.pop.value)
    print(my_linked_list.pop.value)
    print(my_linked_list.delete(0).value)

    print(my_linked_list.pop)

    my_linked_list.prepend(0)
    my_linked_list.prepend(-1)

    print(my_linked_list.print_list)
    print("-----" * 10)

    print(my_linked_list.pop_first.value)
    print(my_linked_list.pop_first.value)
    print(my_linked_list.pop_first)

    print(my_linked_list.print_list)
    print("-----" * 10)

    my_linked_list.append(11)
    my_linked_list.append(3)
    my_linked_list.append(23)
    my_linked_list.append(7)

    print(my_linked_list.print_list)
    print(my_linked_list.get(2).value)

    my_linked_list.set_value(2, 32)

    print(my_linked_list.print_list)
    print("-----" * 10)

    my_linked_list.insert(2, 20)

    print(my_linked_list.print_list)
    print("-----" * 10)

    print(my_linked_list.delete(2).value)
    print(my_linked_list.print_list)
    print("-----" * 10)

    my_linked_list.reverse()
    print(my_linked_list.print_list)
    print("-----" * 10)
