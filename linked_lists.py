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

def delete_middle_node(node):
  # not the solution, don't have access to head
  # n = list.head

  # while n != None:
  #   if n != list.head and n == node:
  #     prev.next = n.next

  # prev = n
  # n = n.next

  if node == None or node.next == None:
    return False

  # copy data from next node onto the current node
  n = node.next
  node.data = n.data
  node.next = n.next
  return True

def partition(list, x):
  # my answer, almost, but not quite, doesn't put lesser values at head, and greater values at tail to ensure partition
  # n = list.head
  # while n != None:
  #   if n.data < x:
  #     n.next = n
  
  # correct answer
  n = list.head
  while n != None:
    if n.data < x:
      list.head.next = list.head
      list.head = n
    else:
      n.append_to_tail(n.data)

def sum_lists(l1, l2):
  n1 = l1.head
  n2 = l2.head

  while n1 != None:
    if n2 == None:
      return False
    s = n1.data + n2.data
    l3 = LinkedList(Node(s))
    n3 = l3.head
    if s > 9:
      if n1.next != None:
        s = s - 10
        n3.next = Node(s)
        n1.next.data += 1
      else:
        s = s - 10
        n3.next = Node(s)
        n1.next = Node(1)
        n2.next = Node(0)
    else:
      n3.next = Node(s)
      n1 = n1.next
      n2 = n2.next
      n3 = n3.next

  n3 = l3.head
  sum_list = []
  while n3 != None:
    sum_list.append(n3.data)
    n3 = n3.next

  sum_list.reverse()
  sum_str = ''.join(map(str, sum_list))
  return sum_str

def is_palindrome(l):
  # not in the spirit of the question asked i think
  # n = l.head
  # str = []

  # while n != None:
  #   str.append(n.data)
  #   n = n.next
  
  # if str == str.reverse():
  #   return True
  # else:
  #   return False

  # copy and reverse the list and compare
  n = l.head
  l2 = LinkedList(Node(None))

  while n != None:
    # copy of current node
    node = Node(n.data)
    # reversing
    node.next = l2.head
    l2.head = node
    # iterating through first list
    n = n.next
  
  n1 = l.head
  n2 = l2.head

  while n1 != None and n2 != None:
    if n1.data != n2.data:
      return False
    n1 = n1.next
    n2 = n2.next
  return n1 == None and n2 == None

def intersection(l1, l2):
  n1 = l1.head
  n2 = l2.head

  c1 = 0
  c2 = 0

  while n1 != None:
    t1 = n1
    c1 += 1
    n1 = n1.next

  while n2 != None:
    t2 = n2
    c2 += 1
    n2 = n2.next

  # check if lengths are the same, if not truncate longer lists' head
  if c1 != c2:
    if c1 > c2:
      diff = c1 - c2
      n1 = l1.head
      count = 0
      while count < diff:
        l1.head = n1.next
        count += 1
        n1 = n1.next
    else:
      diff = c2 - c1
      n2 = l2.head
      count = 0
      while count < diff:
        l2.head = n2.next
        count += 1
        n2 = n2.next

  if t1 != t2:
    return False
  else:
    n1 = l1.head
    n2 = l2.head
    while n1 != None:
      if n1.data == n2.data:
        return n1
      n1 = n1.next
      n2 = n2.next

def loop_detection(l):
  # set both slowrunner (one step at a time) and fastrunner (two steps at a time)
  slow = l.head
  fast = l.head

  while fast != None and fast.next != None:
    # step through until there is a collision
    slow = slow.next
    fast = fast.next.next
    # if there is a collision, break out
    if slow == fast:
      break
  
  # if there is no meeting point, therefore no loop
  if fast == None or fast.next == None:
    return None
  
  # set slow to head, keep fast at collision point
  # if they move at same pace they will meet at loop start
  # because 

  slow = l.head
  while slow != fast:
    slow = slow.next
    fast = fast.next
  
  # the start of the loop
  return fast