# baekjun problem no.10814

import sys

t = int(sys.stdin.readline())
users = []
for _ in range(t):
    age, name = sys.stdin.readline().split()
    users.append([int(_), int(age), name])

users.sort(key= lambda x:( x[1],x[0]))
for _ in range(t):
    print(f'{users[_][1]} {users[_][2]}')