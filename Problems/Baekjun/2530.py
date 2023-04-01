# https://www.acmicpc.net/problem/2530

hour, minute, sec = map(int,input().split())
cooking_sec = int(input())
now_time = hour * 360 + minute * 60 + sec
com_time = now_time + cooking_sec
com_hour, com_min, com_sec = com_time // 360,
# 초 단위로 변환
if (com_time // 360) >= 24:
    com_time -= (24*360)
    print(com_time // 360, com_time % 60)
else:
    print(com_time // 60, com_time % 60)



