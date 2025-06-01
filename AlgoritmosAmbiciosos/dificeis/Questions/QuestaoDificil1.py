import sys
import threading

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    it = iter(data)
    T = int(next(it))
    jobs = []
    max_d = 0

    for _ in range(T):
        d = int(next(it))
        m = int(next(it))
        jobs.append((d, m))
        if d > max_d:
            max_d = d

    size = 1
    while size < max_d:
        size <<= 1

    N = size
    INF = 10**18

    tree_sum  = [0] * (2 * N)
    tree_moff = [0] * (2 * N)

    for i in range(N):
        pos = N + i
        if i < max_d:
            d = i + 1
            tree_sum[pos] = 0
            tree_moff[pos] = -d
        else:
            tree_sum[pos] = 0
            tree_moff[pos] = -INF

    for pos in range(N - 1, 0, -1):
        lc = pos << 1
        rc = lc | 1
        s_left = tree_sum[lc]
        s_right = tree_sum[rc]
        tree_sum[pos] = s_left + s_right
        mo_left  = tree_moff[lc]
        mo_right = tree_moff[rc]
        tree_moff[pos] = mo_left if (mo_left >= mo_right + s_left) else (mo_right + s_left)

    out = []
    for (d, m) in jobs:
        pos = N + (d - 1)
        tree_sum[pos] += m
        tree_moff[pos] = tree_sum[pos] - d

        pos >>= 1
        while pos:
            lc = pos << 1
            rc = lc | 1
            s_left = tree_sum[lc]
            s_right = tree_sum[rc]
            tree_sum[pos] = s_left + s_right

            mo_left  = tree_moff[lc]
            mo_right = tree_moff[rc]
            tree_moff[pos] = mo_left if (mo_left >= mo_right + s_left) else (mo_right + s_left)
            pos >>= 1

        lateness = tree_moff[1]
        if lateness < 0:
            lateness = 0
        out.append(str(lateness))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    threading.Thread(target=main).start()