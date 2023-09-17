# baekjun problem no.10845

from collections import deque
import sys

N = int(sys.stdin.readline())
queue = deque()

for n in range(N):
    c = sys.stdin.readline().split()
    if c[0] == 'push':
        queue.append(int(c[1]))
    elif c[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif c[0] == 'size':
        print(len(queue))
    elif c[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    else :
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])