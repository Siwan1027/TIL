# baekjun problem no.9375
import sys
import itertools

n = int(sys.stdin.readline())

for _ in range(n):
    clothes = int(sys.stdin.readline())
    box = {}
    result = 1
    for _ in range(clothes):
        cloth, category = sys.stdin.readline().split()
        if box.get(category) == None:
            box[category] = [cloth]
        else:
            box[category].append(cloth)
    for key in box:
        box[key].append('nude')
    for key in box:
        result *= len(box[key])

    print(result-1)