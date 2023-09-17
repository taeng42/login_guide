# APP 등록 절차
1. intra.42.fr 로그인
2. https://profile.intra.42.fr/oauth/applications/ 접속
3. [REGISTER A NEW APP] 버튼 클릭
4. 하단을 참고하여 적절한 데이터를 입력
    - Name: 적절한 이름 설정
    - Image: 업로드 필수 아님.
    - Description: 해당 app의 적절한 설명을 입력
    - Website: 가급적 메인 페이지 주소를 입력하라고 하지만 필수는 아님
    - Public: 특별한 이유가 없다면 체크 해제
    - Redirect URI: 로그인 후 토큰을 수신받을 페이지의 주소(도메인까지 정확하게 입력)
    - Scope: 특별한 용도가 없다면 전부 체크 해제. (예시 그림에는 체크가 되어있지만 무시)
    - ![app_registry](https://github.com/taeng42/login_guide/blob/main/readme_rsc/app_registry.png)
5. [Submit] 버튼 클릭
6. 자동으로 해당 앱의 정보 페이지로 이동될 것

# app_info.yaml 파일 설정
생성했던 앱의 정보 페이지를 참조하여 내용을 채웁니다.  
- UID: 앱 정보 페이지에서 UID의 내용을 입력 
- SECRET: 앱 정보 페이지에서 SECRET의 내용을 입력
- REDIRECT_URI: 앱 정보 페이지에서 REDIRECT URI의 내용을 입력. (빨간색 폰트의 주소를 입력하면 됩니다.)
- ![app_info_yaml_setting](https://github.com/taeng42/login_guide/blob/main/readme_rsc/app_info_yaml_setting.png)


# 설치 & 실행
```
$ docker compose up -d --build
```


# 테스트
1. 웹브라우저에서 http://127.0.0.1:8042/login/login 접속 후 [LOGIN BTN] 클릭
2. 로그인을 진행 후 이동된 페이지에서 동의 (이미 브라우저에서 인트라넷 로그인이 되어있으면 생략될 수 있습니다.)
3. 다시 이동된 페이지에서 json 데이터가 나온다면 정상적으로 테스트 된 것입니다. 


# 테스트 종료 후
```
$ docker compose down -v
```
