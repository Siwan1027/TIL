# 3.15 웹 (day_11)

---

![Request_Response](https://blogs.brain-mentors.com/content/images/size/w1600/2023/02/image.png)

- WEB 환경은 요청(Request)은 URL(Uniform Resource Locator)로, 응답은 문서 한 장(주로 HTML)로 돌아간다.

## URL(Uniform Resource Locator)

- 웹페이지, 이미지, 비디오 등의 위치를 가르키는 문자열(Hyper text)

## HTML(Hyper Text Markup Language)

1. Head
    - 해당 HTML에서 데이터가 가진 속성을 설정, 설명해주는 데이터(meta datas)들을 포함
    - 해당 HTML이 참조할 문서, 데이터셋을 삽입할 수 있음
    - metadata
        
        
        | <title>제목</title> | 해당 HTML의 제목 지정 |
        | --- | --- |
        | <style> .con{} </style> | HTML 문서의 style 정의 |
        | <link rel=”” href=”#”> | rel 은 #와의 관계 href는 참조 데이터 / 외부 리소스와 연계(HTML↔CSS) |
        | <meta charset="utf-8"> | 컴퓨터가 문자열을 해석하는 방법 지정한다. |
        | <meta name = “keyword” content=”~,~,~” | content를 keyword로 지정하여 검색엔진이 탐색하기 쉽게 한다. |
        | <meta name = “discription” content=”discription”> | 해당 html의 간략한 설명을 지정한다. |
2. Body
    - HTML에서 실제 뼈대를 담당하는 구간

### Attribute

- global attributes
    
    
    | Attributes | Description |
    | --- | --- |
    | id | 유일한 식별자 요소 지정, javascript 와 겹치는 부분이 많아 id 로 속성을 지정하는 경우는 거의 없다. |
    | class | 해당 개체에 class 를 지정한다. bootstrap 와 같은 오픈소스 stylesheet 에서 받아온 css 에 영향을 많이 받는다. |
    | hidden | css의 hidden 과 다르게 브라우저에 나오지 않는다. |
    | lang | 언어 지정, 검색엔진(robot.txt) 해당 웹페이지의 언어를 인식하게 한다. |
    | style | 요소의 인라인 스타일을 지정한다. |
    | tabindex |  |
    | title | 해당 요소의 제목을 지정한다. |

### 기본 Tags

| Tags | 의미 |
| --- | --- |
| <title>제목</title> | 제목 지정 |
| <link rel=”” href=”#”> | rel 은 #와의 관계 href는 참조 데이터 |
| <a href=”#”> text </a> | 해당 내용(text)을 클릭 시 # 로 이동한다. <a></a> 사이에 넣는 요소를 링크로 만들 수 있다. |
| <script></script> | client side Javascript 를 정의한다. |
| <h#></h#> | h1~h6까지 소제목으로 분할하여 표현 가능 |
| <mark>강조!</mark> | ‘강조!’ 를 밑줄친다. |
| <p></p> | paragraph - 문단을 나눌때 쓰임 |
| <br> | break - 강제 개행 |
| <ul></ul> | Unordered List - 순서가 없는 리스트 |
| <li></li> | List - 순서가 있는 리스트 [li*int] 처럼 한번에 리스트를 선언할 수 있다. |
| <img src=”소스의 파일 경로” alt=”기본 설명”> | src 가 가르키는 img 파일을 불러온다. 이미지가 없으면 alt를 표시한다. |