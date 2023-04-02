# 3.7 파이썬(day_5)

## 함수

- E = MC**2
    - Error = More Code ** 2
        - 코드가 장황해 질 수록 에러는 제곱으로 많아진다
        - 반복 작업은 되도록 함수화 / 표현하고자 하는 것은 장황하지 않게
- 선언과 호출
    
    ```python
    def 이름(parameter_1, parameter_2) :
    		코드 블럭 # 실행하고자 하는 내용
    ```
    
    - 변수는 재료, 코드블럭은 조리법, return 값은 요리
    - dir(**builtins**) : 파이썬 내장함수 목록을 보여주는 함수
    - **함수는 종료 시 단 하나의 리턴 값만을 반환**
        - 다수의 return 값 발생 시 tuple 로 묶어서 반환하는 것이 default
        
        ```python
        def passing (a,b):
        		return a,b
        
        print(passing(1,2))
        
        # 결과값은 (1,2)
        ```
        

<aside>
💡 함수 내에서 선언된 변수는 사용 후 메모리를 반환한다.

</aside>

- 가변 인자(가변 인자, 가변 키워드 인자)
    - *(asterlisk) 를 이용해서 입력값들을 튜플화 할 수 있음.
- LEGB Rule 변수 참조 법칙

```python
# Local scope: 함수
# Enclosed scope: 특정 함수의 상위 함수
# Global scope: 함수 밖의 변수 혹은 import된 모듈
# Built-in scope: 파이썬안에 내장되어 있는 함수 또는 속성

a = 1213
def func(a):
    a= 20
    print(a+1)
    del a
    print(a)
    return
func(1)

# 이 경우 파이썬이 컴파일 할 때 
# func() 함수 내부 모든 a를 이미 Local scape로 인식하기 때문에 a를 참조할 수 없는 값으로 설정하고
# Error 처리함
# UnboundLocalError: local variable 'a' referenced before assignment
# Local 변수 'a' 를 할당하기 전에 참조할 수 없다
# print() 함수에 a 를 할당하고 싶지만 Local 변수 중에 a를 찾을 수가 없네.. 라는 뜻
```

<aside>
💡 함수 내부(Local scope)에서는 아무리 지지고 볶아도 Global scope에 영향을 끼칠수 없음.

즉 우리가 Global scope에서 지지고 볶아도 Built-in scope 자체에 영향을 끼칠 수 는 없음.

global 메소드로 global scope 에 영향을 끼칠 수 있지만, 

reference type에서는 필요없기 때문에 숫자, 문자에만 쓰이는 편이다.

</aside>

- Exeption : reference type(참조객체) 는 이름에 할당된 값이 아닌 이름이 가르키는 값을 수정하는 것이기 때문에 global 과 local 의 경계가 없어진다…
    - 이럴 때 쓰라고 tuple이라는 존재가 있다 (희망)
    - c 포인터랑 다를게 없는 듯… 절망과 공포의 구간

---

### 자습 (23:00 ~ 23:30)

- 재귀함수에 대한 간단한 예습
    - 재귀함수란 결론적으로 함수 내에 부모 함수가 자식 함수가 되고 그 과정이 반복됨
        - 무한정 반복될 경우 메모리에 과부하 (stack over flow)
    - 그러므로 자식 함수의 인자는 부모 함수의 인자보다는 작아지면서 반복되어야하고 인자가 1 또는 설정한 값에 도달하면 멈출 수 있도록 안전장치를 걸어줘야 한다

내가 정의한 재귀함수는 이런 개념인데 내일 강의와 비교해보면 좋을 것 같다