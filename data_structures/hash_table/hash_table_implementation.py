from typing import List, Optional


class HashTable:
    def __init__(self, size=7):
        """
        Init method.

        :param size: size of table, should be a prime number for a better distribution
        """
        self.data_map: List = [None] * size

    # O(1)
    def __hash(self, key) -> int:
        """
        Create hash calculation with a prime number e.g. 23

        :param key: key
        :return: value after hashing
        """
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    # O(1)
    def set_item(self, key, value):
        index = self.__hash(key)
        if not self.data_map[index]:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    # O(1)
    def get_item(self, key) -> Optional[int]:
        index = self.__hash(key)
        pairs = self.data_map[index]
        if pairs:
            for pair in pairs:
                if key in pair:
                    return pair[1]

        return None

    @property
    def keys(self) -> List[Optional[str]]:
        all_keys = []
        for data in self.data_map:
            if data:
                for pair in data:
                    all_keys.append(pair[0])

        return all_keys

    @property
    def print_table(self) -> List:
        output = []
        for index, value in enumerate(self.data_map):
            output.append(f"{index}: {value}")

        print("-----" * 10)
        return output


if __name__ == "__main__":
    my_hash_table = HashTable()
    print(my_hash_table.print_table)

    my_hash_table.set_item("bolts", 1400)
    my_hash_table.set_item("washers", 50)
    my_hash_table.set_item("lumber", 70)

    print(my_hash_table.print_table)
    print(my_hash_table.get_item("washers"))

    print(my_hash_table.keys)
