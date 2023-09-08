# baekjun problem no.18110

import sys

n = int(sys.stdin.readline())

def round_n(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

if not n:
    print(0)
else:
    scores = [int(sys.stdin.readline()) for _ in range(n)]
    trunc = round_n(n * 0.15)
    apply_trunc = sorted(scores)[trunc: n - trunc]
    average = round_n(sum(apply_trunc) / len(apply_trunc))
    print(average)