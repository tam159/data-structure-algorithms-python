from typing import List

def sellection_sort(l: List) -> List:
    """
    Time Complexity	O(n^2).
    Space Complexity O(1).
    """
    for i in range(len(l)-1):
        index_of_min_value = i

        for j in range(i+1, len(l)):
            if l[j] < l[index_of_min_value]:
                index_of_min_value = j

        if i != index_of_min_value:
            temp = l[i]
            l[i] = l[index_of_min_value]
            l[index_of_min_value] = temp

    return l

if __name__ == "__main__":
    my_list = [4, 2, 6, 5, 1, 3]
    print(sellection_sort(my_list))
