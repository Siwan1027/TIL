# baekjun problem no.1920

import sys
from collections import deque

n = int(sys.stdin.readline())

for i in range(n):
    ps = list(sys.stdin.readline().strip())
    queue = deque()
    if ps[0] == ')' :
            result = 'NO'
    else:        
        for _ in ps:
            if _ == '(':
                queue.append(1)
            else:
                try:
                    queue.pop()
                except:
                     result = 'NO'
                     break
            result = 'NO' if len(queue) else 'YES'
    print(result)