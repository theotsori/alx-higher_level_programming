#!/usr/bin/python3
"""A class Node that defines a node of a singly linked list"""


class Node:
    """A class that defines a node in a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node or None): The next node in the linked list.
    """
    def __init__(self, data, next_node=None):
        """Initializes a node with the given data and next node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node or None): The next node in the linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """int: setting data for linked list"""
        return self._data

    @data.setter
    def data(self, value):
        """Sets the data of the node.

        Args:
            value (int): The value to set as the data of the node.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Node or None: setting next node for linked list"""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node of the node.

        Args:
            value (Node or None): The next node in the linked list.

        Raises:
            TypeError: If the value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


"""A class SinglyLinkedList that defines a singly linked list"""


class SinglyLinkedList:
    """A class that defines a singly linked list.

    Attributes:
        head (Node or None): The head node of the linked list.
    """
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
        """Inserts a new node into the sorted position in the linked list.

        Args:
            value (int): The data to be stored in the new node.
        """
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
