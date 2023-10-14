# 프로젝트 urls에서 include한 경우에
# 앱 내 직접 파일 만들어서 추가해줘야한다!

from django.urls import path
from . import views
# 해당 앱 내의 views를 불러올거니까 .으로 표현

app_name = 'testapp'

urlpatterns = [
    path('first/', views.first, name='first'),
    path('second/', views.second, name='second'),
    # 앱 이름과 함수(경로)이름 지정해주기-html에서 urls로 이동시킬때 사용됨
    # 앱:경로명 이런 형식으로!
    path('third/<str:sam>/', views.third, name='third'),
    # 주소(url)에 변수(view함수 인자로 전달 가능)를 포함시키는 것
    # <타입:이름> 형태로 저장!
]