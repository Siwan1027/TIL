# https://www.acmicpc.net/problem/5063

T = int(input())

for cs in range(T):
    non_ad, ad, ad_fee = list(map(int, input().split()))
    if non_ad > ad - ad_fee:
        print("do not advertise")
    elif non_ad == ad - ad_fee:
        print(("does not matter"))
    else :
        print("advertise")