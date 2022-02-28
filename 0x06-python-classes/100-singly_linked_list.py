#!/usr/bin/python3
""" Define node class """


class Node:
    """ Initialize Node """
    def __init__(self, data, next_node=None):

        if isinstance(data, int):
            self.data = data
        else:
            raise TypeError("data must be an integer")
        if isinstance(next_node, Node) or next_node is None:
            self.next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    """ getter """
    @property
    def data(self):
        return self.__data

    """ setter """
    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    """ getter for next node """
    @property
    def next_node(self):
        return self.__next_node

    """ setter note to priv """
    @next_node.setter
    def next_node(self, value):
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

""" Define class single list """


class SinglyLinkedList:
    """ initializer for list """
    def __init__(self):
        self.__head = None

    """ inserts node """
    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value, None)
        elif value <= self.__head.data:
            new = Node(value, self.__head)
            self.__head = new
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data <= value:
                tmp = tmp.next_node
            nex = tmp.next_node
            tmp.next_node = Node(value, nex)

    """ makes list """
    def __str__(self):
        tmp = self.__head
        p = ''
        while tmp is not None:
            p = p + str(tmp.data) + '\n'
            tmp = tmp.next_node
        return p[:-1]
