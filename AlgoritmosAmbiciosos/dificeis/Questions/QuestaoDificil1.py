import sys
import heapq

def shortest_reach(n, edges, s):
    INF = float('inf')
    adj = [dict() for _ in range(n + 1)]
    for u, v, w in edges:
        if v not in adj[u] or adj[u][v] > w:
            adj[u][v] = w
            adj[v][u] = w

    dist = [INF] * (n + 1)
    visited = [False] * (n + 1)
    dist[s] = 0

    heap = [(0, s)]
    while heap:
        d_u, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True

        for v, w_uv in adj[u].items():
            if not visited[v]:
                nd = d_u + w_uv
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

    return [
        -1 if dist[i] == INF else dist[i]
        for i in range(1, n + 1) if i != s
    ]

def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        edges = [tuple(map(int, input().split())) for _ in range(m)]
        s = int(input())
        ans = shortest_reach(n, edges, s)
        print(*ans)

if __name__ == "__main__":
    main()