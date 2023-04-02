# 3.17 웹 (day_13)

---

## Bootstrap

- CSS 관련 다양한 소스코드들
- bootstrap 소스를 코드에 넣을때 link는 <head> script는 <body> 끝에 넣는다.

---

### Grid 시스템

```css
<p class="contaienr d-flex"></p>
/* d-flex 가 의미하는 것은 해당 컨테이너를 flex 컨테이너로 만들겠다는 뜻*/
/* 해당 선언 후 해당 컨테이너 내부 객체들은 default 주축 row 와 교차축인 col을 통해 움직일 수 있음*/
/* day 15 flexbox froggy 참조*/
<p class="container fluid"></p>
/* 해당 선언 후 부터 해당 객체는 화면 크기와 상관없이 width 100% 에 맞춰 자동으로 비율 조정됨*/
```

- 한 가로 폭의 default 가 12인 상태에서 class 끼리 나눠먹는 구조
- xs ~ xxl 까지 값을 설정할 수 있다.
    - size table
        
        ![size_table](https://www.w3schools.com/html/img_sem_elements.gif)
        
    - size 는 row(가로폭) 을 px 사이즈 기준으로 나눠놓은 사이즈
    
    ```html
    <!-- 이런 식으로 객체마다 설정할 수 있다. -->
    <article class="col-sm-12 col-md-6 col-lg-3 card">
    	<img src="./images/buds.jpg" alt="galaxy buds image" class="image-top">
    		<div class="card-body">
    			<div class="card-title">Galaxy Buds</div>
    			<div class="card-text">179,000</div>
    		</div>
    </article>
    <!-- 이런 식으로 div 내의 모든 객체에 한번에 지정해 줄 수도 있다. -->
    <!-- 이때는 cols 다음 숫자가 한 열에 몇개의 content가 들어갈 것인지 설정한다.12/숫자 개수 X -->
    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4">
    	<article class="card cols">
    		<img src="./images/buds.jpg" alt="galaxy buds image" class="image-top">
    			<div class="card-body">
    				<div class="card-title">Galaxy Buds</div>
    				<div class="card-text">179,000</div>
    			</div>
    	</article>
    </div>
    
    ```
    

---

### Semantic tags

- semantic tags table
    |  | xs | sm | md | lg | xlg | xxlg |
    | --- | --- | --- | --- | --- | --- | --- |
    | 컨테이너 | 없음(자동) | 540px | 720px | 960px | 1140px | 1320px |
    | 클래스 접두사 | .col | .col-sm- | .col-md- | .col-lg | .col-xlg | .col-xxlg |
    | 열 개수 | 12 | --- | --- | --- | --- | --- |
    | 거터 너비 | 1.5rem 좌우 각 0.75 | --- | --- | --- | --- | --- |
    | 사용자 정의 거터 너비 | 가능 | --- | --- | --- | --- | --- |
    | 중첩 | 가능 | --- | --- | --- | --- | --- |
    | 열 정렬 | 가능 | --- | --- | --- | --- | --- |


- 각각의 요소가 실제 의미하는 역할대로 부여하는 tags
    - 코드의 가독성, 유지보수 ⬆️
- Semantic Tags 종류
    
    
    | 태그 | 설명 | 비유 |
    | --- | --- | --- |
    | \<header> | 머릿글을 정의 | 신문의 제목 |
    | \<nav> | navigation 링크 | 신문의 나눠진 섹션을 한눈에 볼 수 있는 탭 |
    | \<section> | 문서의 구역을 나눔 | 경제, 정치, IT 처럼 파트를 나눔 |
    | \<article> | 내용을 나눔 | 파트 내에서 서로 다른 기사들을 나눔 |
    | \<aside> | 사이드에 존재하는 바 | 신문 양측에 광고, 해당 섹션과 상관없는 정보를 넣은 탭 |
    | \<footer> | 가장 밑에 존재하는 바 | 신문의 발행일자, 주석, 발행업체 등의 정보를 담은 가장 밑에 구간 |