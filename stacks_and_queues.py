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

  