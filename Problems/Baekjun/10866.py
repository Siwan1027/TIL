# baekjun problem no.10866

from collections import deque
import sys

N = int(sys.stdin.readline())
queue = deque()

for n in range(N):
    c = sys.stdin.readline().split()
    if c[0] == 'push_front':
        queue.appendleft(int(c[1]))
    elif c[0] == 'push_back':
        queue.append(int(c[1]))
    elif c[0] == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif c[0] == 'pop_back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
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