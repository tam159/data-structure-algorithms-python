from typing import List

def insertion_sort(l: List) -> List:
    """
    Time Complexity	O(n^2).
    Space Complexity O(1).
    """
    for i in range(1, len(l)):
        temp = l[i]
        j = i - 1
        while temp < l[j] and j >= 0:
            l[j+1] = l[j]
            l[j] = temp
            j -= 1

    return l


if __name__ == "__main__":
    my_list = [4, 2, 6, 5, 1, 3]
    print(insertion_sort(my_list))
