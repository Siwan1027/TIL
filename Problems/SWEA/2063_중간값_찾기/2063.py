# import sys
# sys.stdin = open("input.txt")

length = int(input())
numbers = list(map(int, input().split()))
print(sorted(numbㄴers)[length // 2])