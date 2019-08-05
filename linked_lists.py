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

def return_kth_to_last(list, k):
  # find element where count to next == None equals k?
  # bad solution O(n^2)
  # n = list.head
  # count = 0

  # while n != None:
  #   n2 = n
  #   while n2 != None:
  #     if count == k:
  #       return n
  #     count += 1
  #     n2 = n2.next

  #   count = 0
  #   n = n.next

  # iterative solution O(n) time, O(1) space
  p1 = list.head
  p2 = list.head

  count = 0
  while p1 != None:
    if count == k:
      break
    count += 1
    p1 = p1.next

  while p1 != None:
    p1 = p1.next
    p2 = p2.next
  
  return p2