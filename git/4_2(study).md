# 4.2 자습

---

## GitHub 인증오류

- 21.08 부터 보안상의 문제로 비밀번호로 인증하는 것을 제한
- PAT(Private Access Token)를 활용하여 인증

### GitHub PAT 발급

- Github Developersettings 에서 발급 가능
- 생성 시 권한 설정 가능
- 생성 시 보여주는 키는 이후 확인 불가
- expire 기한 설정 가능

---

## SourceTree

- GitHub PAT 연결
    1. 설정 → 계정 이동
    2. 계정 추가
    3. 암호에 PAT 발급 시 같이 발급된 키 입력
    4. HTTPS 프로토콜 사용
        - if ssh 사용 시 github에서 ssh 추가 발급 필요

---

## Terminal

- GitHub PAK 연결
    1. `git config --global credential.helper osxkeychain`
        - 터미널에서 git 에 접근시 osxkeychain을 사용하겠다고 설정
        - `git config --global credential.helper` 입력하여 적용 확인
    2. `git credential-osxkeychain store`
        - 빈 입력칸 생성
        
        ```python
        host=github.com
        protocol=https
        username=[내 깃헙 username]
        password=[PAT 생성 시 발행된 키]
        # 엔터 두 번 입력 시 종료
        ```
        

<aside>
💡 expired token 삭제 시 기존 keychain 같이 삭제

</aside>