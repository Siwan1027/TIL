# 3.6 파이썬(day_4)

---

## 중첩 조건문

```python
if ~~~ :
	print(~~~)
  if ~~~ :
	print (~~~)
```

```python
# 어렵지 않다
nums = [0, 1, 2, 3, 4]
for idx, num in enumerate(nums):
	print(f"{idx} = {num})

# enumarate() 는 (idx, 원소) 를 튜플형으로 반환해 줌
dic = {'john' : 50, 'eric' : 80}
for key, val in dic.item() :
	print(f"{key} => {val})
```

---

## list comprehension

```python
# list comprehension
list(num+1 for num in range(10))

# 반복문을 영어 문법에 맞춰 간단하게 작성할 수 있는 기법
```

<aside>
💡 이중 for문 내에서 if 문 작성할 때 앞에 공백을 잘 보자…

</aside>

```python
for num in numbers:
    for i in range(2, num):
        if num % i == 0:
            print(num,"은 소수가 아닙니다.", i, "는", num, "의 인수입니다.")
            break
    else:
        print(num, '은 소수입니다.')
# 위 코드와 아래 코드는 출력 횟수가 다르다...
for num in numbers:
    for i in range(2, num):
        if num % i == 0:
            print(num,"은 소수가 아닙니다.", i, "는", num, "의 인수입니다.")
            break
		    else:
		        print(num, '은 소수입니다.')
# 이 코드는 else 문이 2차 for 문 안에서 계속 돌기 때문에 마지막 판별 연산까지 계속 print() 가 돈다..
```