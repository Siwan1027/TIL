# 3.21 서버(day_15)

---

## django VMT

- Django framework process

![django_MVT](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page/basic-django.png)

- Request → urls → view → template → view →Response

### urls

- Request의 url 을 통해 framework 내의 경로를 설정해주는 역할을 한다. (이정표!)
    - Root dir에서는 app으로의 경로를
    - App에서는 view로 보냄으로써 해당 url이 입력됐을때 실행해야 할 작업을 안내한다.

### view

- Urls를 통해 안내된 request에 대한 작업을 실질적으로 시행하는 역할을 한다.
- 해당 서비스에서 필요로 하는 작업들을 함수로 선언하여 해당 url이 request 되었을때 해당 함수를 시행한다.
    - 주로 쓰이는 return
    - `Return render(request, ‘~~.html’ , context)`
        - request 에 대한 return값으로 ‘~~.html’ 을 보여줌
        - Context[key:value]를 통해 선언한 변수를 해당 함수 및 해당 함수가 사용하는 html안에서 사용할 수 있음
    - `Return redirect(request, ‘/app/index/‘)`
        - 함수 종료후 ‘/app/index/‘로 urls을 바꿔서 리턴함

### template

- 해당 서비스에서 사용되는 html을 모아두는 폴더
- Django에서는 모든 template 파일을 한 곳으로 모아서 관리함
    - Name spacing
        - 위 특성으로 인하여 html 파일을 불러올때 다른 앱에서 사용하는 html파일과 이름이 같을 경우 먼저 선언된 app의 html만을 사용하게 됨
        - 이에 대한 해결책으로 template 폴더 안에 하나의 폴더를 더 생성하여 그곳에 파일을 저장함으로서 html 파일에 꼬리표를 붙여주는 방식
            - 이때 template 폴더 안에 생성되는 폴더의 이름은 해당 app의 이름과 통일하는 것이 관습
            

### Model

- DB에 저장할 테이블의 틀을 선언하는 파일
- 1 class = 1 schema
- ORM(object relational mapper)
    - DjangoORM(django 내장)
    - table을 수정할 때는 app/[models.py](http://models.py) 에서 수정한다.