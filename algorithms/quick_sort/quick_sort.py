from typing import List

def swap(list: List, index1: int, index2: int) -> List:
    """Swap two values of two indexes."""
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp

    return list


def pivot(list: List, pivot_index: int, end_index: int) -> int:
    """
    Pivot the list.
    O(n)
    """
    swap_index = pivot_index

    for index in range(pivot_index+1, end_index):
        if list[index] < list[pivot_index]:
            swap_index += 1
            swap(list, swap_index, index)

    swap(list, pivot_index, swap_index)

    return swap_index


def quick_sort(list: List) -> List:
    """
    Quick sort a lit.
    Average: O(n log n)
    The Worst case when there is an already sorted array: O(n^2)
    """
    if len(list) <= 1:
        return list

    pivot_index = pivot(list, 0, len(list))
    left = list[:pivot_index]
    right = list[pivot_index+1:]

    return quick_sort(left) + [list[pivot_index]] + quick_sort(right)


if __name__ == "__main__":
    list = [4, 6, 1, 7, 3, 2, 5]
    list2 = [2, 7, 4, 3, 8, 5, 9, 1, 6]
    list3 = [1, 2, 3, 4, 5, 6, 7]
    # print(pivot(list3, 0, len(list3)))
    # print(list3)
    # print(quick_sort(list))
    print(quick_sort(list2))
