from floyd import Floyd
from generate_graph import GenerateGraph
from utils import GetDiameter, PrintMatrix, PrintGraph, IsConnected


def main():

    node = 5
    all_graph = GenerateGraph()
    diameters = [0, 0, 0, 0, 0]
    count_graph = 1
    count_connected_graph = 0
    valor_esperado = 0

    for _all_graph in all_graph:
        count_graph += len(_all_graph)
        for graph in _all_graph:
            if IsConnected(graph, node):
                count_connected_graph += 1
                cost = Floyd(graph, node)
                diameter = GetDiameter(cost)
                diameters[diameter] += 1

    for i in range(1, len(diameters)):
        valor_esperado += i * diameters[i] / count_connected_graph

    print(f'CANTIDAD DE GRAFOS CONEXOS = {count_connected_graph}')
    print(f'CANTIDAD DE GRAFOS EN TOTAL = {count_graph}')
    print(f'VALOR ESPERADO = {round(valor_esperado, 5)}')

    # print(diameters)


if __name__ == '__main__':
    main()
