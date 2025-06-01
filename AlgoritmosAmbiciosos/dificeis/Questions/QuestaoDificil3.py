#!/bin/python3
# MST

import math
import os
import random
import re
import sys


def main():
    import sys
    input = sys.stdin.read().split()
    g = int(input[0])
    idx = 1
    for _ in range(g):
        n = int(input[idx])
        m = int(input[idx+1])
        s = int(input[idx+2])
        idx +=3
        
        min_edges = n - 1
        max_possible_edges = n * (n - 1) // 2

        if s < min_edges or m < min_edges or m > max_possible_edges:
            print(-1)
            continue

        k = (s + min_edges - 1) // min_edges
        t = k * min_edges - s

        c_t_2 = t * (t - 1) // 2 if t >= 2 else 0

        add_edges_needed = m - min_edges 
        use_k_minus_1 = min(add_edges_needed, c_t_2)
        remaining = max(0, add_edges_needed - use_k_minus_1)

        sum_add = use_k_minus_1 * (k - 1) + remaining * k
        total = s + sum_add

        print(total)

if __name__ == "__main__":
    main()
