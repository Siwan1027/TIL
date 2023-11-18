# 스택/큐 > 주식가격

# prices	        return
# [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]


def solution(prices):
    answer = []
    queue = list(prices)
    index = 0

    while len(queue) > 0:
        price = queue.pop(0)
        count = 0
        for i in range(len(queue)):
            if price > prices[index + i]:
                break
            count += 1
        answer.append(count)
        index += 1
    return answer

prices1 = [1, 2, 3, 2, 3]
result = solution(prices1)
print(result)




