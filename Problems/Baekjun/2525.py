# https://www.acmicpc.net/problem/2525

hour, minute = map(int,input().split())
cook_time = int(input())
now_time = hour * 60 + minute
# 분 단위로 변환
com_time = now_time + cook_time
if (com_time // 60) >= 24:
    com_time -= (24*60)
    print(com_time // 60, com_time % 60)
else:
    print(com_time // 60, com_time % 60)