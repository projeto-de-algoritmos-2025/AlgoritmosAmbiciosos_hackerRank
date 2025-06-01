#!/bin/python3
#pesos

import math
import os
import random
import re
import sys

def main():
    road_nodes, road_edges = map(int, sys.stdin.readline().split())

    road_from = []
    road_to = []
    road_weight = []

    for _ in range(road_edges):
        u, v, w = map(int, sys.stdin.readline().split())
        road_from.append(u)
        road_to.append(v)
        road_weight.append(w)

    n = road_nodes
    INF = 10**18
    distance = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        distance[i][i] = 0

    for i in range(road_edges):
        u = road_from[i]
        v = road_to[i]
        w = road_weight[i]
        if w < distance[u][v]:
            distance[u][v] = w

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    q = int(sys.stdin.readline())
    for _ in range(q):
        x, y = map(int, sys.stdin.readline().split())
        if distance[x][y] == INF:
            print(-1)
        else:
            print(distance[x][y])

if __name__ == '__main__':
    main()