from typing import List


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value) -> bool:
        new_node = Node(value)

        if not self.root:
            self.root = new_node
            return True

        temp = self.root

        while temp:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if not temp.left:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = new_node
                    return True
                temp = temp.right

    # O(log n)
    def contains(self, value) -> bool:
        temp = self.root

        while temp:
            if value == temp.value:
                return True
            if value < temp.value:
                temp = temp.left
            else:
                temp = temp.right

        return False

    # O(n)
    def min_value_node(self, current_node: Node) -> Node:
        while current_node.left:
            current_node = current_node.left

        return current_node

    @property
    def breadth_first_search(self) -> List:
        """Traverse the tree in breadth"""
        output = []
        queue = [self.root]

        while queue:
            output.append(queue[0].value)
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            queue.pop(0)

        return output

    def dfs_pre_order(self, current_node: Node = None) -> List:
        """Traverse the tree in pre-order depth"""
        output = []

        if not current_node:
            current_node = self.root

        output.append(current_node.value)

        if current_node.left:
            output.extend(self.dfs_pre_order(current_node.left))

        if current_node.right:
            output.extend(self.dfs_pre_order(current_node.right))

        return output

    def dfs_post_order(self, current_node: Node = None) -> List:
        """Traverse the tree in post-order depth"""
        output = []

        if not current_node:
            current_node = self.root

        if current_node.left:
            output.extend(self.dfs_post_order(current_node.left))

        if current_node.right:
            output.extend(self.dfs_post_order(current_node.right))

        output.append(current_node.value)

        return output

    def dfs_in_order(self, current_node: Node = None) -> List:
        """Traverse the tree in in-order depth"""
        output = []

        if not current_node:
            current_node = self.root

        if current_node.left:
            output.extend(self.dfs_in_order(current_node.left))

        output.append(current_node.value)

        if current_node.right:
            output.extend(self.dfs_in_order(current_node.right))

        return output


if __name__ == "__main__":
    my_tree = BinarySearchTree()
    print(my_tree.root)

    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)
    print(my_tree.root.value)
    print(my_tree.root.left.value)
    print(my_tree.root.right.value)

    print(my_tree.contains(100))

    print(my_tree.min_value_node(my_tree.root).value)
    print(my_tree.min_value_node(my_tree.root.right).value)

    print(my_tree.breadth_first_search)
    print(my_tree.dfs_pre_order())
    print(my_tree.dfs_post_order())
    print(my_tree.dfs_in_order())
