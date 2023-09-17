from django.http import HttpResponse


def index(request):
    """
    흐름과 관계 없는 부분입니다. 무시하세요
    """
    HttpResponse("Hello!")


def simple_auth(_uid: str, _secret: str, _code: str, _redirect_uri: str):
    """
    간략하게 만들어 본 인증 과정입니다.
    """
    import json

    """
    urllib3 -> http request를 활용하기위한 라이브러리입니다.
    """
    import urllib3

    #############################################################
    """
    base_url & auth_data
        : https://api.intra.42.fr/apidoc/guides/web_application_flow
    """
    base_url = "https://api.intra.42.fr/oauth/token"
    auth_data = {
        "grant_type": "authorization_code",
        "client_id": _uid,
        "client_secret": _secret,
        "scope": "public profile projects tig elearning forum",
        "code": _code,
        "redirect_uri": _redirect_uri,
    }
    #############################################################

    _session = urllib3.PoolManager()
    response = _session.request(method="POST", url=base_url, fields=auth_data)
    _response_dict = json.loads(response.data.decode("utf-8"))
    _token = _response_dict["access_token"]

    #############################################################
    """
    headers update!
    """
    _session.headers.update({"Authorization": f"Bearer {_token}"})
    #############################################################
    return _session


# this is http://127.0.0.1:8042/login/login
def login(request):
    with open("app_info.yaml", "r", encoding="utf-8") as _f:
        import yaml

        app_info = yaml.load(_f, Loader=yaml.FullLoader)
        _signin = (
            "https://api.intra.42.fr/oauth/authorize"
            + "?client_id="
            + app_info["UID"]
            + "&redirect_uri="
            + app_info["REDIRECT_URI"]
            + "&response_type=code"
        )
    btn = f"<a href='{_signin}'>LOGIN BTN</a>"
    return HttpResponse(btn)


def simple_get(_session, _url):
    import json

    resp = _session.request(method="GET", url=_url)
    return json.loads(resp.data.decode("utf-8"))


# this is http://127.0.0.1:8042/login/receive
def receive(request):
    with open("app_info.yaml", "r", encoding="utf-8") as _f:
        import yaml

        app_info = yaml.load(_f, Loader=yaml.FullLoader)
        _uid = app_info["UID"]
        _secret = app_info["SECRET"]
        _redirect_uri = app_info["REDIRECT_URI"]
        """
        # _redirect_uri = "http://127.0.0.1:8042/login/receive"
            : 지금 이 엔드포인트의 주소입니다.
            [!] 반드시 "설정"한 Redirect URI와 같은 주소의 엔드포인트를 생성하고,
             그곳에서 수신 받아주세요.
            [!] 도메인도 동일해야합니다.
        """

    _code = request.GET["code"]
    """
    # _code = request.GET["code"]
    : code는 redirect uri를 타고 오면 자동으로 랜덤 생성됩니다.
    """

    _session = simple_auth(_uid, _secret, _code, _redirect_uri)
    ## 이제 인증 과정은 종료되었습니다.

    ## 이번에는 본인의 정보를 받아와봅시다.
    me = simple_get(_session, "https://api.intra.42.fr/v2/me")
    """
    # me = simple_get(_session, "https://api.intra.42.fr/v2/me")
        : https://api.intra.42.fr/v2/me > https://api.intra.42.fr/apidoc/2.0/users/me.html
        TLDR; 로그인을 진행 한 자기 자신의 계정 데이터를 받아오는 엔드포인트입니다. 
    """
    is_staff = me["staff?"]
    """
    # is_staff = me['staff?']
        : `staff?' 속성은 해당 계정의 스태프 여부를 식별 할 수 있도록 도와줍니다. 
    """
    return HttpResponse(str(is_staff) + "<br>" + str(me))
