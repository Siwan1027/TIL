# 3.2 파이썬(day_2)

---

## Markdown Editor

---

### 글의 구조화

#의 개수를 통해 상위 제목과 하위 제목을 나눠 글을 구조화

#1개 (제목1)의 경우 문서에서 하나만 들어가는 것이 보통적으로 맞음

---

### 줄 글 강조하기

**이거 볼드 되나 앞뒤를 **로 감싸면 볼드**

**이걸로 감싸면 기울이기*

~ ~~이걸로 감싸면 삭선~~

`이걸로 감싸면` 코드는 `(opt + 원화)이걸로 감싸기

---

### 단락 활용하기

목록 ⇒ 

순서 O

1. 마크다운 배우기
2. 점심먹기
3. 파이썬 배우기
    - 변수
    - 입출력
    - 기본 문법 등등등

순서 X

- md
- python
- django

```markdown
```python
import webbrowser

webbrowser.open('naver.com')
```
```

---

연습 파일

[basic.md]

---

|이렇게|표를|표현한다|

|—-|—-|—-|

|—-| —-| —-|

### 수식

- python 에서 math, numpy 라이브러리를 자주 사용

$$

x+y=10

$$

---

## 파이썬

1. jupyter 설치로 시작

```bash
pip install jupyter
```

`python -V` 명령어에서 python 명령어 자체가 존재하지 않는다고 나옴 

환경변수 설정에 문제

jupyter 노트북은 terminal 을 통해서 구동됨

```jsx
"echo $환경변수명"을 입력하여 변수 값을 확인할 수 있음
"echo $PATH"를 입력하면 PATH 변수의 값을 확인할 수 있음
```

- `jupyter notebook` 으로 실행시켰을때 화면

[https://www.notion.so](https://www.notion.so)

h = 도움말

jupyter 내의 파일을 사용해서 실습

새롭게 알게 된 점

```jsx
a = 13e10 # 일 때 e는 10 뒤에 숫자는 제곱
```

- 수 체계
    - 파이썬은 정수, 실수, 복소수까지 커버
        
         `a = 3-4j #j는 -2`
        

![수체계](https://velog.velcdn.com/images/solfe/post/d5bc22cb-5528-4e3f-847c-8c17c481f35a/image.png)

- 비교연산자
    - and 연산은 [0,None,False] 값이 나온 순간 연산 종료
        - why? 하나만 False 값이 나오는 경우 모두 어쨋든 False
    - or 연산은 [0,None,False 등 …] 이 아닌 값이 나온 순간 연산 종료
        - why? 하나만 True 값이 나오는 경우 모두 어쨋든 True