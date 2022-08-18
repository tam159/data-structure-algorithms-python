def item_in_common(list1, list2) -> bool:
    """
    Using nested loop with O(n^2).

    :param list1:
    :param list2:
    :return: True if there is a common item
    """
    for i in list1:
        for j in list2:
            if i == j:
                return True

    return False


def common_item(list1, list2) -> bool:
    """
    Using dictionary/hash table with O(n).

    :param list1:
    :param list2:
    :return: True if there is a common item
    """
    list1_dict = {}
    # O(n)
    for value in list1:
        list1_dict[value] = True

    # O(n)
    for value in list2:
        if value in list1_dict:
            return True

    return False


if __name__ == "__main__":
    list1 = [1, 3, 5]
    list2 = [2, 4, 5]
    print(item_in_common(list1, list2))
    print(common_item(list1, list2))
