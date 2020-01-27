import sys


class Edge:
    def __init__(self, src, destination, wt):
        self.src = src
        self.destination = destination
        self.wt = wt


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, v1, v2, w):
        self.adj_matrix[v1][v2] = w
        self.adj_matrix[v2][v1] = w

def prims(vertices, ad_matrix):
    visited = [False for _ in range(vertices)]
    parent = [-1 for _ in range(vertices)]
    weight = [sys.maxsize for _ in range(vertices)]
    for i in range(vertices - 1):
        min_vertex = get_min_vertex(vertices, visited, weight)
        visited[min_vertex] = True
        for j in range(vertices):
            if ad_matrix[min_vertex][j] > 0 and visited[j] is False:
                if weight[j] > ad_matrix[min_vertex][j]:
                    weight[j] = ad_matrix[min_vertex][j]
                    parent[j] = min_vertex
    for i in range(1, vertices):
        if i < parent[i]:
            print(str(i) + " " + str(parent[i]) + " " + str(weight[i]))
        else:
            print(str(parent[i]) + " " + str(i) + " " + str(weight[i]))


def get_min_vertex(vertices, visited, weight):
    min_vertex = -1
    for i in range(vertices):
        if visited[i] is False and (min_vertex == -1 or weight[min_vertex] > weight[i]):
            min_vertex = i
    return min_vertex


li = [int(x) for x in input().split()]
v = li[0]
e = li[1]
g = Graph(v)
for i in range(e):
    curr_inp = [int(x) for x in input().split()]
    g.add_edge(curr_inp[0], curr_inp[1], curr_inp[2])

prims(v, g.adj_matrix)
