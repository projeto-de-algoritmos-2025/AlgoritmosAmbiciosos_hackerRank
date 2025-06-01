import sys
import heapq

def prims(n, edges, start):
    adj = [[] for _ in range(n+1)]
    for u, v, w in edges:
        adj[u].append((w, v))
        adj[v].append((w, u))
    
    visited = [False] * (n+1)
    total_weight = 0
    heap = []
    
    visited[start] = True
    for w, v in adj[start]:
        heapq.heappush(heap, (w, v))
    
    while heap:
        w, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += w
        for w2, v2 in adj[u]:
            if not visited[v2]:
                heapq.heappush(heap, (w2, v2))
    
    return total_weight

if __name__ == "__main__":
    data = sys.stdin.read().split()
    it = iter(data)
    n, m = int(next(it)), int(next(it))
    edges = [(int(next(it)), int(next(it)), int(next(it))) for _ in range(m)]
    start = int(next(it))
    print(prims(n, edges, start))