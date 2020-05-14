class Node:
    def __init__(self, data: tuple):
        self.data = data
        self.next = None

    def set_data(self, data: tuple) -> None:
        self.data = data


def check_node_exists(head: Node, val: int) -> bool:
    traveler = head
    while traveler is not None:
        if traveler.data[0] == val:
            return True
        traveler = traveler.next
    return False


class SingleLinkedList:
    def __init__(self):
        self.preHead = Node((0, 0))

    def add_node(self, val: tuple) -> None:
        # need to check if is first node
        new_node = Node(val)
        if self.preHead.next is None:
            self.preHead.next = new_node
            return

        # need to check if the node already exists
        node_exists = check_node_exists(self.preHead.next, val[0])
        # print("node exists: ", node_exists)
        traveler = self.preHead

        if node_exists:
            while traveler.data[0] != val[0]:
                traveler = traveler.next
            traveler.set_data(val)
            return
        else:
            while traveler.next is not None:
                traveler = traveler.next
            traveler.next = new_node

    def get_node(self, key) -> int:
        traveler = self.preHead
        while traveler is not None:
            if traveler.data[0] == key:
                break
            traveler = traveler.next

        if traveler is None:
            return -1
        else:
            return traveler.data[1]

    def remove_node(self, key: int) -> None:
        pre: Node = self.preHead
        head: Node = self.preHead.next
        if head.data[0] != key:
            while head is not None and head.data[0] != key:
                pre = pre.next
                head = head.next

        pre.next = head.next

    def print_list(self):
        traveler = self.preHead
        print("printing list")
        while traveler is not None:
            print(traveler.data, end=", ")
            traveler = traveler.next
        print()
        print("----")


if __name__ == '__main__':
    list = SingleLinkedList()
    list.add_node((1, 10))
    list.add_node((2, 20))
    list.add_node((3, 30))
    list.add_node((4, 40))
    list.add_node((2, 200))

    # list.remove_node(1)
    # list.remove_node(3)

    print(list.get_node(2))
    print(list.get_node(1))
    list.print_list()
