# route between nodes: given a directed graph, design an algorithm
# to find out whether there is a route between two nodes
# breadth

# an iterative implementation of breadth-first search
def search(g, start, end):
  if start == end:
    return True

  # operates as queue
  q = LinkedList()

  for u in g.get_nodes():
    u.state = 'unvisited'
  
  start.state = 'visiting'
  q.add(start)
  u = Node()
  while not q.is_empty():
    u = q.remove_first()
    if u != None:
      for v in u.get_adjacent():
        if v.state == 'unvisited':
          if v == end:
            return True
          else:
            v.state = 'visiting'
            q.add(v)
      
      u.state = 'visited'

  return False