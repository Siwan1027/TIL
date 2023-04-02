# 3.22 서버(day_16)

---

## 웹크롤링

- import requests, beautifulsoup 활용한 웹크롤링
    - requests 모듈로 웹페이지의 내용을 불러온 후, beautifulsoup 모듈로 HTML 문서를 파싱하여 필요한 정보를 추출할 수 있다.
- BeautifulSoup을 사용한 HTML 파싱
    - BeautifulSoup을 사용한 HTML 파싱
        - HTML 문서에서 필요한 정보를 추출하는 방법으로, BeautifulSoup 라이브러리를 활용하여 태그를 찾고 속성값을 불러올 수 있다. 이를 통해 웹크롤링을 할 수 있다.

---

## html form tag

- GET
    - GET 메소드는 url에 data가 노출되어 보안에 취약함
        - DB에 영향을 끼치지 않는 작업(Read) 의 경우 사용됨
        - Dynamic URL 구현 시 해당 pk를 전달해야 하는 경우 사용됨
- POST
    - HTTP 요청 메소드 중 하나로, 서버로 데이터를 전송할 때 사용되는 메소드이다. 데이터를 body에 담아서 전송하기 때문에 url에 data가 노출되지 않는다.
    - CSRF(Cross-site request forgery) 공격을 방지하기 위해, POST 메소드를 사용할 때는 암호화 토큰`<csrf_token> #암호화 토큰`을 사용해야 한다.
    - DB에 영향을 끼치는 작업(Create, Update, Delete)은 POST 메서드를 사용하도록 권장된다.

---

## 동적주소할당법

- Path(<변수형:변수명>, views.detail, name=‘detail’)
    - url에서 동적으로 변하는 부분을 처리하기 위한 방법으로, <변수형:변수명> 형식으로 작성하여 변수명을 지정할 수 있다. 이후 views.py에서 해당 변수를 활용하여 동적으로 데이터를 처리할 수 있다.

---

## templates 을 모듈화하는 방법, 이유

- html 중 공통된 부분을 하나에 작성 후 extend 하여 사용
    - html 작성 시간이 단축, 수정사항 발생 시 한번에 수정 가능하여 유지 보수성 향상
    - 대표적인 예
        - project BASE_DIR에 template dir 생성 후 웹서비스에 html들에서 공통적으로 사용되는 부분을 작성하여 저장 관습적으로 base.html로 선언

```bash
# BASE_DIR/settings.py

'DIRS': [BASE_DIR, 'templates'],
# BASE_DIR의 templates 폴더를 탐색하도록 선언해야 함.
```