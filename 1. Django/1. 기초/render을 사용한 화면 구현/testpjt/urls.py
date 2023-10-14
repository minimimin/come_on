"""
URL configuration for testpjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# include 쓸 때는 import 해주는 거 잊지말기!
from testapp import views
# 앱에서 views.py로 갈거니까 그거 불러오기 한다고 알려주기!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    # views.py의 어떤 함수를 쓰는 건지 알려주기!
    # 앱에는 
    path('testapp/', include('testapp.urls')),
    # 앱의 urls로 가도록 하는 거! 
    # 앱의 urls로 갔을 때는 앱의 모든 urls 주소들이 다 testapp/으로 시작한다
    # include 쓰면 앱이름.ulrs(가리키는 곳이 urls.py겠지?!)로 될 수 있도록
]
