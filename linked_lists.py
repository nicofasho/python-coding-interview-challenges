class Node:
  def __init__(self, data):
    self.next = None
    self.data = data
    return

  def append_to_tail(self, d):
    end = Node(d)
    n = self
    while n.next != None:
      n = n.next
    n.next = end
    return

class LinkedList:
  def __init__(self, head):
    self.head = head
    return

def delete_node(head, d):
  n = head

  if n.data == d:
    return head.next
  
  while n.next != None:
    if n.next.data == d:
      n.next = n.next.next
      return head
    n = n.next

  return head

def remove_dupes(list):
  # go through linked list til n == None
  # add Nodes to list, use in keyword to check if data exists already

  n = list.head
  nodes = []

  while n != None:
    if n.data in nodes:
      prev.next = n.next
    else:
      nodes.append(n.data)
      prev = n
    n = n.next