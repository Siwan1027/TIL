# 3.28 웹 서비스 (day_20)

---

## FORM

- forms.py 의 생성
    - forms를 필요로 하는 app 에 python파일로 생성
        - 사용자 입력이 있는 경우 반필수적으로 사용
- forms.py의 역할
    1. **사용자 입력 유효성 검증**
    2. views 받아온 입력을 필드 매칭 자동화
    3. HTML에 input 태그 생성 자동화
        - 04_form에 `view.py` html들 참조
        
        ```python
        from django import forms
        
        form = ~~~form()
        
        # HTML
        # {{ form.as_p }} 필요로 하는 데이터에 대한 입력창을 자동으로 생성
        ```