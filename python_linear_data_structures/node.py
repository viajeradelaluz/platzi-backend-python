"""
Module to create simple linked list and traverses it for node data.
The linked list uses the class Node to create node instances.
"""


class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def main() -> None:
    # Creating a linked list.
    linked_list = []
    node = None
    for num in range(5, 0, -1):
        node = Node(num, node)
        linked_list.insert(0, node.data)

    # Traversing the linked list to save the data and print it.
    to_print = ''
    while node:
        to_print += f'{node.data} -> '
        node = node.next
    to_print = to_print[:-4]

    print(linked_list)
    print(to_print)


if __name__ == '__main__':
    main()
