from typing import List

def bubble_sort(l: List) -> List:
    """
    Time Complexity	O(n^2).
    Space Complexity O(1).
    """
    for i in range(len(l)-1, 0, -1):
        for j in range(i):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp

    return l


if __name__ == "__main__":
    my_list = [4, 2, 6, 5, 1, 3]
    print(bubble_sort(my_list))
