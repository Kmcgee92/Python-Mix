

class Node:

  def __init__(self, _value):
    self._value = _value
    self._next = None



class LinkedList:

  def __init__(self):
    self._head = None
    self._tail = None
    self._length = 0


  def get_node(self, position):
    # if(position is 0 and self._length is not 0): return self._head._value
    if(position > self._length): return None
    x = self._head
    count = 0
    while x:
      if(count is position): return x._value
      x = x._next
      count+=1

  def add_to_tail(self, value):
    new_node = Node(value)
    if(self._head is None): 
      self._head = new_node
      self._length+=1
      return
    if(self._tail is None):
      self._head._next = new_node
      self._tail = new_node
      self._length+=1
      return

    self._length+=1
    self._tail._next = new_node
    self._tail = new_node


  def add_to_head(self, value):
    new_node = Node(value)
    if self._head is None:
      self._length+=1
      self._head = new_node
      return self._head._value

    self._length+=1
    new_node._next = self._head
    self._head = new_node
    return self._head._value


  def remove_head(self):
    if not self._head: return 'There is no current Head'
    if not self._tail: 
      self._head = None
      return None

    self._head = self._head._next
    return self._head


  # TODO: Implement the remove_tail method here
  def remove_tail(self):
    if(self._tail is None): return "Can't perform action, there is no tail!"
    x = self._head
    y = self._head._next
    for _ in range(self._length-1):




  # TODO: Implement the __len__ method here

  def __len__(self):
    return self._length

# Phase 2

  # TODO: Implement the contains_value method here
  def contains_value(self, target):
    pass

  # TODO: Implement the insert_value method here
  def insert_value(self, position, value):
    pass

  # TODO: Implement the update_value method here
  def update_value(self, position, value):
    pass

  # TODO: Implement the remove_node method here
  def remove_node(self, position):
    pass

  # TODO: Implement the __str__ method here
  def __str__(self):
    list = []
    x = self._head
    while x:
      list.append(x._value)
      x = x._next
    return str(list)

# Phase 1 Manual Testing:





linked_list = LinkedList()


# # 2. Test getting a node by its position
# print(linked_list.get_node(0))                # None

# # 3. Test adding a node to the list's tail
linked_list.add_to_tail('chess move')
linked_list.add_to_tail('some value')
linked_list.add_to_tail('hamburgers')
# print(linked_list.get_node(0)._value)         # `new tail node`
# print("current head", linked_list._head)



# # 4. Test adding a node to list's head
linked_list.add_to_head('newest head')
print('GET NODE AT HEAD: ',linked_list.get_node(0))  
print('='*40)              # <__main__.Node object at ...>

# print(linked_list.get_node(0))                # <__main__.Node object at ...>
# print(linked_list.get_node(0)._value)         # `new head node`

# print('current tail', linked_list._tail)
# # 5. Test removing the head node
linked_list.remove_head()

# print(linked_list.get_node(0)._value)         # `new tail node` because `new head node` has been removed
# print(linked_list.get_node(1))                # `None` because `new head node` has been removed

# # 6. Test removing the tail node
# print(linked_list.get_node(0)._value)         # `new tail node`
linked_list.remove_tail()
# print(linked_list.get_node(0))                # None

# # 7. Test returning the list length
print(len(linked_list))                                 # 2

# Phase 2 Manual Testing

# # 1. Test whether the list contains_value a value
# linked_list = LinkedList()
# linked_list.add_to_head('new head node')
# print(linked_list.contains_value('new head node'))      # True
# print(linked_list.contains_value('App Academy node'))   # False

# # 2. Test inserting a node value into the list at a specific position
# linked_list.insert_value(0, 'hello!')
# print(linked_list.get_node(0)._value)                   # `hello!`

# # 3. Test updating a list node's value at a specific position
# linked_list.update_value(0, 'goodbye!')
# print(linked_list.get_node(0)._value)                   # `goodbye!`

# # 4. Test removing a node value from the list at a specific position
# print(linked_list.get_node(1)._value)                   # `new head node`
# linked_list.remove_node(1)
# print(linked_list.get_node(1))                          # None

# # 5. Format the list as a string whenever `print()` is invoked
# new_linked_list = LinkedList()
# print(new_linked_list)                  # Empty List
# new_linked_list.add_to_tail('puppies')
# print(new_linked_list)                  # puppies
# new_linked_list.add_to_tail('kittens')
# print(new_linked_list)                  # puppies, kittens


print('whole list of nodes!', str(linked_list))
