# 3.29 웹 서비스 (day_21)

## 리팩토링

### form default

```html
<form action = '' method = ''>
</form>
<--! action의 default 주소는 자기 자신, method의 default 값은 GET-->
```

### form method

- GET
    - GET 메소드는 url에 data가 노출되어 보안에 취약함
        - DB에 영향을 끼치지 않는 작업(Read) 의 경우 사용됨
        - Dynamic URL 구현 시 해당 pk를 전달해야 하는 경우 사용됨
- POST
    - HTTP 요청 메소드 중 하나로, 서버로 데이터를 전송할 때 사용되는 메소드이다. 데이터를 body에 담아서 전송하기 때문에 url에 data가 노출되지 않는다.
    - CSRF(Cross-site request forgery) 공격을 방지하기 위해, POST 메소드를 사용할 때는 암호화 토큰`<csrf_token> #암호화 토큰`을 사용해야 한다.
    - DB에 영향을 끼치는 작업(Create, Update, Delete)은 POST 메서드를 사용하도록 권장된다.

## 앱 스페이싱
- 앱마다 있는 `views.py` 파일에 같은 이름의 함수가 정의되는 경우
    - django에서 먼저 선언된  app에 있는 함수를 실행해 보여줌
        1. 이를 방지하기 위해 app_name = ‘앱 이름’ 으로 설정
        2. ‘앱 이름 : 호출 함수’ 형으로 함수를 호출
        3. app_name을 통해 함수를 탐색해 시행