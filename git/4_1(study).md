# 4.1 (자습)

---

## 4주차 내용 정리 / 복습

---

## 개인 프로젝트 (blog 만들기)

---

## Git & GitHub 활용

---

### SourceTree

- venv 제외하기
    - .gitignore 활용하기
        - 해당 파일을 통해 로컬저장소에 저장하지 않을 폴더, 파일을 지정할 수 있음
            
            ```bash
            # .gitignore 생성
            touch .gitignore
            # 생성 확인
            ls -a
            # vi 편집기로 열기
            vi .gitignore
            # 일반적으로 생략되는 파일
            venv
            __pycache__
            DS.Store
            ```
            
- 터미널 명령어
    
    
    | 명령어 | 의미 |
    | --- | --- |
    | git init | git local 저장소 생성 |
    | git add . | 스테이징 | add 뒤 파일을 스테이지에 올림 |
    | git status | 현재 프로젝트 관리 진행도 확인 |
    | git config —global http://user.name / user.email | 깃허브 id . email을 등록 |
    | git remote add origin [route] | route를 깃허브와 연동 |
    | git commit -m ‘커밋 메시지’ | -m : 메시지를 입력한다 | 커밋과 함께 커밋 메시지를 남긴다. |
    | git log | 작업 내역 확인 |
    | git push origin master | origin : 원격 저장소를 뜻함 | 원격저장소에 commit 내역을 올림 |
    | git push origin [bridge name] | 다른 브랜치에 작업 내용을 올림 |
    | git push origin —all | 모든 브랜치를 업로드 |
    | git merge [branch name] | [branch name] 브랜치를 마스터 브랜치에 병합 |
    

---

## vi 편집기

---

### Command Mode

- 커서 이동
- line, letters 복사 및 삭제
- Command
    
    
    | Command | Description |
    | --- | --- |
    | dd | 커서가 위치한 줄 삭제 |
    | yy | 커서가 위치한 줄 복사 |
    | p | 붙여넣기 |

### Insert Mode

- 내용 입력
- Command
    
    
    | Command | Description |
    | --- | --- |
    | i | 현재 커서 앞에서 입력 시작 |
    | a | 현재 커서 뒤에서 입력 시작 |
    | esc | 입력 모드 종료 |

### Colone Mode

- 저장
- 종료
- Command
    
    
    | Command | Description |
    | --- | --- |
    | : | Colone mode 진입 |
    | q | 종료 |
    | q! | 강제종료 |
    | w | 저장 |
    | wq | 저장 후 종료 |
    | wq 파일 이름 | 파일 이름 지정, 저장 후 종료 |

---

## 마케팅 기본

---