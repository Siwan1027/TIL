"""
1. 테스트 개수
2. 몇일 사이 가격 범위, len(n) 몇일간?
3. 내일보다 오늘이 싸면 산다? 아니면 최댓값보다 오늘이 싸면 산다!
4. 최댓값에 한번 팔았다 -> 그 다음부터는 내일보다 오늘이 싸면 사야지
5. 생각할게 너무 많은데...?

"""

T = int(input())
for cs in range(T):
    highest_price, profit = 0, 0
    days = int(input())
    daily_price = list(map(int, input().split()))
    daily_price.reverse()
    for day in range(days):
        if daily_price[day] > highest_price:
            highest_price = daily_price[day]
        else :
            profit += highest_price - daily_price[day]
    print(f'#{cs+1}', profit)
    print(f'#{cs+1}', profit)