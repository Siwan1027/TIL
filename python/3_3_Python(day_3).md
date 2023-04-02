# 3.3 파이썬(day_3)

---

## 문자열 인덱싱, 슬라이싱

관련해서는 위키독스, jupyter notebook 내 예제 파일을 참고하자

문자열은 메모리 내에 아래 형태로 저장된다.

`h = "python"`

| 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| p | y | t | h | o | n |

### Indexing `(주소를)목록화하다`

```python
h[0] = p, h[1] = y
```

### Sclicing `잘라서 구분짓다 같다`

```python
h[0:2] = py
h[2:4] = th
```

---

## 컨테이너

### 시퀀스 형

- python 관례
    - 변수명은 복수형
    - = 앞뒤 띄기
    - , 뒤에 띄기
    - 마지막에도 , 붙이기 **[trailing comma]**
- 리스트(mutable)
    
    ```python
    
    nums_1 = list(),[]
    nums_2 = [1,2,3,4]
    ```
    
- 튜플(immutable)
    
    ```python
    nums_1 = tuple(), ()
    nums_2 = (1,2,3,4,5)
    ```
    
- 레인지(immutable)
    
    ```python
    arg = range(x, y, z)
    ```
    
    - range 는 범위를 설정하는 것일 뿐 리스트나 튜플형태로 반환되지 않는다.

### 비시퀀스 형

- 세트(mutable)
    
    ```python
    s1 = {1, 2, 3, 3, 4, 4, 5, 5, 6,}
    s2 = set()
    ```
    
    - 중복을 허용하지 않는다.
    - 리스트의 중복제거 시 자주 사용하게 됨.
- 딕셔너리(mutable)

```python
dic_1 = {'one': 1, 'two': 2, 'three': 3}
```

- value 는 mutable

---

## 멤버십 연산자

- in

```python
a = [113,124,234]
1 in a
False
1 in range(3)
True
1.1 in range(3)
False
```

- not in
    - in 연산 값의 반전값

---

### 자습

<aside>
💡 문제 풀이 중 알게 된 점

</aside>

1. 입력받는 값을 list에 동적할당 해주기 위해서 append() 메소드를 사용한다.

```python
# 값을 3개 입력받아 가장 큰 수를 출력
nums = []
cnt = 0
for cnt in range(3) :
	x = input("enter num :")
	cnt += 1
	nums.append(x)
	# num 에는 크기 상관없이 nums[0] 부터 값이 입력된다
nums.sort()
print(nums[-1])
```