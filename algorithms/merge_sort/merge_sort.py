from typing import List


def merge(list1: List[int], list2: List[int]) -> List[int]:
    """
    Merge two sorted list into one sorted list.
    Time complexity: O(n)
    """
    combined_list: List = []
    index1: int = 0
    index2: int = 0
    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] < list2[index2]:
            combined_list.append(list1[index1])
            index1 += 1
        else:
            combined_list.append(list2[index2])
            index2 += 1

    combined_list.extend(list1[index1:])
    combined_list.extend(list2[index2:])
    return combined_list


def break_list(list: List[int]) -> List[List[int]]:
    """
    Break the list into a list of a list of 1 element.
    Time complexity: O(n)
    """
    return [[element] for element in list]


def merge_sort(list: List[int]) -> List[int]:
    """
    Sort the list by breaking it in half then merge them together.
    Time complexity: O(n log n)
    Space complexity: O(n)
    """
    if len(list) == 1:
        return list

    middle_index: int = len(list) // 2
    left: list = list[:middle_index]
    right: list = list[middle_index:]

    return merge(merge_sort(left), merge_sort(right))


def merge_sort2(list: List[int]) -> List[int]:
    """
    Sort the list by breaking it into a list of a list of 1 element, then merge them.
    """
    broken_list = break_list(list)
    while len(broken_list) > 1:
        broken_list = [
            merge(broken_list[index], broken_list[index + 1])
            for index in range(0, len(broken_list) - 1, 2)
        ]

    sorted_list = broken_list[0]
    if len(sorted_list) < len(list):
        sorted_list = merge(sorted_list, [list[-1]])

    return sorted_list


if __name__ == "__main__":
    list1: list = [1, 3, 7, 8]
    list2: list = [2, 4, 5, 6]
    print(merge(list1, list2))
    list = [2, 7, 4, 3, 8, 5, 9, 1, 6]
    print(merge_sort(list))
    print(merge_sort2(list))
