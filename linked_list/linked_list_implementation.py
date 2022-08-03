from typing import Optional

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

    def pop(self) -> Optional[int]:
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
            return temp.value




    def prepend(self, value):
        pass

    def insert(self, index, value):
        pass

    def print_list(self):
        temp = self.head
        while temp:
            print(f"Value: {temp.value}")
            temp = temp.next


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
# print(my_linked_list.head.value)
print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())
my_linked_list.print_list()
