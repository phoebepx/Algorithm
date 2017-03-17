# coding:utf-8
# created by Phoebe_px on 2017/3/16
#def a undirected graph
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

#Connected Component
    #DFS
        #use stack
def dfs_norecursion(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited
        #use recursion
def dfs_recursion(graph,start,visted = None):
    if visted ==None:
        visted = set()
    visted.add(start)
    for next in graph[start]-visted:
        dfs_recursion(graph,next,visted)
    return visted
    #BFS
def bfs(graph,start):
    visited,queue = set(),[start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex]-visited)
    return visited
#Test
print(dfs_norecursion(graph,'A'))   #{'E', 'F', 'A', 'C', 'D', 'B'}
print(dfs_recursion(graph,'A'))     #{'E', 'F', 'A', 'D', 'C', 'B'}
print(bfs(graph,'A'))               #{'E', 'F', 'A', 'C', 'D', 'B'}

#Generate paths from start to goal
    #dfs using stack
def dfs_paths_stack(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

    #dfs using recursion
def dfs_paths_recursion(graph,start,goal,path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths_recursion(graph, next, goal, path + [next])

    #bfs
        # using queue
def bfs_paths_queue(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))
    #bfs
        # using deque
from collections import deque
def bfs_paths_deque(graph, start, goal):
    queue = deque([(start,[start])])
    while queue:
        vertex,path= queue.popleft()
        if vertex==goal:
            yield path
        for next in graph[vertex]-set(path):
            queue.extend([(next,path+[next])])

#Test
print(list(dfs_paths_stack(graph, 'A', 'F')))                #[['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
print(list(dfs_paths_recursion(graph,'A','F',path=None)))    #[['A', 'B', 'E', 'F'], ['A', 'C', 'F']]
print(list(bfs_paths_queue(graph,'A','F')))                   #[['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
print(list(bfs_paths_deque(graph,'A','F')))                   #[['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
#shortest_path
def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths_deque(graph, start, goal))
    except StopIteration:
        return None
print(shortest_path(graph, 'A', 'F'))  # ['A', 'C', 'F']













