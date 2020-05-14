from src.binary_search.design.SingleLinkedList.SingleLinkedList import SingleLinkedList


class MyHashMap:

    def __init__(self):
        """ initialising the hash-map here"""
        self.list: SingleLinkedList = SingleLinkedList()

    def put(self, key: int, value: int) -> None:
        """ value will always be non negative"""
        self.list.add_node((key, value))

    def get(self, key: int) -> int:
        """returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key"""
        return self.list.get_node(key)

    def remove(self, key: int) -> None:
        """removes the mapping of the specified value key if this map contains a mapping for the key"""
        self.list.remove_node(key)


if __name__ == '__main__':
    hash_map = MyHashMap()
    hash_map.put(1, 10)
    hash_map.put(2, 20)
    print(hash_map.get(1))
    print(hash_map.get(3))
    hash_map.put(2, 1) # needs to update the value
    print(hash_map.get(2)) # should return 1 now
    hash_map.remove(2)
    print(hash_map.get(2))
