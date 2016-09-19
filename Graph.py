#  File: Graph.py

#  Description: Creates a graph from an input

#  Student's Name: Bella Shah

#  Student's UT EID: BHS533

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: May 5, 2016

#  Date Last Modified: May 7, 2016
import copy

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if vertex was visited
  def wasVisited (self):
    return self.visited 

  # determine the label of the vertex
  def getLabel (self):
    return self.label

  # string representation of the label
  def __str__(self):
    return str (self.label)

class Edge (object):
  def __init__ (self, fromVertex, toVertex, weight=1):
    self.u = fromVertex
    self.to = toVertex
    self.weight = weight

  # comparison operators
  def __lt__ (self, other):
    return self.weight < other.weight

  def __le__ (self, other):
    return self.weight <= other.weight
  
  def __gt__ (self, other):
    return self.weight > other.weight
  
  def __ge__ (self, other):
    return self.weight >= other.weight
  
  def __eq__ (self, other):
    return self.weight == other.weight
  
  def __ne__ (self, other):
    return self.weight != other.weight
  
class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []
    self.Edges = []

  # checks if a vertex label already exists
  def hasVertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).label):
        return True
    return False
  
  # check if a edge already exists
  def hasEdge(self, edge):
    for entry in self.Edges:
      if entry.u == edge.u and entry.to == edge.to:
        return True
    return False

  # add a vertex with given label
  # create adjmat
  def addVertex (self, label):
    if not self.hasVertex (label):
      self.Vertices.append (Vertex (label))

      # add a new column in the adjacency matrix for new Vertex
      nVert = len (self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append (0)
    
      # add a new row for the new Vertex in the adjacency matrix
      newRow = []
      for i in range (nVert):
        newRow.append (0)
      self.adjMat.append (newRow)

  # add weighted directed edge to graph
  def addDirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.Edges.append(Edge(start, finish))
    

  # add weighted undirected edge to graph
  def addUndirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight
    self.Edges.append(Edge(start, finish))

  # return an unvisited vertex adjacent to v
  def getAdjUnvisitedVertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
        return i
    return -1

  # stack is empty reset the flags
  def flagReset(self):    
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False
      
  # does a depth first search in a graph
  def dfs (self, v):
    self.flagReset()
    # create a stack
    theStack = Stack()

    # mark the vertex as visited and push on the stack
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theStack.push (v)

    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex (theStack.peek())
      if (u == -1):
        u = theStack.pop() 
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push(u)
        
    
    
  # does a breadth first search in a graph
  def bfs (self, v, flag = True):
    self.flagReset()
    # create a queue
    theQueue = Queue ()

    # mark the vertex as visited and enqueue
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theQueue.enqueue (v)

    while (not theQueue.isEmpty()):
      # get the vertex at the front
      v1 = theQueue.dequeue()
      # get an adjacent unvisited vertex
      v2 = self.getAdjUnvisitedVertex (v1)
      while (v2 != -1):
        (self.Vertices[v2]).visited = True
        print (self.Vertices[v2])
        theQueue.enqueue (v2)
        v2 = self.getAdjUnvisitedVertex (v1)
    if flag == True:  
      self.flagReset()

      
# get index from vertex label
  def getIndex (self, label):
    for i in range(len(self.Vertices)):
      if self.Vertices[i].label == label:
        return i
    return -1
    
  # get edge weight between two vertices
  # return -1 if edge does not exist
  def getEdgeWeight (self, fromVertexLabel, toVertexLabel):
    u = self.getIndex(fromVertexLabel)
    to = self.getIndex(toVertexLabel)
    if u >= 0 and to >=0:      
      if self.adjMat[u][to] > 0:
        return self.adjMat[u][to]
      else:
        return -1
    else:
      return -1
  
  # get a list of neighbors that you can go to from a vertex
  # return empty list if there are none
  def getNeighbors (self, vertexLabel):
    neighbor_list = []
    u = self.getIndex(vertexLabel)
    if u >= 0:
      for j in range(len(self.adjMat[u])):
        if self.adjMat[u][j] != 0:
          neighbor = self.Vertices[j].label
          neighbor_list.append(neighbor)
      return neighbor_list
    else:
      return neighbor_list # just return the empty list
    
  # get a copy of the list of vertices
  def getVertices (self):
    copied_vertices_list = []
    for entry in self.Vertices:
      copied_vertices_list.append(entry)
    return copied_vertices_list
  
# determine if the graph has a cycle
  def hasCycle (self):
    nVert = len (self.Vertices)
    visited_list = []
    # create a stack
    theStack = Stack()
    # mark the vertex as visited and push on the stack
    (self.Vertices[0]).visited = True
    theStack.push (0)# argument is an index.
    
    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex (theStack.peek())   
      if (u == -1):
        u = theStack.pop()       
      else:
        for i in range (nVert):
          if (self.adjMat[u][i] > 0) and (i in theStack.stack):
             self.flagReset()
             return True
        (self.Vertices[u]).visited = True
        theStack.push(u)
        visited_list.append(u)
        
    self.flagReset()
    
    return False

  def isConnected_undirect(self,v):
    self.bfs(v,False)
    for entry in self.Vertices:
      if entry.visited == False:
        return False
    return True
  
  def isSingle_direct(self):
    v_set = set()
    for entry in self.Edges:
      v_set.add(entry.u)
      v_set.add(entry.to)
    print( len(v_set))
    print(len(self.Vertices))

    return len(v_set) == len(self.Vertices)
       
  # return a list of vertices after a topological sort
  def toposort (self):
    copymat = copy.deepcopy(self.adjMat)
    for entry in self.adjMat:
      for en in entry:
        print(en, end = ' ')
      print()
    start_list = []

    nVert = len (self.Vertices)
    for i in range(nVert):
      start_flag = True
      for j in range(nVert):
        if (self.adjMat[j][i] != 0):
          start_flag = False
          break
      if start_flag == True:
        start_list.append(i)
    print(start_list)
        
    topo_list = []
    theStack = Stack()
    for idx in start_list:
      theStack.push(idx)
      while (not theStack.isEmpty()):
        u = self.getAdjUnvisitedVertex (theStack.peek())
        if (u != -1):
          theStack.push(u)
        else:
          no_succ_index = theStack.pop()      
          (self.Vertices[no_succ_index]).visited = True
          topo_list.append(self.Vertices[no_succ_index].label)

    for i in range (nVert):
      (self.Vertices[i]).visited = False
    topo_list.reverse() 
    return topo_list
    
  def spanTree (self, start):
    start_index = self.getIndex(start)
    span_tree = []
    span_vertice = [start_index]
    while(len(span_vertice) < len(self.Vertices)):
      fr_index, to_index = self.getBranches(span_vertice)
      path_string = str(self.Vertices[fr_index].label) + " - " + str(self.Vertices[to_index].label)
      span_tree.append(path_string)
    return span_tree
  
  def getBranches(self, cur_vert_list):  
      for entry in Edge_list:
        if entry[0] in cur_vert_list and entry[1] not in cur_vert_list:
          cur_vert_list.append(entry[1])
          Edge_list.remove(entry)
          return entry[0], entry[1]
  
  def shortestPath_single(self, fromVertexLabel, toVertexLabel):
    pass
  
  # determine shortest path from a single vertex
  # to all other vertex.
  # another way to do this is to call shortestPath_single multi times
  def shortestPath (self, fromVertexLabel):
  
    start_idx = self.getIndex(fromVertexLabel)
    nVert = len (self.Vertices)
    graph_dict = {}
    for i in range(nVert):
      toVert_idx_list = []
      for j in range(nVert):
        if self.adjMat[i][j] != 0:
          toVert_idx_list.append(j)
      graph_dict[i] = toVert_idx_list
    for i in range(nVert):
      target_paths = self.find_all_paths(graph_dict, start_idx, i) # get all possible path from start to target
      if target_paths == []: # no path found, it is unreachable from the start
        print(self.Vertices[i].label + ' - unreachable')     
      else:
        cost_list = []
        for single_path in target_paths:
          if len(single_path) == 1:
            cost_list.append(0)
          else:
            path_cost = 0
            for j in range(len(single_path)-1):
              path_cost += self.adjMat[single_path[j]][single_path[j+1]]
            cost_list.append(path_cost)
        min_cost = min(cost_list)
        print(self.Vertices[i].label + ' - ' + str(min_cost))  
              
  def find_all_paths(self,graph_d, start, end, path=[]):
    path = path + [start]
    if start == end:
      return [path]
    if not start in graph_d:
      return []
    paths = []
    for node in graph_d[start]:
      if node not in path:
        newpaths = self.find_all_paths(graph_d, node, end, path)
        for newpath in newpaths:
          paths.append(newpath)
    return paths
  
  # delete an edge from the adjacency matrix
  def deleteEdge (self, fromVertexLabel, toVertexLabel):
    u = self.getIndex(fromVertexLabel)
    to = self.getIndex(toVertexLabel)
    if u >= 0 and to >=0:
      self.adjMat[u][to] = 0      
    else:
      return
    
  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  def deleteVertex (self, vertexLabel):
    targetVIndex = self.getIndex(vertexLabel)
    if targetVIndex >= 0:
      for entry in self.Vertices:
        if vertexLabel == entry.label:
          self.Vertices.remove(entry)    
      for i in range(len(self.adjMat)):
        del self.adjMat[i][targetVIndex]      
      del self.adjMat[targetVIndex]     
    else:
      return

def main():
  # Creates Graph object
  city = Graph()

  # Opena file for reading
  inFile = open ("./graph.txt", "r")

  numVertices = int ((inFile.readline()).strip())
  print(numVertices)
  
  for i in range (numVertices):
    vertex = (inFile.readline()).strip()
    city.addVertex (vertex)

  numEdges = int ((inFile.readline()).strip())
  global Edge_list
  Edge_list = []
  for i in range (numEdges):
    edge = (inFile.readline()).strip()
    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])
    city.addDirectedEdge (start, finish, weight)
    Edge_list.append([start,finish,weight])
  Edge_list.sort(key = lambda column: (column[2])) 
  
  startVertex = (inFile.readline()).strip()
  # Closes file
  inFile.close()
  
 
  startIndex = city.getIndex(startVertex)
  # test depth first search
  print ("Depth First Search from",startVertex)
  city.dfs (startIndex)
  print()

  # test breadth first search
  print ("Breadth First Search from",startVertex)
  city.bfs (startIndex)
  print()

  output = []
  if(not city.hasCycle()):
    # test topological sort
    print ("Topological Sort")
    output = city.toposort()
  else:
    # test minimum cost spanning tree
    print("Minimum Cost Spanning Tree from", startVertex)
    output = city.spanTree(startVertex)
    
  for l in output:
    print(l)
  print()

  # test single source shortest path algorithm
  print("Shortest Path from",startVertex)
  city.shortestPath(startVertex)

  print(city.isSingle_direct())
  
main()