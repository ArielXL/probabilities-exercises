from queue import Queue

def GetGraph(graph, node):

    new_graph = [[] for _ in range(node)]

    for i in range(len(graph)):
        t = graph[i]
        
        if isinstance(t, tuple):        
            u, v = t[0], t[1]
            new_graph[u].append(v)
            new_graph[v].append(u)

    return new_graph

def BFS(graph, u):
    queue = Queue()
    visited = [ False, False, False, False, False ]
    queue.put(u)
    visited[u] = True

    while not queue.empty():
        elem = queue.get()
        for v in graph[elem]:
            if not visited[v]:
                visited[v] = True
                queue.put(v)

    return visited

def IsConnected(g, node):
    
    graph = GetGraph(g, node)
    visited = BFS(graph, 0)
    
    count = 0
    for i in range(len(visited)):
        if visited[i]:
            count += 1

    return count == len(visited)

def GetDiameter(cost):

    diameter = -1

    for i in range(len(cost)):
        for j in range(len(cost[i])):
            if diameter < cost[i][j] and cost[i][j] < 10000:
                diameter = cost[i][j]

    return diameter

def PrintMatrix(cost):
    print('COSTO')
    for i in range(len(cost)):
        print(cost[i])

def PrintGraph(graph):
    print('GRAFO')
    for i in range(len(graph)):
        t = graph[i]
        if isinstance(t, tuple):        
            u, v = t[0], t[1]
            print(f'{u} <--> {v}')