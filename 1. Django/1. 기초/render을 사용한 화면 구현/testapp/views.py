from django.shortcuts import render

# -------------------------------------------------------------------------------------

def index(request):
    # 무조건 request를 매개변수로 받아야한다.
    # 거기에 추가로 원하는 거(예) pk 등) 더 받아 올 수 있음
    return render(request, 'testapp/index.html')
    # 매개변수, 이동할 템플릿, 딕셔너리(이거는 선택사항)

# -------------------------------------------------------------------------------------

def first(request):
    return render(request, 'testapp/first.html')

# -------------------------------------------------------------------------------------

def second(request):
    # 다른 곳에서 받아오는 건 여기다 어떤 거 받아올 지 적어줘야해!!!!!!
    # request.GET 요청 중 딕셔너리 받아오는 거 의미하거든?
    # 그래서 get()함수를 써서 받아오는 곳의 어느 요소 이름(키의 값)을 가지고 올지 확인해야해!
    ID = request.GET.get('name')
    password = request.GET.get('bimil')
    # ★ GET을 통해 받으면 받는 곳으로 바로 넘어가게 되어있더라!! 신기해!!!
    content = {
        'ID' : ID,
        'password' : password,
        # 키는 문자열!!!!! 값은 위에 저장된 변수!!!!!!
    }
    return render(request, 'testapp/second.html', content)

# -------------------------------------------------------------------------------------

def third(request, sam):
    # url에서 받아온 변수를 인자로 받음
    name = sam
    content = {
        'name':name,
}
    return render(request, 'testapp/third.html', content)

# -------------------------------------------------------------------------------------
