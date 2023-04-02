# 3.20 서버 (day_14)

---

## 서버 개발

- 직접 개발은 처음부터 창업 / Framework는 체인점 창업으로 볼 수 있다.

---

### 직접 개발

- 서버의 모든 요소를 직접 설정하며 처음부터 개발하는 것을 의미함
- 모든 요소를 직접 설정할 수 있기 때문에 자유도가 높다는 장점이 있음

---

### Framework[django]

- Django 설치 / Project 생성
    1. django 설치 [수업에서는 3.2.18 사용]
        1. Django의 버전에는 LTS(Long Term Service)버전과 개발단계의 버전이 있다. LTS가 완성도가 높으며 현업에서는 프로젝트를 장기적인 관점에서 관리해야하기 때문에 LTS를 주로 사용한다.
        2. `pip install django==3.2.18`
    2. django 로 프로젝트 만들기
        1. django-admin startproject 제목
            1. `Django-admin startapp . 제목`
            2. `.` 으로 현재 폴더에 바로 Root DIR을 생성할 수 있다.
        2. django 명령어는 django-admin으로 기본 명령어 확인 가능
        3. project 안에 매니저 `manage.py` 를 통해서 서버를 열 수 있음.
    3. Django 로 app 만들기
        - `Django-admin startapp 제목`
        - App을 생성하고 나서는 BASE_DIR의 setting.py에 앱을 꼭 등록해줘야 한다.
            - 등록 순서에 따라 작업 실행 시 탐색 순서가 달라진다.

<aside>
💡 다른 Framework 로는 Flask, FastAPI 등이 있다.

</aside>