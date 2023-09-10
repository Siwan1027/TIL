# baekjun problem no.1181

import sys

t = int(sys.stdin.readline())
words = []
for i in range(t):
    words.append(input())
words = set(words)
result = list(words)
result.sort()
result.sort(key=len)

for word in result:
    print(word)

