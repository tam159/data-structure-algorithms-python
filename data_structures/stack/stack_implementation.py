from typing import List, Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value):
        new_node = Node(value)

        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

        self.height += 1

    @property
    def pop(self) -> Optional[Node]:
        if self.height == 0:
            return None

        popped_node = self.top
        self.top = self.top.next

        popped_node.next = None
        self.height -= 1

        return popped_node

    @property
    def print_stack(self) -> List:
        output = []
        temp = self.top

        while temp:
            output.append(temp.value)
            temp = temp.next

        print("-----" * 10)
        return output


if __name__ == "__main__":
    my_stack = Stack(7)

    print(my_stack.print_stack)

    my_stack.push(23)
    my_stack.push(3)
    my_stack.push(11)
    print(my_stack.print_stack)

    print(my_stack.pop.value)
    print(my_stack.print_stack)
