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
    return self.top
  
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

# extend classes to track minimum
class StackMin(Stack):
  def push(self, data):
    newMin = min(data, self.minimum())
    super().push(NodeMin(data, newMin))

  def minimum(self):
    if self.is_empty():
      return 'error'
    else:
      return self.peek().minimum

class NodeMin(StackNode):
  def __init__(self, v, minimum):
    self.data = v
    self.minimum = minimum

# better solution: use additional stack which keeps track of mins
class StackMin2(Stack):
  def __init__(self, s2):
    self.s2 = Stack(s2)

  def push(self, data):
    if data <= self.minimum():
      self.s2.push(data)
    super().push(data)

  def pop(self):
    value = super().pop()
    if value == self.minimum():
      self.s2.pop()
    return value

  def minimum(self):
    if self.s2.is_empty():
      return 'error'
    else:
      return self.s2.peek()

# Stack of Plates: implement a set of stacks data structure that creates a new stack
# once the previous one exceeds capacity

class SetOfStacks:
  def __init__(self, capacity):
    self.capacity = capacity
    self.stacks = []

  def get_last_stack(self):
    if len(self.stacks) == 0:
      return None
    return self.stacks[-1]

  def push(self, data):
    last = self.get_last_stack()
    if last != None and not last.is_full():
      last.push(data)
    else:
      stack = SetStack(self.capacity)
      stack.push(data)
      stacks.add(stack)
    
  def pop(self):
    last = self.get_last_stack()
    if last == None:
      return 'error'
    v = last.pop()
    if len(last) == 0:
      self.stacks.pop(-1)
    return v

  def is_empty(self):
    last = self.get_last_stack()
    return last == None or last.is_empty()

  def pop_at(self, index):
    return left_shift(index, True)

  def left_shift(self, index, remove_top):
    stack = self.stacks[index]
    if (remove_top):
      removed_item = stack.pop()
    else:
      removed_item = stack.remove_bottom()
    
    if stack.is_empty():
      self.stacks.pop(index)
    elif len(self.stacks) > index + 1:
      v = left_shift(index + 1, False)
      stack.push(v)
    
    return removed_item

class SetStack:
  def __init__(self, capacity):
    self.capacity = capacity
    self.size = 0
    self.bottom = None
    self.top = None

  def is_full(self):
    return self.capacity == self.size

  def join(self, above, below):
    if below != None:
      below.above = above
    if above != None:
      above.below = below

  def push(self, data):
    if self.size >= self.capacity:
      return False
    self.size += 1
    n = StackNode(data)
    if self.size == 1:
      self.bottom = n
    self.join(n, top)
    self.top = n
    return True

  def pop(self):
    t = self.top
    top = top.below
    size -= 1
    return t.data

  def is_empty(self):
    return self.size == 0

  def remove_bottom(self):
    b = self.bottom
    self.bottom = bottom.above
    if self.bottom != None:
      bottom.below = None
    self.size -= 1
    return b.data

# Implement a queue via stacks
# newest items go in 1st stack, when you want to remove an item
# shift all items to second stack, pop first item, the 'oldest' item

class MyQueue:
  def __init__(self):
    stack_newest = Stack()
    stack_oldest = Stack()

  def size(self):
    return len(self.stack_newest) + len(self.stack_oldest)

  def add(self, value):
    # push onto new stack, where the newest elements are on top
    self.stack_newest.push(value)

  def shift_stacks(self):
    if self.stack_oldest.is_empty():
      while not self.stack_oldest.is_empty():
        self.stack_oldest.push(stack_newest.pop())

  def peek(self):
    self.shift_stacks()
    return self.stack_oldest.peek()

  def remove(self):
    self.shift_stacks()
    return self.stack_oldest.pop()


# Implement a sort function that sorts a stack such that the smallest
# items are on the top

class SortStack(Stack):
  def sort(self, s):
    r = Stack()
    while not s.is_empty():
      tmp = s.pop()
      while not r.is_empty() and r.peek() > tmp:
        s.push(r.pop())
      r.push(tmp)

    while not r.is_empty():
      s.push(r.pop())

# Animal Shelter: queue where people can choose to either adopt 'oldest' pet,
# 'oldest' dog, or 'oldest' cat

class Animal:
  def __init__(self, n):
    self.name = n

  def set_order(self, order):
    self.order = order

  def get_order(self):
    return self.order

  def is_older_than(self, a):
    return self.order < a.get_order()


    
class AnimalQueue:
  def __init__(self)
  