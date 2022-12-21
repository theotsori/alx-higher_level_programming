#!/usr/bin/python3
"""A class Node that defines a node of a singly linked list"""


class Node:
    """Node that defines a singly linked list"""
    def __init__(self, data, next_node=None):
        """Initializing data and next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """setting data for linked list"""
        return self._data

    @data.setter
    def data(self, value):
        """setting data value to be an integer"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """setting next node for linked list"""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """setting linked list value"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


"""A class SinglyLinkedList that defines a singly linked list"""


class SinglyLinkedList:
    def __init__(self):
        """Initializing class"""
        self.head = None

    def __str__(self):
        """string attribute to print class"""
        nodes = []
        current_node = self.head
        while current_node is not None:
            nodes.append(str(current_node.data))
            current_node = current_node.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """Sorting node insert value with conditions"""
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node is not None and \
                    current_node.next_node.data < value:
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node
