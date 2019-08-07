class Stack:
  def __init__(self, top_node):
    self.top = StackNode(top_node)

  def pop(self): 
    if self.top == None:
      return False
    else:
      item = self.top.data
      top = self.top.next
      return item

  def push(self, item):
    t = StackNode(item)
    t.next = self.top
    self.top = t

  def peek(self):
    if self.top == None:
      return False
    return self.top.data
  
  def is_empty(self):
    return self.top == None

class StackNode:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.first = None
    self.last = None
  
  # add item to end of the list
  def add(self, item):
    t = QueueNode(item)
    if self.last != None:
      self.last.next = t
    self.last = t

    if self.first == None:
      self.first = self.last

  #remove first item in the list
  def remove(self):
    if self.first == None:
      return False
    
    data = first.data
    self.first = self.first.next
    if self.first == None:
      self.last = None

    return data

  def peek(self):
    if self.first == None:
      return False
    return self.first.data

  def is_empty(self):
    return self.first == None

class QueueNode:
  def __init__(self, data):
    self.data = data
    self.next = None

# Three in one: describe how you could use a single array to implement three stacks  
# Stack 1 starts at index 0, Stack 2 at 1, Stack 3 at 2
# If data is pushed into stack 1, shift all other stacks up one index, if data is popped from stack 1, shift all other stacks down one index
# or use Python insert at 0 for stack 1, len(stack1) for stack 2, and len(stack1) + len(stack2) for stack 3
# solution from book:

class FixedMultiStack:
  def __init__(self, stack_size):
    self.number_of_stacks = 3
    self.stack_capacity = stack_size
    self.values = []
    for i in stack_capacity * number_of_stacks:
      self.values.append(None)
    self.sizes = []
    for i in number_of_stacks:
      self.sizes.append(0)
  
  def push(self, stack_num, value):
    self.sizes[stack_num] += 1
    self.values[self.index_of_top(stack_num)] = value

  def pop(self, stack_num):
    if self.is_empty(stack_num):
      self.empty_stack_exception()
    
    top_index = self.index_of_top(stack_num)
    value = self.values[top_index]
    self.values[top_index] = 0
    self.sizes[stack_num] -= 1
    return value

  def peek(self, stack_num):
    if is_empty(stack_num):
      self.empty_stack_exception()
    
    return self.values[self.index_of_top(stack_num)]

  def is_empty(self, stack_num):
    return self.sizes[stack_num] == 0

  def is_full(self, stack_num):
    return self.sizes[stack_num] == self.stack_capacity

  def index_of_top(self, stack_num):
    offset = stack_num * self.stack_capacity
    size = self.sizes[stack_num]
    return offset + size - 1

  def empty_stack_exception(self):
    pass

# Stack min, design a stack which in addition to push and pop, has a function
# min which returns the minimum element, push pop and min should operate
# in O(1) time

class StackMin:
  def __init__(self, top_node):
    self.top = StackMinNode(top_node)

  def pop(self): 
    if self.top == None:
      return False
    else:
      item = self.top.data
      self.top = self.top.next
      return item

  def push(self, item):
    t = StackMinNode(item, min(item.data, self.min()))
    t.next = self.top
    self.top = t

  def peek(self):
    if self.top == None:
      return False
    return self.top.data
  
  def is_empty(self):
    return self.top == None

  def min(self):
    return peek().min

class StackMinNode:
  def __init__(self, data, minimum):
    self.data = data
    self.next = None
    self.min = minimum