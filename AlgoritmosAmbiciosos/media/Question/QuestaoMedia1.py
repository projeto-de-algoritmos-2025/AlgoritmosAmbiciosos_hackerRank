import sys
import heapq

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    s = int(next(it))
    respostas = []
    for _ in range(s):
        n = int(next(it))
        intervals = []
        for i in range(n):
            a = int(next(it))
            b = int(next(it))
            intervals.append((a, b, i))
        events = []
        for (a, b, idx) in intervals:
            events.append((a,  1, idx, b))
            events.append((b, -1, idx, b))
        events.sort(key=lambda x: (x[0], -x[1]))
        selected = [False] * n
        active   = [False] * n
        heap = []
        active_count = 0
        for (time, typ, idx, end_time) in events:
            if typ == 1:
                active[idx] = True
                selected[idx] = True
                active_count += 1
                heapq.heappush(heap, (-end_time, idx))
                if active_count > 2:
                    while heap:
                        neg_b, j = heapq.heappop(heap)
                        if selected[j] and active[j]:
                            selected[j] = False
                            active_count -= 1
                            break
            else:
                if selected[idx]:
                    active_count -= 1
                active[idx] = False
        resultado = sum(selected)
        respostas.append(str(resultado))
    sys.stdout.write("\n".join(respostas))
if __name__ == "__main__":
    main()