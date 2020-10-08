"""
============================================================================
Implementation Exercise: Singly Linked List
============================================================================

-------
Phase 1:
-------
1. Node and LinkedList initialization
2. Getting a node by its position
3. Adding a node to the list's tail
4. Adding a node to list's head
5. Removing the head node
6. Removing the tail node
7. Returning the list length

-------
Phase 2:
-------

1. Check whether the list contains_value a value
2. Inserting a node value into the list at a specific position
3. Updating a list node's value at a specific position
4. Removing a node value from the list at a specific position
5. Format the list as a string whenever `print()` is invoked
"""

# Phase 1

# TODO: Implement a Linked List Node class here


class Node:
    # TODO: Set the `_value` `_next` node instance variables
    def __init__(self, value):
        self._value = value
        self._next = None


# TODO: Implement a Singly Linked List class here
class LinkedList:
    # TODO: Set the `_head` node, `_tail` node, and list `_length` instance variables
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    # TODO: Implement the get_node method here
    def get_node(self, position):
        if (not self._head or not self._tail):
            return Node(None)
        if(position > self._length):
            return Node(None)

        curr_node = self._head
        count = 0
        while curr_node:
            if(count is position):
                return curr_node
            curr_node = curr_node._next
            count += 1

    # TODO: Implement the add_to_tail method here

    def add_to_tail(self, value):
        new_node = Node(value)
        if (self._head is None and self._tail is None):
            self._head = new_node
            self._tail = new_node
            self._length += 1
            return new_node._value
        curr_tail = self._tail
        curr_tail._next = new_node
        self._tail = new_node
        self._length += 1
        return new_node._value

    # TODO: Implement the add_to_head method here
    def add_to_head(self, value):
        new_node = Node(value)
        if(self._head is None):
            self._head = new_node
            self._length += 1
            self._tail = new_node
            return new_node._value
        curr_head = self._head
        new_node._next = curr_head
        self._head = new_node
        self._length += 1
        return new_node._value

    # TODO: Implement the remove_head method here
    def remove_head(self):
        curr_val = self._head._value
        if (not self._head or not self._tail):
            return 'List is empty'
        if self._length == 1:
            self._head = None
            self._tail = None
            self._length -= 1
            return curr_val
        new_head = self._head._next
        self._head._next = None
        self._head = new_head
        self._length -= 1
        return curr_val

    # TODO: Implement the remove_tail method here
    def remove_tail(self):
        if not self._head:
            return 'their isn\'t any data'
        if (self._length == 1):
            curr_node = self._head
            self._head = None
            self._tail = None
            self._length -= 1
            return curr_node
        x = self.get_node(self._length-2)
        y = self._tail
        x._next = None
        self._tail = x
        self._length -= 1
        return y._value

    # TODO: Implement the __len__ method here

    def __len__(self):
        return self._length

# Phase 2

    # TODO: Implement the contains_value method here
    def contains_value(self, target):
        def checker(target, current=self._head):
            if (not current._next):
                return False
            if (current._value == target):
                return True
            else:
                return checker(target, current._next)

        return checker(target)
    # TODO: Implement the insert_value method here

    def insert_value(self, position, value):
        new_node = Node(value)
        x = self.get_node(position)
        y = self.get_node(position+1)
        if(x and y):
            x._next = new_node
            new_node._next = y
            self._length += 1
            return new_node
        return 'Invalid position argument'

    # TODO: Implement the update_value method here

    def update_value(self, position, value):
        x = self.get_node(position)
        x._value = value
        return x

    # TODO: Implement the remove_node method here
    def remove_node(self, position):
        to_be_deleted = self.get_node(position)
        prev_node = self.get_node(position-1)
        next_node = to_be_deleted._next
        to_be_deleted._next = None
        prev_node._next = next_node
        return to_be_deleted

    # TODO: Implement the __str__ method here
    def __str__(self):
        return str([self.get_node(i)._value for i in range(self._length)])
# list [val for val in range(self._length)]
# Phase 1 Manual Testing:


# 1. Test Node and LinkedList initialization
node = Node('hello')
print(node)                                     # <__main__.Node object at ...>
print(node._value)                              # hello
linked_list = LinkedList()
# <__main__.LinkedList object at ...>
print(linked_list._head)
linked_list.add_to_head('something else')
linked_list.add_to_head('water')
linked_list.add_to_head('node')
linked_list.add_to_head('fire')
linked_list.add_to_head('stone')
print(str(linked_list))
print(len(linked_list))
