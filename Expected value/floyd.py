from utils import PrintMatrix, PrintGraph

# graph es una tupla de tuplas
def Floyd(graph, node):

    infinito = 10000
    cost = []
    for _ in range(node):
        cost.append([0,0,0,0,0])

    for i in range(node):
        for j in range(node):
            cost[i][j] = infinito

    for i in range(len(graph)):
        t = graph[i]
        
        if isinstance(t, tuple):        
            u, v = t[0], t[1]

            cost[u][v] = 1
            cost[v][u] = 1

    for i in range(node):
        cost[i][i] = 0

    for k in range(node):
        for i in range(node):
            for j in range(node):
                if cost[i][k] + cost[k][j] < cost[i][j]:
                    cost[i][j] = cost[i][k] + cost[k][j]

    return cost
