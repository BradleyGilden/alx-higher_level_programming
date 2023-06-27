#!/usr/bin/python3

"""
This module contains a singly linked list implemented in python

Author: Bradley Dillion Gilden
Date: 27-06-2023
"""


class Node:
    """Node - this class is responsible for creating new instances of nodes
    to add to the list
    Attributes(instance):
        @private
        data(int): node data
        next_node(Node): reference to next node in list
    """
    def __init__(self, data, next_node=None):
        """__init__ - Node constructor
        Args:
            new_node(Node): reference to next node in list (optional)
            data(int): data assigned to new node"""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """getter method for node data"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter method for node data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter method for node reference"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter method for node reference"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList - contains methods that manipulate a singly linked list
    Attributes(instance):
        @private
        head(Node) = reference to beginning of linked list
    """
    def __init__(self):
        """__init__ - constructor, initialises head reference"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts new node in sorted list
        Args:
            value(int): int data to be added to newly inserted node"""
        n_node = Node(value)
        if n_node is None:
            return
        if self.__head is None:
            self.__head = n_node
            return
        ptr = self.__head
        count = 0
        while ptr is not None:
            if value < ptr.data and count == 0:
                n_node.next_node = self.__head
                self.__head = n_node
                return
            elif ptr.next_node is not None and value >= ptr.data\
                    and value < ptr.next_node.data:
                n_node.next_node = ptr.next_node
                ptr.next_node = n_node
                return
            elif ptr.next_node is None and value >= ptr.data:
                ptr.next_node = n_node
                return
            count += 1
            ptr = ptr.next_node

    def __str__(self):
        """used to print list data line by line"""
        ptr = self.__head
        while ptr is not None:
            if ptr.next_node is not None:
                print(ptr.data)
            else:
                print(ptr.data, end="")
            ptr = ptr.next_node
        return ""
